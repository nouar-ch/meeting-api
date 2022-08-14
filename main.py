from flask import Flask, request, jsonify
from pyrfc3339 import parse, generate
import pytz
from datetime import timedelta
import holidays

APP = Flask(__name__)


## Calculate the best date and time from the intersection between the time intervals.
def calculate_best_dates(dates):
    # Parse the dates into python datetime objects.
    parsed_dates = list(
        {
            **el,
            'from': parse(el['from']).astimezone(tz=pytz.utc),
            'to': parse(el['to']).astimezone(tz=pytz.utc)}
        for el in dates
    )

    for date in parsed_dates:
        # Check if the day is a weekend, if so we cannot have the meeting.
        if date['from'].date().weekday() >= 5:
            return []
        
        # Check if the given date is a holiday. If so the user cannot attend and we return [].
        if getattr(holidays, date['CC'])().get(date['from']) is not None:
            return []

    # Looking for the biggest start time in the list (the latest time available to start)
    from_max_date = max(list(dates['from'] for dates in parsed_dates))

    # Looking for the smallest finish time in the list (the earliest we have to finish)
    to_min_date = min(list(date['to'] for date in parsed_dates))

    # If the latest time to start is bigger than the earliest time to finish
    # We shall consider that there should always be an hour of intersection at least.
    if from_max_date - to_min_date >= timedelta(hours=1):
        
        # In this case there is no intersection between the times.
        return []

    return [
        {
            'from': generate(from_max_date),
            'to': generate(to_min_date)
        }
    ]

@APP.post('/api/v1/calculate-best-dates')
def best_dates():
    requested_dates = request.get_json(force=True)
    print(requested_dates)

    response_dates = calculate_best_dates(requested_dates)

    if len(response_dates):
        return jsonify({
            'status': 'success',
            'message': 'Time retrieved successfuly',
            'data': response_dates
        })
    
    return jsonify({
        'status': 'error',
        'message': 'No overlaping time found',
        'data': None
    })

def main():
    APP.run(debug=True)

if __name__ == '__main__':
    main()

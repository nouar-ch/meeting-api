from flask import Flask, request, jsonify

APP = Flask(__name__)

def calculate_best_dates(dates):
    return []

@APP.post('/api/v1/calculate-best-dates')
def best_dates():
    requested_dates = request.get_json(force=True)
    print(requested_dates)

    response_dates = calculate_best_dates(requested_dates)

    return jsonify(response_dates)

def main():
    APP.run(debug=True)

if __name__ == '__main__':
    main()

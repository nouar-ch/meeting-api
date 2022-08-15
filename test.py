import unittest
from main import calculate_best_dates

class TestMeetingTime(unittest.TestCase):
    def runTest(self):
        dates = [{
            "from": "2022-05-02T09:00:00.0+08:00",
            "to": "2022-05-02T17:00:00.0+08:00",
            "CC": "SG"
        },
        {
            "from": "2022-05-02T09:00:00.0+01:00",
            "to": "2022-05-02T17:00:00.0+01:00",
            "CC": "NG"
        },
        {
            "from": "2022-05-02T09:00:00.0+05:30",
            "to": "2022-05-02T17:00:00.0+05:30",
            "CC": "IN"
        }]

        returned_dates = calculate_best_dates(dates)
        self.assertEqual(len(returned_dates), 0, 'List should be empty')

        returned_dates = calculate_best_dates(dates[-1:])
        self.assertEqual(len(returned_dates), 1, 'List should contain one date')


if __name__ == '__main__':
    unittest.main()

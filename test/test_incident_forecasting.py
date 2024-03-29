import unittest
from incident_data_extractor import IncidentDataExtractor

from num_incidents_per_day_forecasting import NumIncidentsPerDayForecasting


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.directory = "../wiki"
        self.extractor = IncidentDataExtractor(self.directory)
        self.incidents_data = self.extractor.load_incidents()

    def test_preprocess_data(self):
        data = [
            {'Date and Time': '2024-04-01 10:00:00', 'Incident ID': '1'},
            {'Date and Time': '2024-04-01 11:00:00', 'Incident ID': '2'},
            # Add more test data as needed
        ]
        forecasting = NumIncidentsPerDayForecasting(data)
        forecasting.preprocess_data()
        self.assertEqual(forecasting.data['incidents'].iloc[0], 2)  # Expecting 2 incidents on the same day

    def test_run_with_actual_data(self):
        forecasting = NumIncidentsPerDayForecasting(self.incidents_data)
        forecasting.run()

        # Since `run` doesn't return anything, we check if the model is trained
        self.assertIsNotNone(forecasting.model)

        # Optionally, verify the model's performance metric (e.g., RMSE) is within an expected range
        # This requires modifying the `run` method to store the RMSE as an instance variable
        # Example:
        # self.assertLess(forecasting.rmse, some_upper_limit)


if __name__ == '__main__':
    unittest.main()

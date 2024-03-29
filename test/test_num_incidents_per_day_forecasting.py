import unittest
from incident_data_extractor import IncidentDataExtractor

from num_incidents_per_day_forecasting import NumIncidentsPerDayForecasting


class TestNumIncidentsPerDayForecasting(unittest.TestCase):
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

    def test_model_performance(self):
        forecasting = NumIncidentsPerDayForecasting(self.incidents_data)
        forecasting.get_model_performance()

        # Since `run` doesn't return anything, we check if the model is trained
        self.assertIsNotNone(forecasting.model)

        # Verify the model's performance metric (e.g., RMSE) is within an expected range
        rmse_some_upper_limit = 0.25
        self.assertLess(forecasting.rmse, rmse_some_upper_limit)


if __name__ == '__main__':
    unittest.main()

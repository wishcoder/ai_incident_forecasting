import unittest
from incident_data_extractor import IncidentDataExtractor
from root_cause_forecasting import RootCauseForecasting


class TestRootCauseForecasting(unittest.TestCase):
    def setUp(self):
        self.directory = "../wiki"
        self.extractor = IncidentDataExtractor(self.directory)
        self.incidents_data = self.extractor.load_incidents()

        self.rc_forecasting = RootCauseForecasting()
        self.rc_forecasting.pre_init(self.incidents_data, unit_test=True)
        self.rc_forecasting.prepare_data()
        self.rc_forecasting.train()
        self.rc_forecasting.validate_model()

    def test_predict_app1(self):
        # For prediction, pass the title of the incident you want to predict the root cause for
        predicted_root_cause = self.rc_forecasting.predict("App 1")
        print(f"Predicted class for the root cause: {predicted_root_cause}")
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()

import unittest
from incident_data_extractor import IncidentDataExtractor

from component_affected_forecasting import ComponentAffectedForecasting


class TestComponentAffectedForecasting(unittest.TestCase):
    def setUp(self):
        self.directory = "../wiki"
        self.extractor = IncidentDataExtractor(self.directory)
        self.incidents_data = self.extractor.load_incidents()

    def test_affected_firewall_forcasting(self):
        forecasting = ComponentAffectedForecasting()
        forecasting.preprocess_data(self.incidents_data)
        forecasting.split_data()
        forecasting.train_model()
        forecasting.evaluate_model()

        new_titles = ["Email system down"]
        predictions = forecasting.predict_component_affected(new_titles)
        expected_component = 'Firewall-2'
        # Assert the predicted component is as expected
        self.assertEqual(predictions[0], expected_component,
                         "The predicted component does not match the expected output.")

        resolution_steps = forecasting.get_resolution_steps(predictions[0])
        print(f"Resolution Steps: {resolution_steps}")
        expected_resolution = "1. The routing issue was quickly detected by the network monitoring system. 2. Network engineers corrected the firewall configuration, restoring normal traffic distribution between App-3 and App-4 by 10:30."
        self.assertEqual(resolution_steps, expected_resolution,
                         "The predicted resolution does not match the expected output.")


if __name__ == '__main__':
    unittest.main()

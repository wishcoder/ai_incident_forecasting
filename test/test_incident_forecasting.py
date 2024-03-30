import unittest
from incident_data_extractor import IncidentDataExtractor
from incident_forecasting import IncidentForecasting


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.directory = "../wiki"
        self.extractor = IncidentDataExtractor(self.directory)
        self.incidents_data = self.extractor.load_incidents()
        self.forecasting = IncidentForecasting()
        self.forecasting.main_helper(unit_test=True)
        self.forecasting.train(self.incidents_data)
        self.forecasting.validate_model()

    def test_app1_changes(self):
        new_issue = ["App 1 changes"]
        predicted_components, predicted_resolutions = self.forecasting.predict(new_issue)
        self.assertNotEqual(predicted_components, None)
        self.assertNotEqual(predicted_resolutions, None)

        expected_components = ' '.join(['Router-1', 'Firewall-1', 'App-1'])
        expected_resolutions = ' '.join([
            '1. The issue was quickly identified by the development team through user reports and system monitoring. 2. The configuration changes were rolled back, restoring App-1 to its previous stable state by 15:30.'
        ])

        print(f"Predicted Components: {predicted_components}")
        print(f"Predicted Resolutions: {predicted_resolutions}")

        predicted_components = ' '.join(predicted_components)
        predicted_resolutions = ' '.join(predicted_resolutions)

        self.assertIn(predicted_components, expected_components)
        self.assertIn(predicted_resolutions, expected_resolutions)

    def test_app4_changes(self):
        new_issue = ["App 4 changes"]
        predicted_components, predicted_resolutions = self.forecasting.predict(new_issue)
        self.assertNotEqual(predicted_components, None)
        self.assertNotEqual(predicted_resolutions, None)

        expected_components = ' '.join(['Router-2', 'Firewall-2', 'App-4'])
        expected_resolutions = ' '.join([
            '1. The configuration changes were promptly reviewed by the IT support team. 2. Adjustments were made to restore access, with full functionality returning to all users by 17:45.',
            '1. The issue was identified through user feedback and system monitoring. 2. The original database connection settings were restored, improving performance back to optimal levels by 16:00.',
            '1. The issue was quickly identified by the development team through user reports and system monitoring. 2. The configuration changes were rolled back, restoring App-1 to its previous stable state by 15:30.'
        ])

        print(f"Predicted Components: {predicted_components}")
        print(f"Predicted Resolutions: {predicted_resolutions}")

        predicted_components = ' '.join(predicted_components)
        predicted_resolutions = ' '.join(predicted_resolutions)

        self.assertIn(predicted_components, expected_components)
        self.assertIn(predicted_resolutions, expected_resolutions)

    def test_convert_to_csv(self):
        csv_created = self.extractor.convert_to_csv(incidents_data=self.incidents_data, csv_file_name='../data/incident_data.csv')
        self.assertTrue(csv_created)


if __name__ == '__main__':
    unittest.main()

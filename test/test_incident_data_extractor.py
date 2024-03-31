# File: test_incident_data_extractor.py
import unittest
from incident_data_extractor import IncidentDataExtractor
from unittest.mock import patch, MagicMock


class TestIncidentDataExtractor(unittest.TestCase):
    def setUp(self):
        # Sample HTML content for two incident files
        self.sample_html_1 = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Incident Report: Incident 1</title>
            </head>
            <body>
                <article class="incident-report">
                    <h1 class="incident-title">Incident Report: Incident 1</h1>
                    <section class="incident-section incident-detail">
                        <h2>Incident Details</h2>
                        <p><span class="detail-label">Incident ID:</span><span class="detail-info">1</span></p>
                        <p><span class="detail-label">Title:</span><span class="detail-info">Title 1</span></p>
                        <p><span class="detail-label">Date and Time:</span><span class="detail-info">2024-04-01 10:00:00</span></p>
                        <p><span class="detail-label">Reported By:</span><span class="detail-info">Reporter 1</span></p>
                        <p><span class="detail-label">Component Affected:</span><span class="detail-info">Component 1</span></p>
                    </section>
                    <section class="incident-section incident-description">
                        <h2>Incident Description</h2>
                        <p>Detailed description of Incident 1.</p>
                    </section>
                    <section class="incident-section impact-analysis">
                        <h2>Impact Analysis</h2>
                        <p>Analysis of the Incident 1's impact.</p>
                    </section>
                    <section class="incident-section root-cause-analysis">
                        <h2>Root Cause</h2>
                        <p>Update applied an incompatible version of a critical security dependency</p>
                    </section>
                    <section class="incident-section resolution-steps">
                        <h2>Resolution Steps</h2>
                        <p>Step-by-step resolution of Incident 1.</p>
                        <p><span class="detail-label">Resolved By:</span><span class="detail-info">Resolver 1</span></p>
                        <p><span class="detail-label">Resolution Date and Time:</span><span class="detail-info">2024-04-01 12:00:00</span></p>
                    </section>
                    <section class="incident-section incident-status">
                        <h2>Status</h2>
                        <p>Current status of Incident 1.</p>
                    </section>
                    <section class="incident-section lessons-learned">
                        <h2>Lessons Learned</h2>
                        <p>Insights or lessons learned from Incident 1.</p>
                    </section>
                </article>
            </body>
            </html>
        """

        self.sample_html_2 = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Incident Report: Incident 2</title>
            </head>
            <body>
                <article class="incident-report">
                    <h1 class="incident-title">Incident Report: Incident 2</h1>
                    <section class="incident-section incident-detail">
                        <h2>Incident Details</h2>
                        <p><span class="detail-label">Incident ID:</span><span class="detail-info">2</span></p>
                        <p><span class="detail-label">Title:</span><span class="detail-info">Title 2</span></p>
                        <p><span class="detail-label">Date and Time:</span><span class="detail-info">2024-04-02 10:00:00</span></p>
                        <p><span class="detail-label">Reported By:</span><span class="detail-info">Reporter 2</span></p>
                        <p><span class="detail-label">Component Affected:</span><span class="detail-info">Component 2</span></p>
                    </section>
                    <section class="incident-section incident-description">
                        <h2>Incident Description</h2>
                        <p>Detailed description of Incident 2.</p>
                    </section>
                    <section class="incident-section impact-analysis">
                        <h2>Impact Analysis</h2>
                        <p>Analysis of the Incident 2's impact.</p>
                    </section>
                    <section class="incident-section root-cause-analysis">
                        <h2>Root Cause</h2>
                        <p>Update applied an incompatible version of a critical security dependency</p>
                    </section>
                    <section class="incident-section resolution-steps">
                        <h2>Resolution Steps</h2>
                        <p>Step-by-step resolution of Incident 2.</p>
                        <p><span class="detail-label">Resolved By:</span><span class="detail-info">Resolver 2</span></p>
                        <p><span class="detail-label">Resolution Date and Time:</span><span class="detail-info">2024-04-02 12:00:00</span></p>
                    </section>
                    <section class="incident-section incident-status">
                        <h2>Status</h2>
                        <p>Current status of Incident 2.</p>
                    </section>
                    <section class="incident-section lessons-learned">
                        <h2>Lessons Learned</h2>
                        <p>Insights or lessons learned from Incident 2.</p>
                    </section>
                </article>
            </body>
            </html>
        """

        # Patch listdir to return file names
        self.mock_listdir_patcher = patch('os.listdir')
        self.mock_listdir = self.mock_listdir_patcher.start()
        self.mock_listdir.return_value = ['incident1.html', 'incident2.html']

        # Patch 'builtins.open' to return sample HTML content
        self.mock_open_patcher = patch('builtins.open', side_effect=[
            MagicMock(read=MagicMock(return_value=self.sample_html_1)),
            MagicMock(read=MagicMock(return_value=self.sample_html_2))
        ])
        self.mock_open = self.mock_open_patcher.start()

        # Create an instance of the IncidentDataExtractor class with a dummy directory
        self.directory = "dummy_directory"
        self.extractor = IncidentDataExtractor(self.directory)

    def tearDown(self):
        # Stop patching
        self.mock_listdir_patcher.stop()
        self.mock_open_patcher.stop()

    def test_extract_incident_data(self):
        sample_html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Incident Report: Test Incident</title>
        </head>
        <body>
            <article class="incident-report">
                <h1 class="incident-title">Incident Report</h1>
                <section class="incident-section incident-detail">
                    <h2>Incident Details</h2>
                    <p><span class="detail-label">Incident ID:</span><span class="detail-info">ID12345</span></p>
                    <p><span class="detail-label">Title:</span><span class="detail-info">Test Incident</span></p>
                    <p><span class="detail-label">Date and Time:</span><span class="detail-info">2024-03-29 12:00</span></p>
                    <p><span class="detail-label">Reported By:</span><span class="detail-info">John Doe/IT Department</span></p>
                    <p><span class="detail-label">Component Affected:</span><span class="detail-info">Web Server</span></p>
                </section>
                <section class="incident-section incident-description">
                    <h2>Incident Description</h2>
                    <p>Detailed description of the incident.</p>
                </section>
                <section class="incident-section impact-analysis">
                    <h2>Impact Analysis</h2>
                    <p>Analysis of the incident's impact.</p>
                </section>
                <section class="incident-section root-cause-analysis">
                    <h2>Root Cause</h2>
                    <p>Update applied an incompatible version of a critical security dependency</p>
                </section>
                <section class="incident-section resolution-steps">
                    <h2>Resolution Steps</h2>
                    <p>Step-by-step resolution.</p>
                    <p><span class="detail-label">Resolved By:</span><span class="detail-info">Jane Smith/Resolution Team</span></p>
                    <p><span class="detail-label">Resolution Date and Time:</span><span class="detail-info">2024-03-30 08:00</span></p>
                </section>
                <section class="incident-section incident-status">
                    <h2>Status</h2>
                    <p>Resolved</p>
                </section>
                <section class="incident-section lessons-learned">
                    <h2>Lessons Learned</h2>
                    <p>Insights or lessons learned from the incident.</p>
                </section>
            </article>
        </body>
        </html>
        """
        # Extract data from the sample HTML
        extracted_data = self.extractor.extract_incident_data(sample_html)

        # Assert that the extracted data matches the expected values
        self.assertEqual(extracted_data['Incident ID'], 'ID12345')
        self.assertEqual(extracted_data['Title'], 'Test Incident')
        self.assertEqual(extracted_data['Date and Time'], '2024-03-29 12:00')
        self.assertEqual(extracted_data['Reported By'], 'John Doe/IT Department')
        self.assertEqual(extracted_data['Component Affected'], 'Web Server')
        self.assertEqual(extracted_data['Root Cause'], 'Update applied an incompatible version of a critical security dependency')
        self.assertEqual(extracted_data['Resolution Steps'], 'Step-by-step resolution.')
        self.assertEqual(extracted_data['Resolved By'], 'Jane Smith/Resolution Team')
        self.assertEqual(extracted_data['Resolution Date and Time'], '2024-03-30 08:00')
        self.assertEqual(extracted_data['Current Status'], 'Resolved')
        self.assertEqual(extracted_data['Lessons Learned'], 'Insights or lessons learned from the incident.')

    def test_load_incidents(self):
        # Call the load_incidents method
        incidents_data = self.extractor.load_incidents()

        # Assert that the correct number of incidents are loaded
        self.assertEqual(len(incidents_data), 2)

        # Asset the data for incident 1
        self.assertEqual(incidents_data[0]['Incident ID'], '1')
        self.assertEqual(incidents_data[0]['Title'], 'Title 1')
        self.assertEqual(incidents_data[0]['Date and Time'], '2024-04-01 10:00:00')
        self.assertEqual(incidents_data[0]['Reported By'], 'Reporter 1')
        self.assertEqual(incidents_data[0]['Component Affected'], 'Component 1')
        self.assertEqual(incidents_data[0]['Root Cause'],
                         'Update applied an incompatible version of a critical security dependency')
        self.assertEqual(incidents_data[0]['Resolution Steps'], 'Step-by-step resolution of Incident 1.')
        self.assertEqual(incidents_data[0]['Resolved By'], 'Resolver 1')
        self.assertEqual(incidents_data[0]['Resolution Date and Time'], '2024-04-01 12:00:00')
        self.assertEqual(incidents_data[0]['Current Status'], 'Current status of Incident 1.')
        self.assertEqual(incidents_data[0]['Lessons Learned'], 'Insights or lessons learned from Incident 1.')

        # Asset the data for incident 2
        self.assertEqual(incidents_data[1]['Incident ID'], '2')
        self.assertEqual(incidents_data[1]['Title'], 'Title 2')
        self.assertEqual(incidents_data[1]['Date and Time'], '2024-04-02 10:00:00')
        self.assertEqual(incidents_data[1]['Reported By'], 'Reporter 2')
        self.assertEqual(incidents_data[1]['Component Affected'], 'Component 2')
        self.assertEqual(incidents_data[1]['Root Cause'],
                         'Update applied an incompatible version of a critical security dependency')
        self.assertEqual(incidents_data[1]['Resolution Steps'], 'Step-by-step resolution of Incident 2.')
        self.assertEqual(incidents_data[1]['Resolved By'], 'Resolver 2')
        self.assertEqual(incidents_data[1]['Resolution Date and Time'], '2024-04-02 12:00:00')
        self.assertEqual(incidents_data[1]['Current Status'], 'Current status of Incident 2.')
        self.assertEqual(incidents_data[1]['Lessons Learned'], 'Insights or lessons learned from Incident 2.')


if __name__ == '__main__':
    unittest.main()

import unittest

from gcp_on_premise_summarization import IncidentSummarizer


class TestIncidentSummarizer(unittest.TestCase):
    def test_summarize_incident(self):
        project_id = "your-project-id"
        location = "your-location"
        endpoint_name = "your-gemini-endpoint"
        network = "projects/{}/locations/global/networks/{}".format(project_id, "your-vpc-network")

        summarizer = IncidentSummarizer(project_id, location, endpoint_name, network)

        incident = {
            'Incident ID': '1',
            'Title': 'Title 1',
            'Date and Time': '2024-04-01 10:00:00',
            'Reported By': 'Reporter 1',
            'Component Affected': 'Component 1',
            'Resolution Steps': 'Step-by-step resolution of Incident 1.',
            'Resolved By': 'Resolver 1',
            'Resolution Date and Time': '2024-04-01 12:00:00',
            'Current Status': 'Current status of Incident 1.',
            'Lessons Learned': 'Insights or lessons learned from Incident 1.'
        }

        summarized_incident = summarizer.summarize_incident(incident.copy())

        print(f"Incident with Summary: {summarized_incident}")

        self.assertNotEqual(summarized_incident, None)


if __name__ == '__main__':
    unittest.main()

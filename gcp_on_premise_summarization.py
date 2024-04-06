from google.cloud import aiplatform
from google.protobuf import json_format


class IncidentSummarizer:
    """
    Vertex AI Private Endpoints:
    Vertex AI offers the option to deploy models within a Virtual Private Cloud (VPC) environment.
    This allows you to access the model without any data leaving your network.
    You can configure a Private Endpoint for your Gemini model within your VPC.
    Refer to the [Vertex AI documentation on Private Endpoints]
    https://cloud.google.com/vertex-ai/docs/predictions/using-private-endpoints for details on setup.
    """

    def __init__(self, project_id: str, location: str, endpoint_name: str, network: str):
        self.project_id = project_id
        self.location = location
        self.endpoint_name = endpoint_name
        self.network = network
        self._client = aiplatform.EndpointServiceClient()

    # Function to summarize text using Vertex AI Private Endpoint
    def summarize_text(self, text: str) -> str:
        endpoint = self._client.endpoint_path(self.project_id, self.location, self.endpoint_name)
        instances = [{'text': text}]
        instances_json = json_format.MessageToJson(aiplatform.Instances(instances=instances))

        predictions = self._client.predict(endpoint=endpoint, instances=instances_json)
        return predictions.predictions[0]['document_sentiment']['summary']

    # Function to get text for summarization from incident data
    def get_text_from_incident(self, incident: dict) -> str:
        # Implement logic to combine and preprocess text from email body, chat transcript, title, and other relevant fields based on your data structure
        text = f"Title: {incident['Title']}\n"  # Add other relevant fields as needed
        return text

    # Function to summarize and update an incident
    def summarize_incident(self, incident: dict) -> dict:
        text_to_summarize = self.get_text_from_incident(incident)
        summary = self.summarize_text(text_to_summarize)
        incident['Summary'] = summary
        return incident
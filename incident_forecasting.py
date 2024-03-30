import re
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from transformers import DistilBertTokenizer, DistilBertModel

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk


class IncidentForecasting:
    def __init__(self):
        self.resolution_encoder = None
        self.component_encoder = None
        self.stop_words = None
        self.classifier_resolution = None
        self.classifier_component = None
        self.model = None
        self.tokenizer = None
        self.X_test = None
        self.y_test_comp = None
        self.y_test_res = None

    def main(self):
        self.main_helper(unit_test=False)

    def main_helper(self, unit_test):
        if unit_test is True:
            # Load the model and tokenizer from the local directory
            self.tokenizer = DistilBertTokenizer.from_pretrained('../distilbert-base-uncased')
            self.model = DistilBertModel.from_pretrained('../distilbert-base-uncased')

            # Load nltk data from local directory
            nltk.data.path.append('../nltk_data')
        else:
            self.tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
            self.model = DistilBertModel.from_pretrained('distilbert-base-uncased')
            # Load nltk data
            nltk.download('punkt')
            nltk.download('stopwords')

        self.classifier_component = RandomForestClassifier()
        self.classifier_resolution = RandomForestClassifier()
        self.stop_words = set(stopwords.words('english'))
        self.component_encoder = None
        self.resolution_encoder = None

    def preprocess_text(self, text):
        """Convert text to lowercase, remove punctuation, and filter out stop words."""
        text = text.lower()
        text = re.sub(r'\W', ' ', text)
        word_tokens = word_tokenize(text)
        filtered_text = [word for word in word_tokens if word not in self.stop_words]
        return ' '.join(filtered_text)

    def text_to_embedding(self, text):
        """Convert text to BERT embedding."""
        inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
        outputs = self.model(**inputs)
        return outputs.last_hidden_state[:, 0, :].detach().numpy()

    def prepare_data(self, dataset, label_field):
        """Preprocess dataset and prepare features and labels for a given label field."""
        df = pd.DataFrame(dataset)
        df['Preprocessed Title'] = df['Title'].apply(self.preprocess_text)
        X = np.vstack(df['Preprocessed Title'].apply(self.text_to_embedding))
        y = df[label_field]
        label_encoder = {label: idx for idx, label in enumerate(y.unique())}
        y_encoded = y.map(label_encoder)
        # random_state '42' itself comes from Douglas Adams' "The Hitchhiker's Guide to the Galaxy,"
        # where 42 is humorously presented as "the Answer to the Ultimate Question of Life, the Universe, and Everything."
        return train_test_split(X, y_encoded, test_size=0.2, random_state=42), label_encoder

    def train(self, dataset):
        """Train the model on the provided dataset for both components and resolutions."""
        # Train for Component Affected
        (X_train, X_test, y_train, y_test_comp), self.component_encoder = self.prepare_data(dataset, 'Component Affected')
        self.classifier_component.fit(X_train, y_train)
        y_pred = self.classifier_component.predict(X_test)
        print(f"Component Prediction Accuracy: {accuracy_score(y_test_comp, y_pred)}")

        # Train for Resolution Steps
        (X_train, X_test, y_train, y_test_res), self.resolution_encoder = self.prepare_data(dataset, 'Resolution Steps')
        self.classifier_resolution.fit(X_train, y_train)
        y_pred = self.classifier_resolution.predict(X_test)
        print(f"Resolution Prediction Accuracy: {accuracy_score(y_test_res, y_pred)}")

        # Store X_test, y_test_comp, and y_test_res for validation
        self.X_test = X_test
        self.y_test_comp = y_test_comp
        self.y_test_res = y_test_res

    def validate_model(self):
        """Validate the model using the test set and print out performance metrics."""
        # Component Affected
        y_pred_comp = self.classifier_component.predict(self.X_test)
        # Generate a list of all unique labels that might be predicted
        labels_comp = list(self.component_encoder.values())
        labels_names_comp = list(self.component_encoder.keys())
        print("Validation Results for 'Component Affected':")
        print(classification_report(self.y_test_comp, y_pred_comp, labels=labels_comp, target_names=labels_names_comp, zero_division=0))

        # Resolution Steps
        y_pred_res = self.classifier_resolution.predict(self.X_test)
        # Generate a list of all unique labels that might be predicted
        labels_res = list(self.resolution_encoder.values())
        labels_names_res = list(self.resolution_encoder.keys())
        print("Validation Results for 'Resolution Steps':")
        print(classification_report(self.y_test_res, y_pred_res, labels=labels_res, target_names=labels_names_res, zero_division=0))

    def validate_model_old(self):
        """Validate the model using the test set and print out performance metrics."""
        # Component Affected
        y_pred_comp = self.classifier_component.predict(self.X_test)
        print("Validation Results for 'Component Affected':")
        print(classification_report(self.y_test_comp, y_pred_comp, target_names=self.component_encoder.keys()))

        # Resolution Steps
        y_pred_res = self.classifier_resolution.predict(self.X_test)
        print("Validation Results for 'Resolution Steps':")
        print(classification_report(self.y_test_res, y_pred_res, target_names=self.resolution_encoder.keys()))

    def predict(self, titles):
        """Predict the 'Component Affected' and 'Resolution Steps' for new incident titles."""
        preprocessed_titles = [self.preprocess_text(title) for title in titles]
        embeddings = np.vstack([self.text_to_embedding(title) for title in preprocessed_titles])

        # Predict Component
        component_predictions = self.classifier_component.predict(embeddings)
        inverse_component_encoder = {v: k for k, v in self.component_encoder.items()}
        predicted_components = [inverse_component_encoder[pred] for pred in component_predictions]

        # Predict Resolution
        resolution_predictions = self.classifier_resolution.predict(embeddings)
        inverse_resolution_encoder = {v: k for k, v in self.resolution_encoder.items()}
        predicted_resolutions = [inverse_resolution_encoder[pred] for pred in resolution_predictions]

        return predicted_components, predicted_resolutions

    if __name__ == "__main__":
        main()

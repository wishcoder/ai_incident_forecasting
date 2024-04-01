import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import pandas as pd
import string
from sklearn.preprocessing import LabelEncoder


def preprocess_text(text):
    """
    Basic preprocessing can be expanded based on needs
    :param text:
    :return: string
    """
    # Convert text to lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Additional preprocessing steps can be added here if needed
    return text


def dataset_to_dataframe(dataset):
    """
    get DataFrame with the incident data
    :param dataset:
    :return: DataFrame
    """
    return pd.DataFrame(dataset)


class RootCauseForecasting:
    def __init__(self):
        self.dataset = None
        self.data_data_frame = None

        self.prepare_data_x = None
        self.prepare_data_y = None

        self.X_train = None
        self.y_train = None
        self.X_val = None
        self.y_val = None
        self.vectorizer = None
        self.model = None

        self.label_encoder = None

        self.index_to_root_cause = None
        self.unit_test = False

    def pre_init(self, dataset, unit_test):
        self.unit_test = unit_test
        self.dataset = dataset
        self.data_data_frame = dataset_to_dataframe(self.dataset)
        labels, uniques = pd.factorize(self.data_data_frame['Root Cause'])
        self.index_to_root_cause = dict(enumerate(uniques))
        self.vectorizer = TfidfVectorizer(ngram_range=(1, 3), stop_words='english')
        self.model = RandomForestClassifier()
        self.label_encoder = LabelEncoder()

    def prepare_data(self):
        # Assuming 'dataset' is a DataFrame with 'Title' and 'Root Cause' columns
        texts = [preprocess_text(text) for text in self.data_data_frame['Title']]
        self.prepare_data_x = self.vectorizer.fit_transform(texts)
        self.prepare_data_y = self.label_encoder.fit_transform(self.data_data_frame['Root Cause'])

    def train(self):
        self.X_train, self.X_val, self.y_train, self.y_val = train_test_split(self.prepare_data_x, self.prepare_data_y,
                                                                              test_size=0.2, random_state=42)
        self.model.fit(self.X_train, self.y_train)
        y_pred = self.model.predict(self.X_val)
        if self.unit_test is True:
            print(classification_report(self.y_val, y_pred, zero_division=0))

    def validate_model(self):
        y_pred = self.model.predict(self.X_val)
        accuracy = accuracy_score(self.y_val, y_pred)
        print(f"Accuracy: {accuracy * 100:.2f}%")

        # Specify the labels parameter to include only the labels present in y_val
        unique_labels = np.unique(np.concatenate((self.y_val, y_pred)))
        target_names = self.label_encoder.inverse_transform(unique_labels)
        if self.unit_test is True:
            print("\nClassification Report:\n",
                  classification_report(self.y_val, y_pred, labels=unique_labels, target_names=target_names,
                                        zero_division=0))

    def predict(self, text):
        processed_text = preprocess_text(text)
        prepare_data_x = self.vectorizer.transform([processed_text])
        prediction_idx = self.model.predict(prepare_data_x)[0]
        root_cause = self.label_encoder.inverse_transform([prediction_idx])[0]
        return root_cause

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder


def preprocess_text(text):
    """
    Basic preprocessing can be expanded based on needs.
    """
    # Convert text to lowercase
    text = text.lower()
    # Additional preprocessing steps can be added here if needed
    return text


class RootCauseForecasting:
    def __init__(self):
        # Initialize a Pipeline with TfidfVectorizer and RandomForestClassifier
        self.y_val = None
        self.y_train = None
        self.X_val = None
        self.X_train = None
        self.pipeline = Pipeline([
            ('tfidf', TfidfVectorizer(stop_words='english', ngram_range=(1, 3), max_df=0.9, min_df=2)),
            ('clf', RandomForestClassifier(random_state=42))
        ])
        self.label_encoder = LabelEncoder()

    def prepare_data(self, dataset):
        """
        Prepares the dataset for training or prediction.
        """
        df = pd.DataFrame(dataset)
        X = df['Title'].apply(preprocess_text)
        y = self.label_encoder.fit_transform(df['Root Cause'])
        return X, y

    def train(self, X, y):
        """
        Trains the model using the provided dataset.
        """
        # Splitting the dataset into training and validation sets
        self.X_train, self.X_val, self.y_train, self.y_val = train_test_split(X, y, test_size=0.2, random_state=42)
        self.pipeline.fit(self.X_train, self.y_train)

    def validate_model(self):
        """
        Validates the model using the validation set and prints out the classification report.
        """
        y_pred = self.pipeline.predict(self.X_val)

        # Identify the unique labels present in the true labels and predictions
        unique_labels = np.unique(np.concatenate((self.y_val, y_pred)))

        print("Accuracy:", accuracy_score(self.y_val, y_pred))
        print("Classification Report:")
        print(classification_report(self.y_val, y_pred, labels=unique_labels,
                                    target_names=self.label_encoder.inverse_transform(unique_labels), zero_division=0))

    def predict(self, text):
        """
        Predicts the root cause for a given issue title.
        """
        processed_text = preprocess_text(text)
        prediction_idx = self.pipeline.predict([processed_text])[0]
        root_cause = self.label_encoder.inverse_transform([prediction_idx])[0]
        return root_cause

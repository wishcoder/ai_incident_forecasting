import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report


class ComponentAffectedForecasting:
    def __init__(self):
        self.model = Pipeline([
            ('vectorizer', TfidfVectorizer()),
            ('classifier', LogisticRegression(max_iter=1000))
        ])
        self.dataframe = None  # To store the original DataFrame
        self.X_train, self.X_test, self.y_train, self.y_test = None, None, None, None

    def preprocess_data(self, data):
        """Converts input data into a DataFrame and preprocesses it."""
        self.dataframe = pd.DataFrame(data)
        # Here, implement any specific preprocessing steps you might need.
        # For example, handling missing values, encoding categorical variables, etc.

    def split_data(self, test_size=0.2, random_state=42):
        """Splits the data into training and testing sets."""
        if self.dataframe is not None:
            X = self.dataframe['Title']
            y = self.dataframe['Component Affected']
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=test_size,
                                                                                    random_state=random_state)
        else:
            raise ValueError("Data has not been preprocessed. Please call preprocess_data first.")

    def train_model(self):
        """Trains the model using the training data."""
        if self.X_train is not None and self.y_train is not None:
            self.model.fit(self.X_train, self.y_train)
        else:
            raise ValueError("Training data is not available. Please ensure data is split correctly.")

    def predict_component_affected(self, titles):
        """Predicts the component affected based on the title."""
        if self.model:
            return self.model.predict(titles)
        else:
            raise Exception("Model has not been trained yet.")

    def evaluate_model(self):
        """Evaluates the model's performance on the test set."""
        if self.X_test is not None and self.y_test is not None:
            predictions = self.model.predict(self.X_test)
            print(classification_report(self.y_test, predictions, zero_division=1))
        else:
            raise ValueError("Test data is not available. Please ensure data is split correctly.")

    def get_resolution_steps(self, component_predicted):
        """
        The method get_resolution_steps naively returns the 'Resolution Steps' of the
        most recent related incident. Depending on your application, you might want to implement a
        more sophisticated logic, possibly considering the similarity between incidents
        based on other features (e.g., using NLP techniques to find similar 'Titles' or 'Resolution Steps').
        This approach assumes that historical 'Resolution Steps' are a good basis for future incidents,
        which might not always be the case. Continuous monitoring and updating of the model and its data are essential.
        :param component_predicted:
        :return:
        """

        # Filter the dataframe for the predicted component
        filtered_df = self.dataframe[self.dataframe['Component Affected'] == component_predicted]
        # Sort by 'Date and Time' to find the most recent incident
        filtered_df = filtered_df.sort_values(by='Date and Time', ascending=False)
        if not filtered_df.empty:
            # Return the 'Resolution Steps' of the most recent incident
            return filtered_df.iloc[0]['Resolution Steps']
        else:
            return "No resolution steps found for the predicted component."

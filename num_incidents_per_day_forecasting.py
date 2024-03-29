import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import numpy as np


class NumIncidentsPerDayForecasting:
    """
    forecasting the number of incidents per day based on the date
    """
    def __init__(self, data):
        self.data = pd.DataFrame(data)
        self.model = None
        self.rmse = None

    def preprocess_data(self):
        """Converts date and time to numerical features and prepares target variable."""
        self.data['Date and Time'] = pd.to_datetime(self.data['Date and Time'])
        self.data['day_of_year'] = self.data['Date and Time'].dt.dayofyear

        # Assuming the target is to predict the number of incidents per day
        self.data = self.data.groupby('day_of_year').size().reset_index(name='incidents')

    def split_data(self):
        """Splits data into training and testing sets."""
        X = self.data[['day_of_year']]
        y = self.data['incidents']
        return train_test_split(X, y, test_size=0.2, random_state=42)

    def train_model(self, X_train, y_train):
        """Trains the forecasting model."""
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.model.fit(X_train, y_train)

    def predict(self, X):
        """Makes predictions using the trained model."""
        return self.model.predict(X)

    def evaluate_model(self, X_test, y_test):
        """Evaluates the model's performance."""
        predictions = self.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        return np.sqrt(mse)

    def get_model_performance(self):
        """Executes the forecasting process."""
        self.preprocess_data()
        X_train, X_test, y_train, y_test = self.split_data()
        self.train_model(X_train, y_train)
        self.rmse = self.evaluate_model(X_test, y_test)
        print(f"Model RMSE: {self.rmse}")


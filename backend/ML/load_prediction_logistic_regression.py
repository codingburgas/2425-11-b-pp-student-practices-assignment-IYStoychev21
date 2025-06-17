import pandas as pd
import numpy as np

class LoanPrediction:
    def __init__(self, csv_path = '', train_size=0.8, learning_rate=0.01, epochs=1000):
        if csv_path == '':
            return

        self.train_size = train_size
        self.learning_rate = learning_rate
        self.epochs = epochs

        self.df = pd.read_csv(csv_path)
        self.df.columns = self.df.columns.str.strip()

        self.df['education'] = self.df['education'].str.strip().str.lower().map({'graduate': 1, 'not graduate': 0})
        self.df['self_employed'] = self.df['self_employed'].str.strip().str.lower().map({'yes': 1, 'no': 0})
        self.df['loan_status'] = self.df['loan_status'].str.strip().str.lower().map({'approved': 1, 'rejected': 0})

        self.X = self.df.drop(columns=['loan_id', 'loan_status']).values
        self.y = self.df['loan_status'].values.reshape(-1, 1)

        self.X = (self.X - np.mean(self.X, axis=0)) / np.std(self.X, axis=0)

        self._train_test_split()

        self.weights = np.zeros((self.X_train.shape[1], 1))
        self.bias = 0

    def _train_test_split(self):
        indices = np.arange(self.X.shape[0])
        np.random.shuffle(indices)
        split_index = int(self.train_size * self.X.shape[0])
        train_idx, test_idx = indices[:split_index], indices[split_index:]
        self.X_train, self.X_test = self.X[train_idx], self.X[test_idx]
        self.y_train, self.y_test = self.y[train_idx], self.y[test_idx]

    def _sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def train(self):
        for _ in range(self.epochs):
            z = np.dot(self.X_train, self.weights) + self.bias
            predictions = self._sigmoid(z)
            error = predictions - self.y_train
            dw = np.dot(self.X_train.T, error) / len(self.y_train)
            db = np.sum(error) / len(self.y_train)
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

    def predict(self, X_input):
        X_input = (X_input - np.mean(self.X, axis=0)) / np.std(self.X, axis=0)
        z = np.dot(X_input, self.weights) + self.bias
        return (self._sigmoid(z) >= 0.5).astype(int)

    def get_accuracy(self):
        predictions = self.predict(self.X_test)
        return np.mean(predictions == self.y_test)

    def get_weights(self):
        return self.weights

    def get_bias(self):
        return self.bias

    def set_weights(self, w):
        self.weights = w

    def set_bias(self, b):
        self.bias = b

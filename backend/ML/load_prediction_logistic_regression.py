import pandas as pd
import numpy as np

class LoanPrediction:
    """
    Logistic Regression model for loan approval prediction.
    
    This class implements a logistic regression classifier specifically designed
    for loan approval prediction. It handles data preprocessing, model training,
    prediction, and performance evaluation.
    
    Attributes:
        train_size (float): Proportion of data to use for training
        learning_rate (float): Learning rate for gradient descent
        epochs (int): Number of training iterations
        df (DataFrame): Original dataset
        X (ndarray): Feature matrix (normalized)
        y (ndarray): Target labels
        X_mean (ndarray): Feature means for normalization
        X_std (ndarray): Feature standard deviations for normalization
        X_train, X_test (ndarray): Training and testing feature sets
        y_train, y_test (ndarray): Training and testing labels
        weights (ndarray): Model weights
        bias (float): Model bias term
    """
    def __init__(self, csv_path = '', train_size=0.8, learning_rate=0.01, epochs=1000):
        """
        Initialize the LoanPrediction model.
        
        Args:
            csv_path (str): Path to the CSV file containing training data.
                           If empty, creates an empty model for loading existing parameters.
            train_size (float): Proportion of data to use for training (default: 0.8)
            learning_rate (float): Learning rate for gradient descent (default: 0.01)
            epochs (int): Number of training iterations (default: 1000)
        """
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
        self.X_mean = np.mean(self.X, axis=0)
        self.X_std = np.std(self.X, axis=0)

        self._train_test_split()

        self.weights = np.zeros((self.X_train.shape[1], 1))
        self.bias = 0

    def _train_test_split(self):
        """
        Split the dataset into training and testing sets.
        
        Randomly shuffles the data and splits it according to the train_size parameter.
        Sets X_train, X_test, y_train, y_test attributes.
        """
        indices = np.arange(self.X.shape[0])
        np.random.shuffle(indices)
        split_index = int(self.train_size * self.X.shape[0])
        train_idx, test_idx = indices[:split_index], indices[split_index:]
        self.X_train, self.X_test = self.X[train_idx], self.X[test_idx]
        self.y_train, self.y_test = self.y[train_idx], self.y[test_idx]

    def _sigmoid(self, z):
        """
        Sigmoid activation function.
        
        Args:
            z (ndarray): Input values
            
        Returns:
            ndarray: Sigmoid output values between 0 and 1
        """
        return 1 / (1 + np.exp(-z))

    def train(self):
        """
        Train the logistic regression model using gradient descent.
        
        Performs gradient descent optimization for the specified number of epochs,
        updating weights and bias to minimize the logistic loss function.
        """
        for _ in range(self.epochs):
            z = np.dot(self.X_train, self.weights) + self.bias
            predictions = self._sigmoid(z)
            error = predictions - self.y_train
            dw = np.dot(self.X_train.T, error) / len(self.y_train)
            db = np.sum(error) / len(self.y_train)
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

    def predict(self, X_input):
        """
        Make predictions on new input data.
        
        Args:
            X_input (ndarray): Input features for prediction
            
        Returns:
            ndarray: Binary predictions (0 for rejected, 1 for approved)
        """
        X_input = (X_input - self.X_mean) / self.X_std
        z = np.dot(X_input, self.weights) + self.bias
        return (self._sigmoid(z) >= 0.5).astype(int)

    def get_accuracy(self):
        """
        Calculate model accuracy on test set.
        
        Returns:
            float: Accuracy score between 0 and 1
        """
        predictions = self.predict(self.X_test)
        return np.mean(predictions == self.y_test)

    def get_precision(self):
        """
        Calculate model precision on test set.
        
        Returns:
            float: Precision score (True Positives / (True Positives + False Positives))
        """
        y_pred = self.predict(self.X_test).astype(int)
        y_true = self.y_test.astype(int)
        tp = np.sum((y_pred == 1) & (y_true == 1))
        fp = np.sum((y_pred == 1) & (y_true == 0))
        return tp / (tp + fp + 1e-8)

    def get_recall(self):
        """
        Calculate model recall on test set.
        
        Returns:
            float: Recall score (True Positives / (True Positives + False Negatives))
        """
        y_pred = self.predict(self.X_test).astype(int)
        y_true = self.y_test.astype(int)
        tp = np.sum((y_pred == 1) & (y_true == 1))
        fn = np.sum((y_pred == 0) & (y_true == 1))
        return tp / (tp + fn + 1e-8)

    def get_f1_score(self):
        """
        Calculate model F1-score on test set.
        
        Returns:
            float: F1-score (harmonic mean of precision and recall)
        """
        p = self.get_precision()
        r = self.get_recall()
        return 2 * p * r / (p + r + 1e-8)

    def get_confusion_matrix(self):
        """
        Calculate confusion matrix on test set.
        
        Returns:
            ndarray: 2x2 confusion matrix with format:
                     [[TN, FP],
                      [FN, TP]]
        """
        y_pred = self.predict(self.X_test).astype(int)
        y_true = self.y_test.astype(int)
        tp = np.sum((y_pred == 1) & (y_true == 1))
        tn = np.sum((y_pred == 0) & (y_true == 0))
        fp = np.sum((y_pred == 1) & (y_true == 0))
        fn = np.sum((y_pred == 0) & (y_true == 1))
        return np.array([[tn, fp], [fn, tp]])

    def get_weights(self):
        """
        Get the trained model weights.
        
        Returns:
            ndarray: Model weights
        """
        return self.weights

    def get_bias(self):
        """
        Get the trained model bias.
        
        Returns:
            float: Model bias term
        """
        return self.bias

    def set_weights(self, w):
        """
        Set the model weights.
        
        Args:
            w (ndarray): Weights to set
        """
        self.weights = w

    def set_bias(self, b):
        """
        Set the model bias.
        
        Args:
            b (float): Bias value to set
        """
        self.bias = b

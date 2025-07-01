from pydantic import BaseModel

class HyperParamsOut(BaseModel):
    """
    Schema for machine learning hyperparameters output.
    
    Attributes:
        id (int): Hyperparameters record's unique identifier
        epochs (int): Number of training epochs
        learning_rate (float): Learning rate used for training
    """
    id: int
    epochs: int
    learning_rate: float

class ParamsOut(BaseModel):
    """
    Schema for trained model parameters output.
    
    Contains the actual trained model weights and normalization parameters.
    
    Attributes:
        id (int): Parameters record's unique identifier
        weights (list[list]): Model weights as nested list
        bias (float): Model bias value
        x_mean (list[float]): Feature mean values for normalization
        x_std (list[float]): Feature standard deviation values for normalization
    """
    id: int
    weights: list[list]
    bias: float
    x_mean: list[float]
    x_std: list[float]

class TestTrainSplitOut(BaseModel):
    """
    Schema for train/test split configuration output.
    
    Attributes:
        id (int): Split configuration record's unique identifier
        testing (float): Proportion of data used for testing
        training (float): Proportion of data used for training
    """
    id: int
    testing: float
    training: float

class ModelMetricsOut(BaseModel):
    """
    Schema for model performance metrics output.
    
    Contains evaluation metrics calculated on the test set.
    
    Attributes:
        id (int): Metrics record's unique identifier
        accuracy (float): Model accuracy score
        precision (float): Model precision score
        f1_score (float): Model F1-score
        recall (float): Model recall score
        confusion_matrix (list[list]): Confusion matrix as nested list
    """
    id: int
    accuracy: float
    precision: float
    f1_score: float
    recall: float
    confusion_matrix: list[list]

class ModelOut(BaseModel):
    """
    Schema for complete model information output.
    
    Aggregates all model-related information including hyperparameters,
    trained parameters, train/test split configuration, and performance metrics.
    
    Attributes:
        id (int): Model record's unique identifier
        hyper_params (HyperParamsOut): Hyperparameters used for training
        test_train_split (TestTrainSplitOut): Train/test split configuration
        params (ParamsOut): Trained model parameters
        model_metrics (ModelMetricsOut): Model performance metrics
    """
    id: int
    hyper_params: HyperParamsOut
    test_train_split: TestTrainSplitOut
    params: ParamsOut
    model_metrics: ModelMetricsOut

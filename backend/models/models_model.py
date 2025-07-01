from tortoise import fields, models
from tortoise.fields.base import CASCADE

class HyperParams(models.Model):
    """
    HyperParams model for storing machine learning hyperparameters.
    
    Attributes:
        id (int): Primary key, auto-generated hyperparameter ID
        epochs (int): Number of training epochs (default: 0)
        learning_rate (float): Learning rate for training (default: 0.001)
        
    Related:
        models: One-to-many relationship with Models
    """
    id = fields.IntField(pk=True)
    epochs = fields.IntField(default=0.0)
    learning_rate = fields.FloatField(default=0.001)

    class Meta:
        table = "hyper_params"


class TestTrainSplit(models.Model):
    """
    TestTrainSplit model for storing train/test data split configuration.
    
    Attributes:
        id (int): Primary key, auto-generated split ID
        testing (float): Proportion of data used for testing (default: 0.2)
        training (float): Proportion of data used for training (default: 0.8)
        
    Related:
        models: One-to-many relationship with Models
    """
    id = fields.IntField(pk=True)
    testing = fields.FloatField(default=0.2)
    training = fields.FloatField(default=0.8)

    class Meta:
        table = "test_train_split"

class Params(models.Model):
    """
    Params model for storing trained model parameters.
    
    Attributes:
        id (int): Primary key, auto-generated parameter ID
        weights (JSON): Model weights as JSON array (default: empty list)
        bias (float): Model bias value (default: 0.0)
        x_mean (JSON): Feature mean values for normalization (default: empty list)
        x_std (JSON): Feature standard deviation values for normalization (default: empty list)
        
    Related:
        models: One-to-many relationship with Models
    """
    id = fields.IntField(pk=True)
    weights = fields.JSONField(default=list[list])
    bias = fields.FloatField(default=0.0)
    x_mean = fields.JSONField(default=list)
    x_std = fields.JSONField(default=list)

    class Meta:
        table = "params"

class ModelMetrics(models.Model):
    """
    ModelMetrics model for storing model performance metrics.
    
    Attributes:
        id (int): Primary key, auto-generated metrics ID
        accuracy (float): Model accuracy score (default: 0.0)
        precision (float): Model precision score (default: 0.0)
        recall (float): Model recall score (default: 0.0)
        f1_score (float): Model F1-score (default: 0.0)
        confusion_matrix (JSON): Confusion matrix as JSON array (default: empty list)
        
    Related:
        models: One-to-many relationship with Models
    """
    id = fields.IntField(pk=True)
    accuracy = fields.FloatField(default=0.0)
    precision = fields.FloatField(default=0.0)
    recall = fields.FloatField(default=0.0)
    f1_score = fields.FloatField(default=0.0)
    confusion_matrix = fields.JSONField(default=list[list])

    class Meta:
        table = "model_metrics"


class Models(models.Model):
    """
    Models model representing a complete ML model with all related components.
    
    This model links together all the components of a trained machine learning model
    including hyperparameters, training parameters, train/test split configuration,
    and performance metrics.
    
    Attributes:
        id (int): Primary key, auto-generated model ID
        hyper_params (HyperParams): Foreign key to hyperparameters used for training
        test_train_split (TestTrainSplit): Foreign key to train/test split configuration
        params (Params): Foreign key to trained model parameters
        model_metrics (ModelMetrics): Foreign key to model performance metrics
    """
    id = fields.IntField(pk=True)
    hyper_params = fields.ForeignKeyField(
            "models.HyperParams",
            related_name="models",
            on_delete=CASCADE,
        )
    test_train_split = fields.ForeignKeyField(
            "models.TestTrainSplit",
            related_name="models",
            on_delete=CASCADE,
        )
    params = fields.ForeignKeyField(
            "models.Params",
            related_name="models",
            on_delete=CASCADE,
        )
    model_metrics = fields.ForeignKeyField(
            "models.ModelMetrics",
            related_name="models",
            on_delete=CASCADE,
        )

    class Meta:
        table = "models"

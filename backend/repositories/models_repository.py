from models import models_model
import json

async def get_hyper_params():
    """
    Retrieve the machine learning model hyperparameters.
    
    Returns:
        HyperParams: Object containing epochs and learning rate configuration
    """
    return await models_model.HyperParams.get(id=1)

async def get_params():
    """
    Retrieve the trained model parameters.
    
    Returns:
        Params: Object containing model weights, bias, and normalization parameters
    """
    return await models_model.Params.get(id=1)

async def get_test_train_split():
    """
    Retrieve the train/test split configuration.
    
    Returns:
        TestTrainSplit: Object containing training and testing data split ratios
    """
    return await models_model.TestTrainSplit.get(id=1)

async def get_model():
    """
    Retrieve the complete model information with all related data.
    
    Returns:
        Models: Complete model object with hyperparameters, parameters,
                train/test split, and performance metrics
    """
    return await models_model.Models.get(id=1).select_related("hyper_params", "params", "test_train_split", "model_metrics")

async def set_params(weights, bias, x_mean, x_std):
    """
    Store trained model parameters in the database.
    
    Args:
        weights: Model weights as numpy array
        bias (float): Model bias value
        x_mean (list): Feature mean values for normalization
        x_std (list): Feature standard deviation values for normalization
        
    Returns:
        Params: The created parameters object
    """
    params = await models_model.Params.create(weights = json.dumps(weights.tolist()), bias = bias, x_mean = x_mean, x_std = x_std)
    return params

async def get_model_metrics():
    """
    Retrieve the model performance metrics.
    
    Returns:
        ModelMetrics: Object containing accuracy, precision, recall, F1-score, and confusion matrix
    """
    return await models_model.ModelMetrics.get(id=1)

async def set_model_metrics(accuracy, precision, f1_score, recall, confusion_matrix):
    """
    Store model performance metrics in the database.
    
    Args:
        accuracy (float): Model accuracy score
        precision (float): Model precision score
        f1_score (float): Model F1-score
        recall (float): Model recall score
        confusion_matrix: Confusion matrix as numpy array
        
    Returns:
        ModelMetrics: The created model metrics object
    """
    return await models_model.ModelMetrics.create(accuracy=accuracy, precision=precision, f1_score=f1_score, recall=recall, confusion_matrix=json.dumps(confusion_matrix.tolist()))

async def add_model():
    """
    Create a complete model record linking all model components.
    
    This function creates a Models record that links together the hyperparameters,
    trained parameters, train/test split configuration, and performance metrics.
    
    Returns:
        Models: The created complete model object
    """
    hp = await get_hyper_params()
    p = await get_params()
    train_test = await get_test_train_split()
    mm = await get_model_metrics()
    model = await models_model.Models.create(model_metrics=mm, hyper_params=hp, params=p, test_train_split=train_test)
    return model

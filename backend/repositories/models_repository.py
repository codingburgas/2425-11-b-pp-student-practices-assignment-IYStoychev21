from models import models_model
import json

async def get_hyper_params():
    return await models_model.HyperParams.get(id=1)

async def get_params():
    return await models_model.Params.get(id=1)

async def get_test_train_split():
    return await models_model.TestTrainSplit.get(id=1)

async def get_model():
    return await models_model.Models.get(id=1).select_related("hyper_params", "params", "test_train_split", "model_metrics")

async def set_params(weights, bias, x_mean, x_std):
    params = await models_model.Params.create(weights = json.dumps(weights.tolist()), bias = bias, x_mean = x_mean, x_std = x_std)
    return params

async def get_model_metrics():
    return await models_model.ModelMetrics.get(id=1)

async def set_model_metrics(accuracy, precision, f1_score, recall, confusion_matrix):
    return await models_model.ModelMetrics.create(accuracy=accuracy, precision=precision, f1_score=f1_score, recall=recall, confusion_matrix=json.dumps(confusion_matrix.tolist()))

async def add_model():
    hp = await get_hyper_params()
    p = await get_params()
    train_test = await get_test_train_split()
    mm = await get_model_metrics()
    model = await models_model.Models.create(model_metrics=mm, hyper_params=hp, params=p, test_train_split=train_test)
    return model

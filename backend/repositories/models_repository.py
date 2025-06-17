from backend.models import models_model
import json

async def get_hyper_params():
    return await models_model.HyperParams.get(id=1)

async def get_params():
    return await models_model.Params.get(id=1)

async def get_test_train_split():
    return await models_model.TestTrainSplit.get(id=1)

async def get_model():
    return await models_model.Models.get(id=1).select_related("hyper_params", "params", "test_train_split")

async def set_params(weights, bias):
    params = await models_model.Params.create(weights = json.dumps(weights.tolist()), bias = bias)
    return params

async def add_model(accuracy: float):
    hp = await get_hyper_params()
    p = await get_params()
    train_test = await get_test_train_split()
    model = await models_model.Models.create(accuracy=accuracy, hyper_params=hp, params=p, test_train_split=train_test)
    return model

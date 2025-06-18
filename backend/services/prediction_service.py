from fastapi.exceptions import HTTPException
from backend.repositories import models_repository, prediction_repository, user_repository
from backend.core.security import create_access_token
from backend.schemas import prediction_schema
from backend.ML import load_prediction_logistic_regression
import numpy as np

async def make_prediction(user_id: int, prediction_data: prediction_schema.PredictionCreate):
    user = await user_repository.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User does not exist")


    hyper_params = await models_repository.get_hyper_params()
    test_train_split = await models_repository.get_test_train_split()
    prediction_input = await prediction_repository.insert_prediction_input(prediction_data)
    params = await models_repository.get_params()

    model = load_prediction_logistic_regression.LoanPrediction()
    model.X_mean = params.x_mean
    model.X_std = params.x_std
    model.set_bias(params.bias)
    model.set_weights(params.weights)

    X_sample = [
        prediction_data.no_of_dependents,
        prediction_data.education,
        prediction_data.self_employed,
        prediction_data.income_amount,
        prediction_data.loan_amont,
        prediction_data.loan_amont_term,
        prediction_data.cibil_score,
        prediction_data.residential_assets_value,
        prediction_data.commercial_assets_value,
        prediction_data.luxury_assets_value,
        prediction_data.bank_asset_value
    ]

    X_sample = np.array(X_sample).reshape(1, -1)
    prediction = model.predict(X_sample)
    prediction_out = await prediction_repository.insert_prediction(prediction[0][0], user, prediction_input)
    return prediction_out

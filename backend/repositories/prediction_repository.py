from backend.models import predictions_model
from backend.schemas import prediction_schema
from backend.models import user_model, predictions_model

async def insert_prediction_input(prediction_data: prediction_schema.PredictionCreate):
    return await predictions_model.PredictionInputs.create(
        no_of_dependents = prediction_data.no_of_dependents,
        education = prediction_data.education,
        self_employed = prediction_data.self_employed,
        income_amount = prediction_data.income_amount,
        loan_amont = prediction_data.loan_amont,
        loan_amont_term = prediction_data.loan_amont_term,
        cibil_score = prediction_data.cibil_score,
        residential_assets_value = prediction_data.residential_assets_value,
        commercial_assets_value = prediction_data.commercial_assets_value,
        luxury_assets_value = prediction_data.luxury_assets_value,
        bank_asset_value = prediction_data.bank_asset_value
    )

async def insert_prediction(prediction: bool, user: user_model.User, prediction_inputs: predictions_model.PredictionInputs, title: str):
    return await predictions_model.Predictions.create(prediction=prediction, user=user, prediction_inputs=prediction_inputs, title=title)

async def get_predictions(user: user_model.User):
    return await predictions_model.Predictions.all().filter(user=user).select_related("user__role", "prediction_inputs")

async def delete_prediction(prediction_id: int):
    return await predictions_model.Predictions.filter(id=prediction_id).delete()

async def get_prediction(prediction_id: int):
    return await predictions_model.Predictions.get(id=prediction_id).select_related("user__role", "prediction_inputs")

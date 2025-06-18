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

async def insert_prediction(prediction: bool, user: user_model.User, prediction_inputs: predictions_model):
    return await predictions_model.Predictions.create(prediction=prediction, user=user, prediction_inputs=prediction_inputs)

from models import predictions_model
from schemas import prediction_schema
from models import user_model, predictions_model

async def insert_prediction_input(prediction_data: prediction_schema.PredictionCreate):
    """
    Store prediction input data in the database.
    
    Args:
        prediction_data (prediction_schema.PredictionCreate): Input data for loan prediction
                                                              including financial and personal information
    
    Returns:
        PredictionInputs: The created prediction input record
    """
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
    """
    Store a prediction result in the database.
    
    Args:
        prediction (bool): The prediction result (True for approved, False for rejected)
        user (user_model.User): The user who made the prediction request
        prediction_inputs (predictions_model.PredictionInputs): The input data used for prediction
        title (str): A descriptive title for the prediction
    
    Returns:
        Predictions: The created prediction record
    """
    return await predictions_model.Predictions.create(prediction=prediction, user=user, prediction_inputs=prediction_inputs, title=title)

async def get_predictions(user: user_model.User):
    """
    Retrieve all predictions for a specific user.
    
    Args:
        user (user_model.User): The user whose predictions to retrieve
    
    Returns:
        list[Predictions]: List of prediction records with related user and input data
    """
    return await predictions_model.Predictions.all().filter(user=user).select_related("user__role", "prediction_inputs")

async def delete_prediction(prediction_id: int):
    """
    Delete a prediction record by its ID.
    
    Args:
        prediction_id (int): The ID of the prediction to delete
    
    Returns:
        int: Number of deleted records
    """
    return await predictions_model.Predictions.filter(id=prediction_id).delete()

async def get_prediction(prediction_id: int):
    """
    Retrieve a specific prediction by its ID.
    
    Args:
        prediction_id (int): The ID of the prediction to retrieve
    
    Returns:
        Predictions: The prediction record with related user and input data
    """
    return await predictions_model.Predictions.get(id=prediction_id).select_related("user__role", "prediction_inputs")

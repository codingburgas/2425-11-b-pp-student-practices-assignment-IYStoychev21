from fastapi.exceptions import HTTPException
from repositories import models_repository, prediction_repository, user_repository
from schemas import prediction_schema
from ML import load_prediction_logistic_regression
import numpy as np

async def make_prediction(user_id: int, prediction_data: prediction_schema.PredictionCreate):
    """
    Create a new loan approval prediction using the trained ML model.
    
    Args:
        user_id (int): The ID of the user making the prediction request
        prediction_data (prediction_schema.PredictionCreate): Input data for the prediction
                                                              including financial and personal information
    
    Returns:
        Prediction: The prediction result with input data and approval/rejection decision
        
    Raises:
        HTTPException: 404 if user does not exist
    """
    user = await user_repository.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User does not exist")

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
    prediction_out = await prediction_repository.insert_prediction(prediction[0][0], user, prediction_input, prediction_data.title)
    return prediction_out

async def get_predictions(user_id: int, user_to_retrieve_id: int):
    """
    Get all predictions for a specific user.
    
    Args:
        user_id (int): The ID of the user making the request
        user_to_retrieve_id (int): The ID of the user whose predictions to retrieve
        
    Returns:
        list[Prediction]: List of predictions with input data and results
        
    Raises:
        HTTPException: 404 if either user does not exist
    """
    user = await user_repository.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User does not exist")

    user_to_retrieve = await user_repository.get_user_by_id(user_to_retrieve_id)
    if not user_to_retrieve:
        raise HTTPException(status_code=404, detail="User does not exist")

    predictions = await prediction_repository.get_predictions(user_to_retrieve)
    return predictions

async def delete_prediction(user_id: int, prediction_id: int):
    """
    Delete a specific prediction record.
    
    Args:
        user_id (int): The ID of the user making the request
        prediction_id (int): The ID of the prediction to delete
        
    Returns:
        Prediction: The deleted prediction object
        
    Raises:
        HTTPException: 404 if user or prediction does not exist
    """
    user = await user_repository.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User does not exist")

    prediction = await prediction_repository.get_prediction(prediction_id)
    if not prediction:
           raise HTTPException(status_code=404, detail="Prediction does not exist")

    await prediction_repository.delete_prediction(prediction.id)
    return prediction

async def get_prediction(user_id: int, prediction_id: int):
    """
    Get a specific prediction by its ID.
    
    Args:
        user_id (int): The ID of the user making the request
        prediction_id (int): The ID of the prediction to retrieve
        
    Returns:
        Prediction: The prediction object with input data and result
        
    Raises:
        HTTPException: 404 if user or prediction does not exist
    """
    user = await user_repository.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User does not exist")

    prediction = await prediction_repository.get_prediction(prediction_id)
    if not prediction:
            raise HTTPException(status_code=404, detail="Prediction does not exist")

    return prediction

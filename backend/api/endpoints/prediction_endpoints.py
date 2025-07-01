from fastapi import APIRouter, HTTPException, Depends, Request
from schemas import prediction_schema
from services import prediction_service
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

router = APIRouter()
security = HTTPBearer()

@router.post("/predict", response_model=prediction_schema.PredictionOut)
async def predict(request: Request, prediction_data: prediction_schema.PredictionCreate, credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Create a new loan approval prediction using the trained ML model.
    
    Args:
        request (Request): FastAPI request object containing user_id in state
        prediction_data (prediction_schema.PredictionCreate): Input data for loan prediction
                                                              including financial and personal information
        credentials: JWT bearer token for authentication
    
    Returns:
        prediction_schema.PredictionOut: Prediction result with input data and approval/rejection decision
        
    Raises:
        HTTPException: 404 if user does not exist
    """
    user_id = request.state.user_id
    try:
        prediction = await prediction_service.make_prediction(user_id, prediction_data)
        return prediction
    except HTTPException as e:
        raise e

@router.get("/get/all", response_model=list[prediction_schema.PredictionOut])
async def get_current_user_predictions(request: Request, credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Get all predictions for the current authenticated user.
    
    Args:
        request (Request): FastAPI request object containing user_id in state
        credentials: JWT bearer token for authentication
    
    Returns:
        list[prediction_schema.PredictionOut]: List of user's predictions with input data and results
        
    Raises:
        HTTPException: 404 if user does not exist
    """
    user_id = request.state.user_id
    try:
        predictions = await prediction_service.get_predictions(user_id, user_id)
        return predictions
    except HTTPException as e:
        raise e

@router.get("/get/all/{id}", response_model=list[prediction_schema.PredictionOut])
async def get_user_predictions(request: Request, id: int, credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Get all predictions for a specific user by their ID.
    
    Args:
        request (Request): FastAPI request object containing user_id in state
        id (int): ID of the user whose predictions to retrieve
        credentials: JWT bearer token for authentication
    
    Returns:
        list[prediction_schema.PredictionOut]: List of the specified user's predictions
        
    Raises:
        HTTPException: 404 if either user does not exist
    """
    user_id = request.state.user_id
    try:
        predictions = await prediction_service.get_predictions(user_id, id)
        return predictions
    except HTTPException as e:
        raise e

@router.get("/get/{id}", response_model=prediction_schema.PredictionOut)
async def get_prediction(request: Request, id: int, credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Get a specific prediction by its ID.
    
    Args:
        request (Request): FastAPI request object containing user_id in state
        id (int): ID of the prediction to retrieve
        credentials: JWT bearer token for authentication
    
    Returns:
        prediction_schema.PredictionOut: The prediction with input data and result
        
    Raises:
        HTTPException: 404 if user or prediction does not exist
    """
    user_id = request.state.user_id
    try:
        prediction = await prediction_service.get_prediction(user_id, id)
        return prediction
    except HTTPException as e:
        raise e

@router.delete("/delete/{id}", response_model=prediction_schema.PredictionOut)
async def delete_prediction(request: Request, id: int, credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Delete a specific prediction record.
    
    Args:
        request (Request): FastAPI request object containing user_id in state
        id (int): ID of the prediction to delete
        credentials: JWT bearer token for authentication
    
    Returns:
        prediction_schema.PredictionOut: The deleted prediction information
        
    Raises:
        HTTPException: 404 if user or prediction does not exist
    """
    user_id = request.state.user_id
    try:
        prediction = await prediction_service.delete_prediction(user_id, id)
        return prediction
    except HTTPException as e:
        raise e

from fastapi import APIRouter, HTTPException, Depends, Request
from backend.schemas import prediction_schema
from backend.services import prediction_service
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

router = APIRouter()
security = HTTPBearer()

@router.post("/predict", response_model=prediction_schema.PredictionOut)
async def predict(request: Request, prediction_data: prediction_schema.PredictionCreate, credentials: HTTPAuthorizationCredentials = Depends(security)):
    user_id = request.state.user_id
    try:
        prediction = await prediction_service.make_prediction(user_id, prediction_data)
        return prediction
    except HTTPException as e:
        raise e

@router.get("/get/all", response_model=list[prediction_schema.PredictionOut])
async def get_current_user_predictions(request: Request, credentials: HTTPAuthorizationCredentials = Depends(security)):
    user_id = request.state.user_id
    try:
        predictions = await prediction_service.get_predictions(user_id, user_id)
        return predictions
    except HTTPException as e:
        raise e

@router.get("/get/all/{id}", response_model=list[prediction_schema.PredictionOut])
async def get_user_predictions(request: Request, id: int, credentials: HTTPAuthorizationCredentials = Depends(security)):
    user_id = request.state.user_id
    try:
        predictions = await prediction_service.get_predictions(user_id, id)
        return predictions
    except HTTPException as e:
        raise e

@router.get("/get/{id}", response_model=prediction_schema.PredictionOut)
async def get_prediction(request: Request, id: int, credentials: HTTPAuthorizationCredentials = Depends(security)):
    user_id = request.state.user_id
    try:
        prediction = await prediction_service.get_prediction(user_id, id)
        return prediction
    except HTTPException as e:
        raise e

@router.delete("/delete/{id}", response_model=prediction_schema.PredictionOut)
async def delete_prediction(request: Request, id: int, credentials: HTTPAuthorizationCredentials = Depends(security)):
    user_id = request.state.user_id
    try:
        prediction = await prediction_service.delete_prediction(user_id, id)
        return prediction
    except HTTPException as e:
        raise e

from fastapi import APIRouter, HTTPException, Depends, Request
from backend.schemas import prediction_schema
from backend.services import prediction_service
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

router = APIRouter()
security = HTTPBearer()

@router.post("/predict", response_model=prediction_schema.PredictionOut)
async def update_user(request: Request, prediction_data: prediction_schema.PredictionCreate, credentials: HTTPAuthorizationCredentials = Depends(security)):
    user_id = request.state.user_id
    try:
        prediction = await prediction_service.make_prediction(user_id, prediction_data)
        return prediction
    except HTTPException as e:
        raise e

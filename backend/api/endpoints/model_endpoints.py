from fastapi import APIRouter, HTTPException, Depends
from backend.schemas import model_schema
from backend.services import model_service
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

router = APIRouter()
security = HTTPBearer()

@router.get("/get", response_model=model_schema.ModelOut)
async def predict(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        model = await model_service.get_model()
        return model
    except HTTPException as e:
        raise e

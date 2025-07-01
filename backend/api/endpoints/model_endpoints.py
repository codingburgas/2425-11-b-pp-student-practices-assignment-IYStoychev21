from fastapi import APIRouter, HTTPException, Depends
from schemas import model_schema
from services import model_service
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

router = APIRouter()
security = HTTPBearer()

@router.get("/get", response_model=model_schema.ModelOut)
async def get_model(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        model = await model_service.get_model()
        return model
    except HTTPException as e:
        raise e

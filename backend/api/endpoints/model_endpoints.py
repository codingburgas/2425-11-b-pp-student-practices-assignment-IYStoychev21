from fastapi import APIRouter, HTTPException, Depends
from schemas import model_schema
from services import model_service
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

router = APIRouter()
security = HTTPBearer()

@router.get("/get", response_model=model_schema.ModelOut)
async def get_model(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Get the current machine learning model information.
    
    Args:
        credentials: JWT bearer token for authentication
    
    Returns:
        model_schema.ModelOut: Complete model information including hyperparameters,
                              training/test split configuration, model parameters,
                              and performance metrics
                              
    Raises:
        HTTPException: 404 if model does not exist
    """
    try:
        model = await model_service.get_model()
        return model
    except HTTPException as e:
        raise e

from fastapi.exceptions import HTTPException
from repositories import models_repository

async def get_model():
    """
    Retrieve the current machine learning model information.

    Returns:
        Model: Complete model information including hyperparameters,
               training/test split configuration, model parameters,
               and performance metrics

    Raises:
        HTTPException: 404 if model does not exist
    """
    model = await models_repository.get_model()
    if not model:
        raise HTTPException(status_code=404, detail="Model does not exist")

    return model

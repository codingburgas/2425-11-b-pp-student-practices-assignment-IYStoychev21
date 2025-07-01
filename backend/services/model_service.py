from fastapi.exceptions import HTTPException
from repositories import models_repository

async def get_model():
    model = await models_repository.get_model()
    if not model:
        raise HTTPException(status_code=404, detail="Model does not exist")

    return model

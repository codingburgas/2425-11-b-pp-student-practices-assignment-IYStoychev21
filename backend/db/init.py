from tortoise import Tortoise
from db.config import TORTOISE_ORM
from models import role_model, models_model

async def init_db():
    """
    Initialize the database connection and seed default data.
    
    This function performs the following operations:
    - Initializes Tortoise ORM with the database configuration
    - Generates database schemas for all models
    - Creates default user roles ('user' and 'admin') if they don't exist
    - Creates default hyperparameters for ML model training if they don't exist
    - Creates default train/test split configuration if it doesn't exist
    
    The function is idempotent - it can be called multiple times safely
    as it checks for existing data before creating new records.
    """
    await Tortoise.init(config=TORTOISE_ORM)
    await Tortoise.generate_schemas()

    existing = await role_model.Role.all().values_list("role_name", flat=True)
    for role_name in ["user", "admin"]:
        if role_name not in existing:
            await role_model.Role.create(role_name=role_name)

    try:
        await models_model.HyperParams.get(id=1)
    except:
        await models_model.HyperParams.create(epochs=1000, learning_rate=0.0001)

    try:
        await models_model.TestTrainSplit.get(id=1)
    except:
        await models_model.TestTrainSplit.create(testing=0.2, training=0.8)

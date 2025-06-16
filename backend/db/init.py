from tortoise import Tortoise
from backend.db.config import TORTOISE_ORM
from backend.models import role_model

async def init_db():
    await Tortoise.init(config=TORTOISE_ORM)
    await Tortoise.generate_schemas()

    existing = await role_model.Role.all().values_list("role_name", flat=True)
    for role_name in ["user", "admin"]:
        if role_name not in existing:
            await role_model.Role.create(role_name=role_name)

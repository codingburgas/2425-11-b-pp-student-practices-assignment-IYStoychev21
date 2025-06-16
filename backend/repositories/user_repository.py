from backend.models import user_model, role_model
from backend.schemas import user_schema

async def get_user_by_username(username: str):
    try:
        return await user_model.User.all().select_related("role").get(username=username)
    except:
        return None

async def get_user_by_id(user_id: int):
    try:
        return await user_model.User.all().select_related("role").get(id=user_id)
    except:
        return None

async def create_user(username: str, first_name: str, last_name: str, password_hash: str):
    role = await role_model.Role.get(role_name="user")
    user = await user_model.User.create(username=username, first_name=first_name, last_name=last_name, password_hash=password_hash, role=role)
    return user

async def delete_user(user_id: int):
    await user_model.User.filter(id=user_id).delete()

async def update_user(user_id: int, user_data: user_schema.UserUpdate):
    await user_model.User.filter(id=user_id).update(**user_data.dict(exclude_unset=True))

async def get_all_users():
    return await user_model.User.all().select_related("role")

async def update_user_role(user_id: int, role_id: int):
    role = await role_model.Role.get(id=role_id)
    await user_model.User.filter(id=user_id).update(role=role)
    return await user_model.User.get(id=user_id)

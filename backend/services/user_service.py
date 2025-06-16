from fastapi.exceptions import HTTPException
from backend.repositories import user_repository
from backend.schemas import user_schema

async def get_current_user(user_id: int):
    user = await user_repository.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User does not exist")

    return user

async def delete_current_user(user_id: int):
    user = await user_repository.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User does not exist")

    await user_repository.delete_user(user.id)
    return user

async def delete_user_admin(user_id: int, user_id_to_delete):
    user = await user_repository.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User does not exist")

    user_to_delete = await user_repository.get_user_by_id(user_id_to_delete)
    if not user_to_delete:
        raise HTTPException(status_code=404, detail="User does not exist")

    if user.role.role_name != "admin":
        raise HTTPException(status_code=403, detail="You don't have permissions")

    await user_repository.delete_user(user_id_to_delete)
    return user_to_delete

async def update_current_user(user_id: int, user_data: user_schema.UserUpdate):
    user = await user_repository.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User does not exist")

    if not user_data.first_name:
        user_data.first_name = user.first_name

    if not user_data.last_name:
        user_data.last_name = user.last_name

    await user_repository.update_user(user.id, user_data)
    updated_user = await user_repository.get_user_by_id(user_id)

    return updated_user

async def update_user_admin(user_id: int, user_id_to_update: int, user_data: user_schema.UserUpdate):
    user = await user_repository.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User does not exist")

    user_to_update = await user_repository.get_user_by_id(user_id_to_update)
    if not user_to_update:
        raise HTTPException(status_code=404, detail="User does not exist")

    if user.role.role_name != "admin":
        raise HTTPException(status_code=403, detail="You don't have permissions")

    if not user_data.first_name:
        user_data.first_name = user_to_update.first_name

    if not user_data.last_name:
        user_data.last_name = user_to_update.last_name

    await user_repository.update_user(user_to_update.id, user_data)
    updated_user = await user_repository.get_user_by_id(user_id_to_update)

    return updated_user

async def get_all_users(user_id: int):
    user = await user_repository.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User does not exist")

    users = await user_repository.get_all_users()
    return users

async def get_user(user_id: int, user_id_to_retrive: int):
    user = await user_repository.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User does not exist")

    user_to_retrive = await user_repository.get_user_by_id(user_id_to_retrive)
    if not user_to_retrive:
        raise HTTPException(status_code=404, detail="User does not exist")

    return user_to_retrive

async def change_user_role(user_id: int, user_to_chage_id: int, role_id : int):
    user = await user_repository.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User does not exist")

    user_to_change = await user_repository.get_user_by_id(user_to_chage_id)
    if not user_to_change:
        raise HTTPException(status_code=404, detail="User does not exist")

    if user.role.role_name != "admin":
        raise HTTPException(status_code=403, detail="You don't have permissions")

    await user_repository.update_user_role(user_to_change.id, role_id)
    updated_user = await user_repository.get_user_by_id(user_to_chage_id)

    return updated_user

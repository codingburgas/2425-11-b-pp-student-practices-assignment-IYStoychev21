from fastapi.exceptions import HTTPException
from repositories import user_repository
from schemas import user_schema

async def get_current_user(user_id: int):
    """
    Get the current user by their ID.
    
    Args:
        user_id (int): The ID of the user to retrieve
        
    Returns:
        User: The user object with role information
        
    Raises:
        HTTPException: 404 if user does not exist
    """
    user = await user_repository.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User does not exist")

    return user

async def delete_current_user(user_id: int):
    """
    Delete the current user account.
    
    Args:
        user_id (int): The ID of the user to delete
        
    Returns:
        User: The deleted user object
        
    Raises:
        HTTPException: 404 if user does not exist
    """
    user = await user_repository.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User does not exist")

    await user_repository.delete_user(user.id)
    return user

async def delete_user_admin(user_id: int, user_id_to_delete):
    """
    Delete a user account (admin operation).
    
    Args:
        user_id (int): The ID of the admin user performing the operation
        user_id_to_delete (int): The ID of the user to delete
        
    Returns:
        User: The deleted user object
        
    Raises:
        HTTPException: 404 if user does not exist, 403 if not admin
    """
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
    """
    Update the current user's profile information.
    
    Args:
        user_id (int): The ID of the user to update
        user_data (user_schema.UserUpdate): The updated user data
        
    Returns:
        User: The updated user object
        
    Raises:
        HTTPException: 404 if user does not exist
    """
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
    """
    Update another user's profile information (admin operation).
    
    Args:
        user_id (int): The ID of the admin user performing the operation
        user_id_to_update (int): The ID of the user to update
        user_data (user_schema.UserUpdate): The updated user data
        
    Returns:
        User: The updated user object
        
    Raises:
        HTTPException: 404 if user does not exist, 403 if not admin
    """
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
    """
    Get all users in the system.
    
    Args:
        user_id (int): The ID of the user requesting the list
        
    Returns:
        list[User]: List of all users with role information
        
    Raises:
        HTTPException: 404 if requesting user does not exist
    """
    user = await user_repository.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User does not exist")

    users = await user_repository.get_all_users()
    return users

async def get_user(user_id: int, user_id_to_retrive: int):
    """
    Get a specific user by ID.
    
    Args:
        user_id (int): The ID of the user making the request
        user_id_to_retrive (int): The ID of the user to retrieve
        
    Returns:
        User: The requested user object
        
    Raises:
        HTTPException: 404 if either user does not exist
    """
    user = await user_repository.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User does not exist")

    user_to_retrive = await user_repository.get_user_by_id(user_id_to_retrive)
    if not user_to_retrive:
        raise HTTPException(status_code=404, detail="User does not exist")

    return user_to_retrive

async def change_user_role(user_id: int, user_to_chage_id: int, role_id : int):
    """
    Change a user's role (admin operation).
    
    Args:
        user_id (int): The ID of the admin user performing the operation
        user_to_chage_id (int): The ID of the user whose role to change
        role_id (int): The ID of the new role to assign
        
    Returns:
        User: The user object with updated role
        
    Raises:
        HTTPException: 404 if user does not exist, 403 if not admin
    """
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

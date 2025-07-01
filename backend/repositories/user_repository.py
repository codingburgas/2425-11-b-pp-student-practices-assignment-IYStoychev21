from models import user_model, role_model
from schemas import user_schema

async def get_user_by_username(username: str):
    """
    Retrieve a user by their username.
    
    Args:
        username (str): The username to search for
        
    Returns:
        User|None: User object with role information if found, None otherwise
    """
    try:
        return await user_model.User.all().select_related("role").get(username=username)
    except:
        return None

async def get_user_by_id(user_id: int):
    """
    Retrieve a user by their ID.
    
    Args:
        user_id (int): The user ID to search for
        
    Returns:
        User|None: User object with role information if found, None otherwise
    """
    try:
        return await user_model.User.all().select_related("role").get(id=user_id)
    except:
        return None

async def create_user(username: str, first_name: str, last_name: str, password_hash: str):
    """
    Create a new user with default 'user' role.
    
    Args:
        username (str): Unique username for the new user
        first_name (str): User's first name
        last_name (str): User's last name
        password_hash (str): Hashed password
        
    Returns:
        User: The newly created user object
    """
    role = await role_model.Role.get(role_name="user")
    user = await user_model.User.create(username=username, first_name=first_name, last_name=last_name, password_hash=password_hash, role=role)
    return user

async def delete_user(user_id: int):
    """
    Delete a user by their ID.
    
    Args:
        user_id (int): The ID of the user to delete
    """
    await user_model.User.filter(id=user_id).delete()

async def update_user(user_id: int, user_data: user_schema.UserUpdate):
    """
    Update user information.
    
    Args:
        user_id (int): The ID of the user to update
        user_data (user_schema.UserUpdate): The updated user data
    """
    await user_model.User.filter(id=user_id).update(**user_data.dict(exclude_unset=True))

async def get_all_users():
    """
    Retrieve all users in the system.
    
    Returns:
        list[User]: List of all users with role information
    """
    return await user_model.User.all().select_related("role")

async def update_user_role(user_id: int, role_id: int):
    """
    Update a user's role.
    
    Args:
        user_id (int): The ID of the user to update
        role_id (int): The ID of the new role to assign
        
    Returns:
        User: The updated user object
    """
    role = await role_model.Role.get(id=role_id)
    await user_model.User.filter(id=user_id).update(role=role)
    return await user_model.User.get(id=user_id)

from tortoise import fields, models

class User(models.Model):
    """
    User model representing system users.
    
    Attributes:
        id (int): Primary key, auto-generated user ID
        username (str): Unique username for authentication (max 255 chars)
        first_name (str): User's first name (max 255 chars)
        last_name (str): User's last name (max 255 chars)
        password_hash (str): Bcrypt hashed password (max 255 chars)
        role (Role): Foreign key reference to user's role (user/admin)
        
    Related:
        predictions: One-to-many relationship with Predictions model
    """
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=255, null=False, unique=True)
    first_name = fields.CharField(max_length=255, null=False)
    last_name = fields.CharField(max_length=255, null=False)
    password_hash = fields.CharField(max_length=255, null=False)
    role = fields.ForeignKeyField(
        "models.Role",
        related_name="users",
        null=True
    )

    class Meta:
        table = "users"

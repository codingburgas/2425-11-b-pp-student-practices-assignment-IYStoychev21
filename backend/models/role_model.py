from tortoise import fields, models

class Role(models.Model):
    """
    Role model representing user roles in the system.
    
    Attributes:
        id (int): Primary key, auto-generated role ID
        role_name (str): Unique role name (e.g., 'user', 'admin'), max 50 chars
        
    Related:
        users: One-to-many relationship with User model
    """
    id = fields.IntField(pk=True)
    role_name = fields.CharField(null=False, unique=True, max_length=50)

    class Meta:
        table = "roles"

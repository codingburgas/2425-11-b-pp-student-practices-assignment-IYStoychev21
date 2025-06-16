from tortoise import fields, models

class User(models.Model):
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

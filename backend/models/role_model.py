from tortoise import fields, models

class Role(models.Model):
    id = fields.IntField(pk=True)
    role_name = fields.CharField(null=False, unique=True, max_length=50)

    class Meta:
        table = "roles"

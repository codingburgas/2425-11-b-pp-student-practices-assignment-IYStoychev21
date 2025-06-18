from tortoise import fields, models

class Predictions(models.Model):
    id = fields.IntField(pk=True)
    prediction = fields.BooleanField()
    prediction_inputs = fields.ForeignKeyField(
        "models.PredictionInputs",
        related_name="predictions",
        null=True
    )
    user = fields.ForeignKeyField(
        "models.User",
        related_name="predictions",
        null=True
    )

    class Meta:
        table = "predictions"

class PredictionInputs(models.Model):
    id = fields.IntField(pk=True)
    no_of_dependents = fields.IntField()
    education = fields.BooleanField()
    self_employed = fields.BooleanField()
    income_amount = fields.IntField()
    loan_amont = fields.IntField()
    loan_amont_term = fields.IntField()
    cibil_score = fields.IntField()
    residential_assets_value = fields.IntField()
    commercial_assets_value = fields.IntField()
    luxury_assets_value = fields.IntField()
    bank_asset_value = fields.IntField()

    class Meta:
        table = "prediction_input"

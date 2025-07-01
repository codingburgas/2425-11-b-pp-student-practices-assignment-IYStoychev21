from tortoise import fields, models

class Predictions(models.Model):
    """
    Predictions model representing loan approval prediction results.
    
    Attributes:
        id (int): Primary key, auto-generated prediction ID
        prediction (bool): Prediction result (True for approved, False for rejected)
        created_at (datetime): Timestamp when prediction was created (auto-generated)
        title (str): Descriptive title for the prediction (max 512 chars)
        prediction_inputs (PredictionInputs): Foreign key to input data used for prediction
        user (User): Foreign key to the user who made the prediction
    """
    id = fields.IntField(pk=True)
    prediction = fields.BooleanField()
    created_at = fields.DatetimeField(auto_now_add=True)
    title = fields.CharField(max_length=512)
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
    """
    PredictionInputs model representing input data for loan predictions.
    
    Attributes:
        id (int): Primary key, auto-generated input ID
        no_of_dependents (int): Number of dependents
        education (bool): Education status (True for graduate, False for non-graduate)
        self_employed (bool): Self-employment status
        income_amount (int): Annual income amount
        loan_amont (int): Requested loan amount
        loan_amont_term (int): Loan term in months
        cibil_score (int): Credit score (CIBIL score)
        residential_assets_value (int): Value of residential assets
        commercial_assets_value (int): Value of commercial assets
        luxury_assets_value (int): Value of luxury assets
        bank_asset_value (int): Value of bank assets
        
    Related:
        predictions: One-to-many relationship with Predictions model
    """
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

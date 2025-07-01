from pydantic import BaseModel
from schemas import user_schema
from datetime import datetime

class PredictionCreate(BaseModel):
    """
    Schema for creating a new loan prediction request.
    
    Contains all the input data required for the ML model to make
    a loan approval prediction.
    
    Attributes:
        no_of_dependents (int): Number of dependents
        title (str): Descriptive title for the prediction
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
    """
    no_of_dependents: int
    title: str
    education: bool
    self_employed: bool
    income_amount: int
    loan_amont: int
    loan_amont_term: int
    cibil_score: int
    residential_assets_value: int
    commercial_assets_value: int
    luxury_assets_value: int
    bank_asset_value: int

class PredictionInputsOut(BaseModel):
    """
    Schema for prediction input data output.
    
    Used when returning the input parameters that were used
    for a specific prediction.
    
    Attributes:
        id (int): Input record's unique identifier
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
    """
    id: int
    no_of_dependents: int
    education: bool
    self_employed: bool
    income_amount: int
    loan_amont: int
    loan_amont_term: int
    cibil_score: int
    residential_assets_value: int
    commercial_assets_value: int
    luxury_assets_value: int
    bank_asset_value: int


class PredictionOut(BaseModel):
    """
    Schema for prediction output data (response model).
    
    Contains the complete prediction result including the input data,
    prediction outcome, and metadata.
    
    Attributes:
        id (int): Prediction record's unique identifier
        prediction (bool): Prediction result (True for approved, False for rejected)
        created_at (datetime): Timestamp when prediction was created
        title (str): Descriptive title for the prediction
        prediction_inputs (PredictionInputsOut): Input data used for the prediction
        user (user_schema.UserOut): User who made the prediction
    """
    id: int
    prediction: bool
    created_at: datetime
    title: str
    prediction_inputs: PredictionInputsOut
    user: user_schema.UserOut

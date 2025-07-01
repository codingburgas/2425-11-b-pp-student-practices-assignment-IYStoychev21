from pydantic import BaseModel
from schemas import user_schema
from datetime import datetime

class PredictionCreate(BaseModel):
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
    id: int
    prediction: bool
    created_at: datetime
    title: str
    prediction_inputs: PredictionInputsOut
    user: user_schema.UserOut

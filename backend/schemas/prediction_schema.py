from pydantic import BaseModel
from backend.schemas import user_schema

class PredictionCreate(BaseModel):
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
    prediction_inputs: PredictionInputsOut
    user: user_schema.UserOut

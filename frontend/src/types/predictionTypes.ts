import { type UserType } from "./userTypes"

export type PredictionInputType = {
    id: number,
    no_of_dependents: number,
    education: boolean,
    self_employed: boolean,
    income_amount: number,
    loan_amont: number,
    loan_amont_term: number,
    cibil_score: number,
    residential_assets_value: number,
    commercial_assets_value: number,
    luxury_assets_value: number,
    bank_asset_value: number
}

export type PredictionType = {
    id: number,
    prediction: boolean,
    created_at: string,
    title: string,
    prediction_inputs: PredictionInputType,
    user: UserType
}

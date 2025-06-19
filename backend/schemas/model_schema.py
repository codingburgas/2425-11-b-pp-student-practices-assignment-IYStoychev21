from pydantic import BaseModel

class HyperParamsOut(BaseModel):
    id: int
    epochs: int
    learning_rate: float

class ParamsOut(BaseModel):
    id: int
    weights: list[list]
    bias: float
    x_mean: list[float]
    x_std: list[float]

class TestTrainSplitOut(BaseModel):
    id: int
    testing: float
    training: float

class ModelMetricsOut(BaseModel):
    id: int
    accuracy: float
    precision: float
    f1_score: float
    recall: float
    confusion_matrix: list[list]

class ModelOut(BaseModel):
    id: int
    hyper_params: HyperParamsOut
    test_train_split: TestTrainSplitOut
    params: ParamsOut
    model_metrics: ModelMetricsOut

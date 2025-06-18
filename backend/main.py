from fastapi import FastAPI
from backend.db.init import init_db
from backend.api.endpoints import auth_endpoints, user_endpoints, prediction_endpoints
from backend.middlewares import auth_middleware
from backend.ML import load_prediction_logistic_regression
from backend.repositories import models_repository

app = FastAPI()

app.add_middleware(auth_middleware.AuthMiddleware)

@app.on_event("startup")
async def startup_event():
    await init_db()

    hyper_params = await models_repository.get_hyper_params()
    test_train_split = await models_repository.get_test_train_split()

    try:
        await models_repository.get_params()
    except:
        model = load_prediction_logistic_regression.LoanPrediction("./training-dataset/loan_approval_dataset.csv", train_size=test_train_split.training, learning_rate=hyper_params.learning_rate, epochs=hyper_params.epochs)
        model.train()
        print(model.X_std)
        await models_repository.set_params(weights=model.get_weights(), bias=model.get_bias(), x_mean=model.X_mean.tolist(), x_std=model.X_std.tolist())
        await models_repository.add_model(accuracy=model.get_accuracy())

app.include_router(auth_endpoints.router, prefix="/api/auth", tags=["Auth"])
app.include_router(user_endpoints.router, prefix="/api/users", tags=["Users"])
app.include_router(prediction_endpoints.router, prefix="/api/predictions", tags=["Predictions"])

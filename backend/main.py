from fastapi import FastAPI
from db.init import init_db
from api.endpoints import auth_endpoints, user_endpoints, prediction_endpoints, model_endpoints
from middlewares import auth_middleware
from ML import load_prediction_logistic_regression
from repositories import models_repository
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(auth_middleware.AuthMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "https://gentle-tree-0f9312803.2.azurestaticapps.net"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    """
    Initialize the application on startup.
    
    This function is called when the FastAPI application starts up. It performs
    the following initialization tasks:
    - Initializes the database connection and creates schemas
    - Retrieves hyperparameters and train/test split configuration
    - Trains a new machine learning model if parameters don't exist
    - Stores model parameters and metrics in the database
    
    The ML model is only trained once on startup if no existing parameters
    are found in the database.
    """
    await init_db()

    hyper_params = await models_repository.get_hyper_params()
    test_train_split = await models_repository.get_test_train_split()

    try:
        await models_repository.get_params()
    except:
        model = load_prediction_logistic_regression.LoanPrediction("./training-dataset/loan_approval_dataset.csv", train_size=test_train_split.training, learning_rate=hyper_params.learning_rate, epochs=hyper_params.epochs)
        model.train()
        await models_repository.set_params(weights=model.get_weights(), bias=model.get_bias(), x_mean=model.X_mean.tolist(), x_std=model.X_std.tolist())
        await models_repository.set_model_metrics(model.get_accuracy(), model.get_precision(), model.get_f1_score(), model.get_recall(), model.get_confusion_matrix())
        await models_repository.add_model()

app.include_router(auth_endpoints.router, prefix="/api/auth", tags=["Auth"])
app.include_router(user_endpoints.router, prefix="/api/users", tags=["Users"])
app.include_router(prediction_endpoints.router, prefix="/api/predictions", tags=["Predictions"])
app.include_router(model_endpoints.router, prefix="/api/models", tags=["Models"])

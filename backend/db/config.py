import os

TORTOISE_ORM = {
    "connections": {
        "default": f"postgres://{os.environ['DB_USER']}:{os.environ['DB_PASSWORD']}@{os.environ['DB_HOST']}:{os.environ['DB_PORT']}/{os.environ['DB_NAME']}"
    },
    "apps": {
        "models": {
            "models": ["models.role_model", "models.user_model", "models.models_model", "models.predictions_model"],
            "default_connection": "default",
        },
    },
}

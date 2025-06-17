import os

TORTOISE_ORM = {
    "connections": {
        "default": f"postgres://{os.environ["DB_USER"]}:{os.environ["DB_PASSWORD"]}@{os.environ["DB_HOST"]}:{os.environ["DB_PORT"]}/{os.environ["DB_NAME"]}"
    },
    "apps": {
        "models": {
            "models": ["backend.models.role_model", "backend.models.user_model", "backend.models.models_model"],
            "default_connection": "default",
        },
    },
}

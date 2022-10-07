from src.settings import Settings

setting = Settings()

TORTOISE_ORM = {
    "connections": {"local": setting.postgres_dsn},
    "apps": {
        "models": {
            "models": [
                "src.data_model",
                "aerich.models"
            ],
            "default_connection": "local",
        },
    },
}

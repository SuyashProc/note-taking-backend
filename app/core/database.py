from tortoise.contrib.fastapi import register_tortoise
from app.core.config import DATABASE_URL

TORTOISE_ORM = {
    "connections": {
        "default": DATABASE_URL
    },
    "apps": {
        "models": {
            "models": [
                "app.models.user",
                "app.models.note",
                "aerich.models"
            ],
            "default_connection": "default",
        }
    }
}


def init_db(app):
    register_tortoise(
        app,
        config=TORTOISE_ORM,
        generate_schemas=False,
        add_exception_handlers=True,
    )
from tortoise import Tortoise
from src.settings import Settings
from src.model_description import TORTOISE_ORM


class PostgresConnection:

    def __init__(self, settings: Settings()) -> None:
        self.settings = settings

    async def init_orm(self):
        await Tortoise.init(
            config=TORTOISE_ORM
        )
        await Tortoise.generate_schemas()

    async def close_orm(self) -> None:
        await Tortoise.close_connections()

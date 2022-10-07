from tortoise import Tortoise
from settings import Settings


class PostgresConnection:

    def __init__(self, settings: Settings()) -> None:
        self.settings = settings

    async def init_orm(self):
        await Tortoise.init(
            db_url=self.settings.postgres_dsn,
            modules={'models': ['data_model']}
        )
        await Tortoise.generate_schemas()
        await Tortoise.close_connections()

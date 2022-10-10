import asyncio
from aerich import Command

from file_process import FileProcess
from model_description import TORTOISE_ORM
from postgres.postgres_connection_manager import PostgresConnection
from postgres.repository import Repository
from settings import Settings

settings = Settings()
postgres = PostgresConnection(settings)
repository = Repository()
file_process = FileProcess()


async def init_db():
    command = Command(tortoise_config=TORTOISE_ORM, app='models')
    await command.init()


async def insert_records():
    for index, row in file_process.data.iterrows():
        await Repository().insert_records(row.to_dict())


def run():
    loop = asyncio.get_event_loop()
    try:
        tasks = asyncio.gather(
            init_db(),
            postgres.init_orm(),
        )
        loop.run_until_complete(tasks)
        loop.run_until_complete(insert_records())
    finally:
        loop.run_until_complete(postgres.close_orm())


run()

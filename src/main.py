import asyncio
from tortoise import run_async

from file_process import FileProcess
from postgres.postgres_connection_manager import PostgresConnection
from settings import Settings

settings = Settings()

file_process = FileProcess()
file_process.create_model()

run_async(PostgresConnection(settings).init_orm())

from postgres.repository import Repository


async def insert_records():
    for index, row in file_process.data.iterrows():
        await Repository().insert_records(row.to_dict())

asyncio.run(insert_records())

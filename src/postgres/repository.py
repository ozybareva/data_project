from data_model import DataModel


class Repository:

    @staticmethod
    async def insert_records(data):
        await DataModel.create(**data)

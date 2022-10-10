from tortoise.models import Model
from tortoise.fields import CharField, FloatField, IntField


class DataModel(Model):
    id = IntField(pk=True)

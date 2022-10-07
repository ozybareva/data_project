from tortoise.models import Model
from tortoise.fields import CharField, FloatField, IntField


class DataModel(Model):
	id = IntField(pk=True)
	ID_UCH_VOST_POL = IntField()
	NAME_BEGIN_VOST_UCH = CharField(max_length=25)
	ESR_BEGIN_VOST_UCH = IntField()
	DOR_BEGIN_VOST_UCH = IntField()
	OKATO_BEGIN_VOST_UCH_NAME = CharField(max_length=100)
	X_BEG_VOST_UCH = FloatField()
	Y_BEG_VOST_UCH = FloatField()
	NAME_END_VOST_UCH = CharField(max_length=25)
	ESR_END_VOST_UCH = IntField()
	DOR_END_VOST_UCH = IntField()
	OKATO_END_VOST_UCH_NAME = CharField(max_length=100)
	X_END_VOST_UCH = FloatField()
	Y_END_VOST_UCH = FloatField()
	NUM_CNSI_MELK_SET = IntField()
	NAME_BEGIN_MELK_SET = CharField(max_length=29)
	ESR_BEGIN_MELK_SET = IntField()
	DOR_BEGIN_MELK_SET = IntField()
	OKATO_BEGIN_MELK_SET_NAME = CharField(max_length=100)
	NAME_END_MELK_SET = CharField(max_length=29)
	ESR_END_MELK_SET = IntField()
	DOR_END_MELK_SET = IntField()
	OKATO_END_MELK_SET_NAME = CharField(max_length=100)

	class Meta:
		table = "data_table"

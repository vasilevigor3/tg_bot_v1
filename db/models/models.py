from peewee import Model, AutoField, TextField, BooleanField

from db.connection import conn


class BaseModel(Model):
    class Meta:
        database = conn


class RUSFigiModel(BaseModel):
    figi_id = AutoField(column_name='id')
    ticker = TextField(column_name='ticker')
    long_or_short = BooleanField(column_name='long_or_short', null=True)

    class Meta:
        table_name = 'rus_figis'


class USDFigiModel(BaseModel):
    figi_id = AutoField(column_name='id')
    ticker = TextField(column_name='ticker')
    long_or_short = BooleanField(column_name='long_or_short', null=True)

    class Meta:
        table_name = 'usd_figis'

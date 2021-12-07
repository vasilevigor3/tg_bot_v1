from peewee import Model, AutoField, TextField, BooleanField

from db.connection import conn


class BaseModel(Model):
    class Meta:
        database = conn


class SubscribedUserModel(BaseModel):
    id = AutoField(column_name='id')
    user_id = TextField(column_name='user_id')

    class Meta:
        table_name = 'subscribed_users'


import peewee

from data.config import database_name, db_port, db_root_pass

conn = peewee.MySQLDatabase(database_name, user="root", password=db_root_pass,
                            host="db", port=3306)

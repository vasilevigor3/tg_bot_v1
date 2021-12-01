import os

from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста

TINKOFF_TOKEN = env.str("TINKOFF_TOKEN")
TINKOFF_TOKEN_SANDNOX = env.str("TINKOFF_TOKEN_SANDNOX")

# HOST = os.getenv("PGHOST")
PG_USER = os.getenv("PG_USER")
PG_PASS = os.getenv("PG_PASS")
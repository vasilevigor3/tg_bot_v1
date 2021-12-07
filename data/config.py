from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
admin_id = env.str("tg_admin")

TINKOFF_TOKEN = env.str("TINKOFF_TOKEN")
TINKOFF_TOKEN_SANDNOX = env.str("TINKOFF_TOKEN_SANDNOX")

db_root_pass = env.str("MYSQL_ROOT_PASSWORD")
db_port = env.int("port")
database_name = env.str("database_name")


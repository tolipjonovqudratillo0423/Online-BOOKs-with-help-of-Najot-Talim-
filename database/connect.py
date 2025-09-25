from psycopg2 import connect
from environs import Env


env = Env()
env.read_env()


def get_connect(query=None):
    return connect(
        user = env.str("USER"),
        password = env.str("PASSWORD"),
        database = env.str("DATABASE"),
        port = env.str("PORT"),
        host = env.str("HOST")
    )
    




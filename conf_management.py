import config as cfg
import psycopg2


def get_telegram_token():
    return cfg.TELEGRAM_TOKEN


def get_telegram_group_id():
    return cfg.TELEGRAM_GROUP_ID


def get_aemet_token():
    return cfg.AEMET_TOKEN


def get_city_id():
    return cfg.CITY_ID


def get_schedule():
    return cfg.WEATHER_SCHEDULE


def get_connection_by_config():
    db = cfg.postgresql
    conn = psycopg2.connect(**db)

    return conn

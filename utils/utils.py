import configparser

from passlib.context import CryptContext


SECRET_KEY = "eb750ede284955f0ea34e05a0dc364db05535873eec546596e3467d9423ae089"
ALGORITHM = "HS256"
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_config():
    config = configparser.ConfigParser()
    config.read("info.cfg")
    return config


def get_password_hash(password):
    return bcrypt_context.hash(password)

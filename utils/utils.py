import configparser


def get_config():
    config = configparser.ConfigParser()
    config.read("info.cfg")
    return config

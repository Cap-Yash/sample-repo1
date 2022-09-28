from configparser import ConfigParser
import os

class ReadProperties:

    def read_configuration(section, key):
        cfg = ConfigParser()
        file_path = os.path.relpath('.\\Configs\\config.ini')
        cfg.read(file_path)

        return cfg.get(section, key)
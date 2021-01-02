from src import *
import configparser
import logging


logger = logging.getLogger(__name__)


class UserSettings:

    # file_path must contain only existing directories at the moment, but it's fine if the file itself doesn't yet exist
    def __init__(self):
        self.config_parser = configparser.ConfigParser()
        self.file_path = os.path.join(PROJECT_DIRECTORY, SETTINGS_FILE_NAME)

        if not os.path.exists(self.file_path):
            self.__create_default_settings()
        else:
            self.config_parser.read(self.file_path)

    def get(self, section, key):
        if not self.config_parser.has_section(section):
            logger.error(f"Attempted to read from non-existent section \"{section}\" in {self.file_path}")
            return None

        if not self.config_parser.has_option(section, key):
            logger.error(f"Attempted to read from non-existent key \"{key}\" in \"{section}\" section of {self.file_path}")
            return None

        return self.config_parser.get(section, key)

    def set(self, section, key, value):
        if not self.config_parser.has_section(section):
            self.config_parser.add_section(section)

        self.config_parser.set(section, key, value)
        self.__write()

    def delete(self, section, key=None):
        if not self.config_parser.has_section(section):
            logger.error(f"Attempted to delete from non-existent section \"{section}\" in {self.file_path}")
            return

        if key is not None:
            if self.config_parser.has_option(section, key):
                self.config_parser.remove_option(section, key)
                self.__write()
            else:
                logger.error(f"Attempted to read from non-existent key \"{key}\" in \"{section}\" section of {self.file_path}")
                return

        self.config_parser.remove_section(section)
        self.__write()

    def __create_default_settings(self):
        self.config_parser = configparser.ConfigParser()
        self.config_parser[SETTINGS_SECTION_KEYWORDS] = {SETTINGS_KEY_ACTIVATION: SETTINGS_DEFAULT_ACTIVATION,
                                                         SETTINGS_KEY_SEPARATOR: SETTINGS_DEFAULT_SEPARATOR}
        self.config_parser[SETTINGS_SECTION_SHORTCUTS] = SETTINGS_DEFAULT_SHORTCUTS
        self.__write()

    def __write(self):
        with open(self.file_path, 'w') as config_file:
            self.config_parser.write(config_file)
            config_file.close()

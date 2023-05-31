from configparser import ConfigParser


class Config(ConfigParser):
    def __init__(self, config_file):
        super().__init__()
        self.read(config_file)

    def get_string(self, section, option):
        try:
            return self.get(section, option)
        except Exception as e:
            raise ValueError(f"Error retrieving string value for [{section}]{option}: {str(e)}")

    def get_boolean(self, section, option):
        try:
            return self.getboolean(section, option)
        except Exception as e:
            raise ValueError(f"Error retrieving boolean value for [{section}]{option}: {str(e)}")

    def get_int(self, section, option):
        try:
            return self.getint(section, option)
        except Exception as e:
            raise ValueError(f"Error retrieving boolean value for [{section}]{option}: {str(e)}")

    def get_list(self, section, option):
        try:
            value = self.get(section, option)
            return [item.strip() for item in value.split(',')]
        except Exception as e:
            raise ValueError(f"Error retrieving list value for [{section}]{option}: {str(e)}")




class ExperimentConfig:
    def __init__(self, config_file):
        config = Config(config_file)
        self.home_path = config.get_string("EXP", "home_path")
        self.run_vectorizer = config.get_boolean("EXP", "run_vectorizer")
        self.data_path = config.get_string("EXP", "data_path")



class ModelConfig:
    def __init__(self, config_file):
        config = Config(config_file)
        self.model = config.get_string("MODEL", "model")
        self.analyzer = config.get_string("MODEL", "analyzer")
        self.lower_case = config.get_string("MODEL", "lower_case")
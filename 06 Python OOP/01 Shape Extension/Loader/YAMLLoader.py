from .loader import Loader
import yaml


class YAMLLoader(Loader):
    def load(self):
        with open("input-file.yaml") as f:
            input_data = yaml.load(f)
            return(input_data)
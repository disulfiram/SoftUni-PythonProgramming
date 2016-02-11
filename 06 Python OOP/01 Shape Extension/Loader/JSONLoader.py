from .loader import Loader
import json


class JSONLoader(Loader):
    def load(self):
        with open(self.filename) as f:
            input_data = json.load(f)
            return input_data

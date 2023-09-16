import json


class AstLoader:
    def __init__(self):
        pass

    @staticmethod
    def load_json_file(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)

import json


class JSONReader:
    @staticmethod
    def read_data(json_data, key):
        if isinstance(json_data, str):
            json_data = json.loads(json_data)
        if key in json_data:
            return json_data[key]
        for k, v in json_data.items():
            if isinstance(v, dict):
                result = JSONReader.read_data(v, key)
                if result is not None:
                    return result
            elif isinstance(v, list):
                for item in v:
                    result = JSONReader.read_data(item, key)
                    if result is not None:
                        return result
        return None

    @staticmethod
    def get_item_by_index(json_data, index, key=None):
        if isinstance(json_data, str):
            json_data = json.loads(json_data)
        if isinstance(json_data, list) and index < len(json_data):
            item = json_data[index]
            if key:
                return item.get(key, None)
            return item
        return None


class TestDataGet:
    __test_data_path = "data/test_data.json"
    __config_data_path = "data/config_data.json"

    @staticmethod
    def get_test_data(key):
        with open(TestDataGet.__test_data_path, 'r') as f:
            json_data = json.load(f)
        return JSONReader.read_data(json_data, key)

    @staticmethod
    def get_config_data(key):
        with open(TestDataGet.__config_data_path, 'r') as f:
            json_data = json.load(f)
        return JSONReader.read_data(json_data, key)

    @staticmethod
    def get_data_from_books_object(index, key=None):
        with open(TestDataGet.__test_data_path, 'r') as f:
            json_data = json.load(f)
        json_index = index - 1
        return JSONReader.get_item_by_index(json_data['books'], json_index, key)

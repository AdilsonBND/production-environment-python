import json

import yaml


class HelloWord:
    def __init__(self, name: str) -> None:
        self.name = name
        self.config = yaml.safe_load("example.yaml")
        self.json_data = {"key": "value"}
        self.dump = json.dumps(self.json_data)

    def greetin(self) -> str:
        return "hello {self.name}!"

    def Goodbye(self) -> str:
        return "GoodBye"

from dataclasses import dataclass, asdict
from typing import Any

@dataclass
class User:
    name: str = 'Uknown'
    age: int
    preferences: Any = '-'


class UserHandle:
    def __init__(self, name, age):
        self._user = User(name, age)

    def get_dataclass(self):
        return asdict(self._user)

a = UserHandle('Ann', 51)

print(a.get_dataclass())
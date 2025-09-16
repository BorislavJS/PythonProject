from abc import ABC, abstractmethod
import re


class BaseGuildMember(ABC):
    _TAG_RE = re.compile(r"^[A-Za-z0-9]+$")

    def __init__(self, tag: str, gold: int, role: str, skill_level: int):
        self.tag = tag
        self.gold = gold
        self.role = role
        self.skill_level = skill_level

    @property
    def tag(self) -> str:
        return self.__tag

    @tag.setter
    def tag(self, value: str):
        if not isinstance(value, str) or not self._TAG_RE.fullmatch(value):
            raise ValueError("Tag must contain only letters and digits!")
        self.__tag = value

    @property
    def gold(self) -> int:
        return self.__gold

    @gold.setter
    def gold(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Gold must be a non-negative integer!")
        self.__gold = value

    @property
    def role(self) -> str:
        return self.__role

    @role.setter
    def role(self, value: str):
        if not isinstance(value, str) or value.strip() == "":
            raise ValueError("Role cannot be empty!")
        self.__role = value

    @property
    def skill_level(self) -> int:
        return self.__skill_level

    @skill_level.setter
    def skill_level(self, value: int):
        if not isinstance(value, int) or not (1 <= value <= 10):
            raise ValueError("Skill level is out of range!")
        self.__skill_level = value

    @abstractmethod
    def practice(self):
        pass


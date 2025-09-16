from abc import ABC, abstractmethod
import re


class BaseGuildHall(ABC):
    _ALIAS_RE = re.compile(r"^[A-Za-z ]+$")

    def __init__(self, alias: str):
        self.alias = alias
        self.__members: list = []

    @property
    def alias(self) -> str:
        return self.__alias

    @alias.setter
    def alias(self, value: str):
        if (
            not isinstance(value, str)
            or len(value.strip()) < 2
            or not self._ALIAS_RE.fullmatch(value.strip())
        ):
            raise ValueError("Guild hall alias is invalid!")
        self.__alias = value.strip()

    @property
    def members(self) -> list:
        return self.__members

    @property
    @abstractmethod
    def max_member_count(self) -> int:
        pass

    def calculate_total_gold(self) -> int:
        return sum(m.gold for m in self.members)

    def status(self) -> str:
        tags = "N/A"
        if self.members:
            tags = " *".join(sorted(m.tag for m in self.members))
        return f"Guild hall: {self.alias}; Members: {tags}; Total gold: {self.calculate_total_gold()}"

    @abstractmethod
    def increase_gold(self, min_skill_level_value: int):
        pass











































from project.guild_halls.base_guild_hall import BaseGuildHall
from project.guild_members.mage import Mage

class MagicTower(BaseGuildHall):
    @property
    def max_member_count(self) -> int:
        return 4

    def __init__(self, alias: str):
        super().__init__(alias)

    def increase_gold(self, min_skill_level_value: int):
        for m in self.members:
            if isinstance(m, Mage) and m.skill_level >= min_skill_level_value:
                m.gold *= 2



















from project.guild_members.base_guild_member import BaseGuildMember

class Warrior(BaseGuildMember):
    def __init__(self, tag: str, gold: int):
        super().__init__(tag=tag, gold=gold, role="Warrior", skill_level=2)

    def practice(self):
        new_level = min(10, self.skill_level + 2)
        self.skill_level = new_level












from character_creator.skill import Skillset

class Character:

    def __init__(self, name):
        self.name = name
        self.level = 1
        self.morality = 50
        self.credits = 500
        self.skillset = Skillset()

    def upgrade_skill(self, skill_name):
        skill = self.skillset.get_skill_by_name(skill_name)
        skill.increase_rank()



import unittest
from character_creator.skill import Skill, Skillset, SkillTypes
from character_creator.constants import SkillNames, Characteristics

class TestSkill(unittest.TestCase):

    def test_skill_class__increase_rank(self):
        cool = Skill(SkillNames.COOL, Characteristics.PRESENCE, SkillTypes.GENERAL)
        cool.increase_rank()
        self.assertEqual(1, cool.rank)

    def test_skill_class__set_career_skill(self):
        lore = Skill(SkillNames.LORE, Characteristics.INTELLECT, SkillTypes.KNOWLEDGE)
        lore.set_career_skill()
        self.assertTrue(lore.is_career_skill)


class TestSkillset(unittest.TestCase):

    def test_skillset_class__get_skill_by_name(self):
        myskills = Skillset()
        lore = myskills.get_skill_by_name(SkillNames.LORE)
        self.assertIsInstance(lore, Skill)
        self.assertEqual(lore.name, SkillNames.LORE)

    def test_skillset_class__get_ranked_skills(self):
        myskills = Skillset()
        lore = myskills.get_skill_by_name(SkillNames.LORE)
        cool = myskills.get_skill_by_name(SkillNames.COOL)
        lore.increase_rank()
        cool.increase_rank()
        ranked_skills = myskills.get_ranked_skills()
        self.assertEqual(ranked_skills, [SkillNames.COOL, SkillNames.LORE])


if __name__ == '__main__':
    unittest.main()

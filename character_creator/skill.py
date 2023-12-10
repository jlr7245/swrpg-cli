from enum import Enum

from .constants import Characteristics, SkillNames


class SkillTypes(Enum):
    GENERAL = "General"
    KNOWLEDGE = "Knowledge"
    COMBAT = "Combat"


class Skill:
    def __init__(self, name, characteristic, skill_type):
        self.name = name
        self.characteristic = characteristic
        self.skill_type = skill_type
        self.rank = 0
        self.is_career_skill = False

    def increase_rank(self):
        self.rank += 1

    def set_career_skill(self):
        self.is_career_skill = True


class Skillset:
    def __init__(self):
        self.astrogation = Skill(SkillNames.ASTROGATION,
                                 Characteristics.INTELLECT, SkillTypes.GENERAL)
        self.athletics = Skill(SkillNames.ATHLETICS,
                               Characteristics.BRAWN, SkillTypes.GENERAL)
        self.brawl = Skill(
            SkillNames.BRAWL, Characteristics.BRAWN, SkillTypes.COMBAT)
        self.charm = Skill(
            SkillNames.CHARM, Characteristics.PRESENCE, SkillTypes.GENERAL)
        self.coercion = Skill(SkillNames.COERCION,
                              Characteristics.WILLPOWER, SkillTypes.GENERAL)
        self.computers = Skill(SkillNames.COMPUTERS,
                               Characteristics.INTELLECT, SkillTypes.GENERAL)
        self.cool = Skill(
            SkillNames.COOL, Characteristics.PRESENCE, SkillTypes.GENERAL)
        self.coordination = Skill(SkillNames.COORDINATION,
                                  Characteristics.AGILITY, SkillTypes.GENERAL)
        self.core_worlds = Skill(SkillNames.CORE_WORLDS,
                                 Characteristics.INTELLECT, SkillTypes.KNOWLEDGE)
        self.deception = Skill(SkillNames.DECEPTION,
                               Characteristics.CUNNING, SkillTypes.GENERAL)
        self.discipline = Skill(SkillNames.DISCIPLINE,
                                Characteristics.WILLPOWER, SkillTypes.GENERAL)
        self.education = Skill(SkillNames.EDUCATION,
                               Characteristics.INTELLECT, SkillTypes.KNOWLEDGE)
        self.gunnery = Skill(SkillNames.GUNNERY,
                             Characteristics.AGILITY, SkillTypes.COMBAT)
        self.leadership = Skill(SkillNames.LEADERSHIP,
                                Characteristics.PRESENCE, SkillTypes.GENERAL)
        self.lore = Skill(
            SkillNames.LORE, Characteristics.INTELLECT, SkillTypes.KNOWLEDGE)
        self.mechanics = Skill(SkillNames.MECHANICS,
                               Characteristics.INTELLECT, SkillTypes.GENERAL)
        self.medicine = Skill(SkillNames.MEDICINE,
                              Characteristics.INTELLECT, SkillTypes.GENERAL)
        self.melee = Skill(
            SkillNames.MELEE, Characteristics.BRAWN, SkillTypes.COMBAT)
        self.negotiation = Skill(SkillNames.NEGOTIATION,
                                 Characteristics.PRESENCE, SkillTypes.GENERAL)
        self.outer_rim = Skill(SkillNames.OUTER_RIM,
                               Characteristics.INTELLECT, SkillTypes.KNOWLEDGE)
        self.perception = Skill(SkillNames.PERCEPTION,
                                Characteristics.CUNNING, SkillTypes.GENERAL)
        self.piloting_planetary = Skill(
            SkillNames.PILOTING_PLANETARY, Characteristics.AGILITY, SkillTypes.GENERAL)
        self.piloting_space = Skill(
            SkillNames.PILOTING_SPACE, Characteristics.AGILITY, SkillTypes.GENERAL)
        self.ranged_heavy = Skill(
            SkillNames.RANGED_HEAVY, Characteristics.AGILITY, SkillTypes.COMBAT)
        self.ranged_light = Skill(
            SkillNames.RANGED_LIGHT, Characteristics.AGILITY, SkillTypes.COMBAT)
        self.resilience = Skill(SkillNames.RESILIENCE,
                                Characteristics.BRAWN, SkillTypes.GENERAL)
        self.skulduggery = Skill(
            SkillNames.SKULDUGGERY, Characteristics.CUNNING, SkillTypes.GENERAL)
        self.stealth = Skill(SkillNames.STEALTH,
                             Characteristics.AGILITY, SkillTypes.GENERAL)
        self.streetwise = Skill(
            SkillNames.STEALTH, Characteristics.CUNNING, SkillTypes.GENERAL)
        self.survival = Skill(SkillNames.SURVIVAL,
                              Characteristics.CUNNING, SkillTypes.GENERAL)
        self.underworld = Skill(SkillNames.UNDERWORLD,
                                Characteristics.INTELLECT, SkillTypes.KNOWLEDGE)
        self.vigilance = Skill(SkillNames.VIGILANCE,
                               Characteristics.WILLPOWER, SkillTypes.GENERAL)
        self.xenology = Skill(SkillNames.XENOLOGY,
                              Characteristics.INTELLECT, SkillTypes.KNOWLEDGE)
        self.skills_list = [self.astrogation, self.athletics, self.brawl, self.charm, self.coercion, self.computers, self.cool, self.coordination, self.core_worlds, self.deception, self.discipline, self.education, self.gunnery, self.leadership, self.lore, self.mechanics, self.medicine,
                            self.melee, self.negotiation, self.outer_rim, self.perception, self.piloting_planetary, self.piloting_space, self.ranged_heavy, self.ranged_light, self.resilience, self.skulduggery, self.stealth, self.streetwise, self.survival, self.underworld, self.vigilance, self.xenology]

    def get_skill_by_name(self, name: str) -> Skill:
        skill = filter(lambda x: x.name == name, self.skills_list)
        return next(skill)

    def get_ranked_skills(self):
        skills = filter(lambda x: x.rank > 0, self.skills_list)
        return list(map(lambda x: x.name, list(skills)))

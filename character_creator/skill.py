from enum import Enum

from .constants import Abilities, SkillNames


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
                                 Abilities.INTELLECT, SkillTypes.GENERAL)
        self.athletics = Skill(SkillNames.ATHLETICS,
                               Abilities.BRAWN, SkillTypes.GENERAL)
        self.brawl = Skill(
            SkillNames.BRAWL, Abilities.BRAWN, SkillTypes.COMBAT)
        self.charm = Skill(
            SkillNames.CHARM, Abilities.PRESENCE, SkillTypes.GENERAL)
        self.coercion = Skill(SkillNames.COERCION,
                              Abilities.WILLPOWER, SkillTypes.GENERAL)
        self.computers = Skill(SkillNames.COMPUTERS,
                               Abilities.INTELLECT, SkillTypes.GENERAL)
        self.cool = Skill(
            SkillNames.COOL, Abilities.PRESENCE, SkillTypes.GENERAL)
        self.coordination = Skill(SkillNames.COORDINATION,
                                  Abilities.AGILITY, SkillTypes.GENERAL)
        self.core_worlds = Skill(SkillNames.CORE_WORLDS,
                                 Abilities.INTELLECT, SkillTypes.KNOWLEDGE)
        self.deception = Skill(SkillNames.DECEPTION,
                               Abilities.CUNNING, SkillTypes.GENERAL)
        self.discipline = Skill(SkillNames.DISCIPLINE,
                                Abilities.WILLPOWER, SkillTypes.GENERAL)
        self.education = Skill(SkillNames.EDUCATION,
                               Abilities.INTELLECT, SkillTypes.KNOWLEDGE)
        self.gunnery = Skill(SkillNames.GUNNERY,
                             Abilities.AGILITY, SkillTypes.COMBAT)
        self.leadership = Skill(SkillNames.LEADERSHIP,
                                Abilities.PRESENCE, SkillTypes.GENERAL)
        self.lore = Skill(
            SkillNames.LORE, Abilities.INTELLECT, SkillTypes.KNOWLEDGE)
        self.mechanics = Skill(SkillNames.MECHANICS,
                               Abilities.INTELLECT, SkillTypes.GENERAL)
        self.medicine = Skill(SkillNames.MEDICINE,
                              Abilities.INTELLECT, SkillTypes.GENERAL)
        self.melee = Skill(
            SkillNames.MELEE, Abilities.BRAWN, SkillTypes.COMBAT)
        self.negotiation = Skill(SkillNames.NEGOTIATION,
                                 Abilities.PRESENCE, SkillTypes.GENERAL)
        self.outer_rim = Skill(SkillNames.OUTER_RIM,
                               Abilities.INTELLECT, SkillTypes.KNOWLEDGE)
        self.perception = Skill(SkillNames.PERCEPTION,
                                Abilities.CUNNING, SkillTypes.GENERAL)
        self.piloting_planetary = Skill(
            SkillNames.PILOTING_PLANETARY, Abilities.AGILITY, SkillTypes.GENERAL)
        self.piloting_space = Skill(
            SkillNames.PILOTING_SPACE, Abilities.AGILITY, SkillTypes.GENERAL)
        self.ranged_heavy = Skill(
            SkillNames.RANGED_HEAVY, Abilities.AGILITY, SkillTypes.COMBAT)
        self.ranged_light = Skill(
            SkillNames.RANGED_LIGHT, Abilities.AGILITY, SkillTypes.COMBAT)
        self.resilience = Skill(SkillNames.RESILIENCE,
                                Abilities.BRAWN, SkillTypes.GENERAL)
        self.skulduggery = Skill(
            SkillNames.SKULDUGGERY, Abilities.CUNNING, SkillTypes.GENERAL)
        self.stealth = Skill(SkillNames.STEALTH,
                             Abilities.AGILITY, SkillTypes.GENERAL)
        self.streetwise = Skill(
            SkillNames.STEALTH, Abilities.CUNNING, SkillTypes.GENERAL)
        self.survival = Skill(SkillNames.SURVIVAL,
                              Abilities.CUNNING, SkillTypes.GENERAL)
        self.underworld = Skill(SkillNames.UNDERWORLD,
                                Abilities.INTELLECT, SkillTypes.KNOWLEDGE)
        self.vigilance = Skill(SkillNames.VIGILANCE,
                               Abilities.WILLPOWER, SkillTypes.GENERAL)
        self.xenology = Skill(SkillNames.XENOLOGY,
                              Abilities.INTELLECT, SkillTypes.KNOWLEDGE)
        self.skills_list = [self.astrogation, self.athletics, self.brawl, self.charm, self.coercion, self.computers, self.cool, self.coordination, self.core_worlds, self.deception, self.discipline, self.education, self.gunnery, self.leadership, self.lore, self.mechanics, self.medicine,
                            self.melee, self.negotiation, self.outer_rim, self.perception, self.piloting_planetary, self.piloting_space, self.ranged_heavy, self.ranged_light, self.resilience, self.skulduggery, self.stealth, self.streetwise, self.survival, self.underworld, self.vigilance, self.xenology]

    def get_skill_by_name(self, name: str) -> Skill:
        skill = filter(lambda x: x.name == name, self.skills_list)
        return next(skill)

    def get_ranked_skills(self):
        skills = filter(lambda x: x.rank > 0, self.skills_list)
        return list(map(lambda x: x.name, list(skills)))

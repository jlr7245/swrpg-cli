from character_creator.skill import Skillset

class Character:

    def __init__(self, name, species):
        # basic stats
        self.name = name
        self.credits = 500
        self.skillset = Skillset()
        self.equipment = []

        # composed from species
        self.species = species

    # various additional setups
    def setup_from_species(self):
        """Runs species-specific starting functions"""
        self.species.starting_ranks(self)
        self.species.species_bonus_choice(self)
        self.xp = self.species.starting_xp
        self.spendable_xp = self.species.starting_xp


    # skills
    def upgrade_skill(self, skill_name, is_free=False):
        """Upgrades a skill. TODO: add logic about spending XP to rank"""
        skill = self.skillset.get_skill_by_name(skill_name)
        if not is_free:
            pass # logic about xp spending here
        skill.increase_rank()

    def get_skill_rank(self, skill_name):
        """Gets rank for a particular skill"""
        skill = self.skillset.get_skill_by_name(skill_name)
        return skill.rank
    
    def list_ranked_skills(self):
        """Lists character's ranked skills"""
        ranked_skills = list(filter(lambda sk: sk.rank > 0, self.skillset.skills_list))
        ranked_list = list(map(lambda sk: f"{sk.name} -- {sk.rank}", ranked_skills))
        return "\n".join(ranked_list)
    
    # equipment + credits
    def add_equipment(self, new_gear):
        """Adds equipment to character"""
        self.equipment.append(new_gear)


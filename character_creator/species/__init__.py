from enum import Enum
from .bothan import Bothan
from .droid import Droid
from .gand import Gand
from .human import Human
from .rodian import Rodian
from .trandoshan import Trandoshan
from .twilek import Twilek
from .wookiee import Wookiee


class SpeciesName(Enum):
    BOTHAN = "Bothan"
    DROID = "Droid"
    GAND = "Gand"
    HUMAN = "Human"
    RODIAN = "Rodian"
    TRANDOSHAN = "Trandoshan"
    TWILEK = "Twi'lek"
    WOOKIEE = "Wookiee"

    @classmethod
    def values(cls):
        return [e.value for e in cls]

species_lookup = {
    SpeciesName.BOTHAN.value: Bothan,
    SpeciesName.DROID.value: Droid,
    SpeciesName.GAND.value: Gand,
    SpeciesName.HUMAN.value: Human,
    SpeciesName.RODIAN.value: Rodian,
    SpeciesName.TRANDOSHAN.value: Trandoshan,
    SpeciesName.TWILEK.value: Twilek,
    SpeciesName.WOOKIEE.value: Wookiee
}

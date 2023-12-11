from enum import Enum
from .bothan import Bothan
from .droid import Droid
from .gand import Gand
from .species import Species

class SpeciesName(Enum):
    BOTHAN = "Bothan"
    DROID = "Droid"
    GAND = "Gand"

    @classmethod
    def values(cls):
        return [e.value for e in cls]

species_lookup = {
    SpeciesName.BOTHAN.value: Bothan,
    SpeciesName.DROID.value: Droid,
    SpeciesName.GAND.value: Gand,
}

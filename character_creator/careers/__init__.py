from enum import Enum
from .bounty_hunter import bounty_hunter


class CareerName(Enum):
    BOUNTY_HUNTER = "Bounty Hunter"

    @classmethod
    def values(cls):
        return [e.value for e in cls]


careers_lookup = {
    CareerName.BOUNTY_HUNTER.value: bounty_hunter,
}

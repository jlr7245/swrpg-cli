from enum import Enum

class SuperEnum(Enum):
    @classmethod
    def keys(cls):
        return [e.name for e in cls]
    
    @classmethod
    def values(cls):
        return [e.value for e in cls]
    
    @classmethod
    def items(cls):
        return [(e.name, e.value) for e in cls]
    
    @classmethod
    def to_dict(cls):
        return {e.name: e.value for e in cls}

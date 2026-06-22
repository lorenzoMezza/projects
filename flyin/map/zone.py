from dataclasses import dataclass, field
from enum import Enum

class Zone_type(Enum):
    NORMAL = "normal"
    BLOCKED = "blocked"
    RESTRICTED = "restricted"
    PRIORITY = "priority"

    @property
    def move_cost(self) -> int:
        return {
            Zone_type.NORMAL: 1,
            Zone_type.RESTRICTED: 2,
            Zone_type.PRIORITY: 1,
            Zone_type.BLOCKED: 0,  # non attraversabile, gestito a parte
        }[self]


@dataclass
class Connection:
    zone_a: str
    zone_b: str
    max_link_capacity: int = 1
    current_usage: int = 0  

@dataclass
class Zone:
    name: str
    x: int
    y: int
    zone_type: Zone_type = Zone_type.NORMAL
    color: str | None = None
    max_drones: int = 1
    is_start: bool = False
    is_end: bool = False
    connections: dict[str, "Connection"] = field(default_factory=dict)
    # stato mutabile della simulazione, separato dal grafo statico
    current_occupants: set[int] = field(default_factory=set)




from zone import Zone, Zone_type, Connection


class Map_graph:
    def __init__(self) -> None:
        self.zones: dict[str, Zone] = {}
        self.connections: list[Connection] = []
        self.start: Zone | None = None
        self.end: Zone | None = None

    def add_zone(self, zone: Zone) -> None:
        pass
    
    def add_connection(self, conn: Connection) -> None:
        pass

    def neighbors(self, zone_name: str) -> dict[str, "Connection"]:
        return self.zones[zone_name].connections
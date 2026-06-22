from map_graph import Map_graph
from zone import Zone

class MapParser:
    def __init__(self, map_path: str) -> None:
        self.map_path = map_path

    def get_map_graph(self, map_path: str | None = None) -> MapGraph:
        path = map_path if map_path is not None else self.map_path

        try:
            with open(path, "r", encoding="utf-8") as file:
                lines = file.readlines()
        except FileNotFoundError as exc:
            raise FileNotFoundError(f"Not found: {path}") from exc
        except PermissionError as exc:
            raise PermissionError(f"Insufficent permissions: {path}") from exc
        except OSError as exc:
            raise OSError(f"I/O error {path}: {exc}") from exc
        self.map_grapth = Map_graph()
        return self.__parse_lines(lines)

    def __parse_lines(self, lines: list[str]) -> MapGraph:
        for line_num, line in enumerate(lines, start=1):
            key_args = line.split(":", 1)

            if len(key_args) != 2:
                raise ValueError(f"invalid line: n*{line_num} -> {line}")

            key = key_args[0].lower().strip()
            args = key_args[1].strip().split(maxsplit=3)

            match key:
                case "start_hub" | "end_hub":
                    if len(args) < 3 or len(args) > 4:
                        raise ValueError(
                            f"invalid line: n*{line_num} -> {line}"
                        )

                    name = args[0]

                    try:
                        x = int(args[1])
                        y = int(args[2])
                    except ValueError:
                        raise ValueError(
                            f"invalid x/y position: n*{line_num} -> {line}"
                        )

                    color = None

                    if len(args) == 4:
                        option = args[3]

                        if not (
                            option.startswith("[color=")
                            and option.endswith("]")
                        ):
                            raise ValueError(
                                f"invalid color: n*{line_num} -> {line}"
                            )

                        color = option[len("[color="):-1]

                    zone = Zone(
                        name=name,
                        x=x,
                        y=y,
                        color=color,
                        is_start=(key == "start_hub"),
                        is_end=(key == "end_hub"),
                    )

                    if key == "start_hub":
                        self.map_graph.start = zone
                    else:
                        self.map_graph.end = zone
                case "hub":
                    args = key_args[1].strip().split(maxsplit=3)
                    
                    
                        




        
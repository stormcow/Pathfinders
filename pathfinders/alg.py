from functools import reduce

from pathfinders.color_print import print_color_chars
from pathfinders.input import PointsList
from pathfinders.point import Point, PointData


class Algorithm:
    def __init__(self, input_list: PointsList) -> None:
        self.points = input_list
        self.path_closed: list[Point] = []
        self.path_open: list[Point] = self.get_points(point=self.points.start_point)
        self.path_final: list[PointData] = []

    def get_points(self, point: PointData) -> list[Point]:
        return sorted(
            filter(
                lambda x: x not in self.path_closed and not x.data.is_wall,
                self.points.get_neighbors(point=point),
            ),
            key=lambda x: x.h_value,
            reverse=True,
        )

    def calculate_path(self, point: Point | None = None) -> None:
        while True:
            if len(self.path_open) == 0:
                print("Points exhausted")
                return
            point = self.path_open.pop()
            self.path_closed.append(point)
            self.path_final.append(
                PointData(x=point.data.x, y=point.data.y, is_path=True)
            )
            if point.data == self.points.end_point:
                print("END")
                return
            self.path_open.extend(
                list(
                    filter(
                        lambda x: x not in self.path_open and x != point,
                        self.get_points(point=point.data),
                    )
                )
            )
            self.path_open.sort(key=lambda x: x.h_value, reverse=True)

    def print_final(self) -> None:
        points: list[PointData] = reduce(
            lambda acc, point: [*acc, point]
            if point not in self.path_final
            else [*acc, PointData(x=point.x, y=point.y, is_path=True)],
            self.points.points_list,
            [],
        )
        self.points.points_list = points
        print_color_chars(
            text=str(self.points),
            definition_of_colors={"*": "blue", "S": "green", "E": "red", "#":"black","-":"yellow"},
        )

    def __repr__(self) -> str:
        return f"""
    {self.points} : LIST OF POINT
    {self.path_closed} : EXPLORED POINTS
    {self.path_open} : POINTS TO BE EXPLORED
    {self.path_final} : FINAL PATH
    """

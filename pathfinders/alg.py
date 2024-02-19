from typing import TYPE_CHECKING

from pathfinders.input import PointsList

if TYPE_CHECKING:
    from pathfinders.point import Point


class Algorithm:
    def __init__(self, input_list: PointsList) -> None:
        self.points = input_list
        self.path_final: list[Point] = []
        self.path_open: list[Point] = []
        self.path_closed: list[Point] = []
        
    def calculate_path(self) -> None:
        

import dataclasses
import math
from typing import Iterator


@dataclasses.dataclass
class PointData:
    x: int
    y: int
    is_wall: bool = False

    def __iter__(self) -> Iterator[int]:
        return iter([self.x, self.y])


class Point:
    def __init__(
        self, self_point: PointData, f_point: PointData, g_point: PointData
    ) -> None:
        self.data = self_point
        self.f_distance = self.calculate_distance(self.data, f_point)
        self.g_distance = self.calculate_distance(self.data, g_point)
        self.h_value = self.f_distance + self.g_distance

    @staticmethod
    def calculate_distance(from_p: PointData, to_p: PointData) -> float:
        return math.dist(from_p, to_p)

    def __repr__(self) -> str:
        return f"""
    Inner data: {self.data}
    Start distance: {self.f_distance:.2f}
    End distance: {self.g_distance:.2f}
    Herustic value: {self.h_value:.2f}
    """

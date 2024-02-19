import random

from pathfinders.point import PointData


class PointsList:
    WIDTH = 20

    def __init__(self, points: list[PointData] | None = None) -> None:
        if not points:
            self.points_list = [
                PointData(x, y, is_wall=random.random() < 0.1)
                for x in range(0, self.WIDTH)
                for y in range(0, self.WIDTH)
            ]
        else:
            self.points_list = points
        self.start_point = random.choice(
            list(filter(lambda x: x.is_wall is False, self.points_list))
        )
        self.end_point = random.choice(
            list(filter(lambda x: x.is_wall is False, self.points_list))
        )

    def get_neighbors(self, point: PointData) -> list[PointData]:
        list_to_return = list(
            filter(
                lambda temp: temp.x in range(point.x - 1, point.x + 1)
                and temp.y in range(point.y - 1 and point.y + 1),
                self.points_list,
            )
        )
        return list_to_return

    def __repr__(self) -> str:
        points = ""
        for point in self.points_list:
            if point.is_wall:
                points += "W"
            elif point == self.start_point:
                points += "S"
            elif point == self.end_point:
                points += "E"
            else:
                points += "-"
        points = "\n".join(
            points[i : i + self.WIDTH] for i in range(0, len(points), self.WIDTH)
        )
        return f"""
Start point: {self.start_point}
End point: {self.end_point}
Points:\n
{points}
    """

import random

from pathfinders.point import Point, PointData


class PointsList:
    WIDTH = 30
    OBSTACLE_CHANCE = 0.5

    def __init__(
        self,
        points: list[PointData] | None = None,
        start: PointData | None = None,
        end: PointData | None = None,
    ) -> None:
        if not points:
            self.points_list = [
                PointData(x, y, is_wall=random.random() < self.OBSTACLE_CHANCE)
                for x in range(0, self.WIDTH)
                for y in range(0, self.WIDTH)
            ]
            self.start_point = random.choice(
                list(filter(lambda x: x.is_wall is False, self.points_list))
            )
            self.end_point = random.choice(
                list(
                    filter(
                        lambda x: x.is_wall is False and x != self.start_point,
                        self.points_list,
                    )
                )
            )
        elif points and start and end:
            self.points_list = points
            self.start_point = start
            self.end_point = end

    def get_neighbors(self, point: PointData) -> list[Point]:
        return [
            Point(self_point=x, f_point=self.start_point, g_point=self.end_point)
            for x in filter(
                lambda temp: temp.x in range(point.x - 1, point.x + 2)
                and temp.y in range(point.y - 1, point.y + 2)
                and temp != point,
                self.points_list,
            )
        ]

    def __repr__(self) -> str:
        points = ""
        for point in self.points_list:
            if point.is_wall:
                points += "#"
            elif point == self.start_point:
                points += "S"
            elif point == self.end_point:
                points += "E"
            elif point.is_path:
                points += "*"
            else:
                points += "-"
        points = "\n".join(
            points[i : i + self.WIDTH] for i in range(0, len(points), self.WIDTH)
        )

        return f"""{points}
    """

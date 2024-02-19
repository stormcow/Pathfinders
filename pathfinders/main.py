from pathfinders.input import PointsList
from pathfinders.point import PointData

if __name__ == "__main__":
    points = PointsList()
    print(points)
    new_points = PointsList(points=points.get_neighbors(PointData(0, 3)))
    print(new_points)

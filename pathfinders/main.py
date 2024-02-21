from pathfinders.alg import Algorithm
from pathfinders.input import PointsList

if __name__ == "__main__":
    points = PointsList()
    alg = Algorithm(points)
    alg.calculate_path()
    print(points.start_point)
    print(points.end_point)
    alg.print_final()

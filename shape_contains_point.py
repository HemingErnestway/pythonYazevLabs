import numpy as np


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


class RadiusError(Exception):
    pass


def circle_contains_point(p: Point, o: Point, r: float) -> bool:
    if (o.x - p.x) ** 2 + (o.y - p.y) ** 2 <= r ** 2:
        return True
    return False


def triangle_contains_point(p: Point, a: Point, b: Point, c: Point) -> bool:
    vect_prod_a = (a.x - p.x) * (b.y - a.y) - (b.x - a.x) * (a.y - p.y)
    vect_prod_b = (b.x - p.x) * (c.y - b.y) - (c.x - b.x) * (b.y - p.y)
    vect_prod_c = (c.x - p.x) * (a.y - c.y) - (a.x - c.x) * (c.y - p.y)
    if vect_prod_a >= 0 and vect_prod_b >= 0 and vect_prod_c >= 0 or \
            vect_prod_a <= 0 and vect_prod_b <= 0 and vect_prod_c <= 0:
        return True
    return False


def shape_contains_point(p: Point, r: float) -> bool:
    if r <= 0:
        raise RadiusError("Non-positive value of radius:", r)

    d1, d2 = False, False

    if p.x <= 0 and p.y >= 0:
        d1 = circle_contains_point(p, Point(0, 0), r)
    d2 = triangle_contains_point(p, Point(r / 2, -r), Point(r, 0), Point(0, 0))

    d = d1 or d2
    return d


def log_shape_contains_point(p: Point, r: float) -> None:
    status, negation = ("✅", "") if shape_contains_point(p, r) else ("❌", " NOT")
    print(f"{status} Shape (R={r}) DOES{negation} contain a point ({p.x:.3}, {p.y:.3})")


def generate_coordinates(amount: int, r: float) -> list[Point]:
    np.random.seed()
    points = []
    for n in range(amount):
        x, y = np.random.uniform(-r - (1 / 30) * r, r + (1 / 30) * r, 2)
        points.append(Point(x, y))
    return points


def check_generated_points(points: list[Point], r: float) -> list[bool]:
    return [shape_contains_point(p, r) for p in points]


def log_check_generated_points(points: list[Point], r: float) -> None:
    for p in points:
        log_shape_contains_point(p, r)

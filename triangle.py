from enum import Enum


class Triangle(Enum):
    Scalene = 'Scalene'
    Isosceles = 'Isosceles'
    Equilateral = 'Equilateral'


def triangle(a: int, b: int, c: int) -> Triangle:
    sorted_value = sorted([a, b, c])
    if sorted_value[0] + sorted_value[1] <= sorted_value[2]:
        raise ValueError("Not a proper triangle")

    if a == b and b == c:
        return Triangle.Equilateral

    if a == b:
        return Triangle.Isosceles
    if b == c:
        return Triangle.Isosceles
    if c == a:
        return Triangle.Isosceles

    return Triangle.Scalene

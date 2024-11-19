from enum import Enum

class Triangle(Enum):
    Scalene = 'Scalene'
    Isosceles = 'Isosceles'
    Equilateral = 'Equilateral'

def triangle(a: int, b: int, c:int) -> Triangle:
    """
    This implementation fails because the Equilaterals are recognised
    as Isosceles
    """
    if a == b:
        return Triangle.Isosceles
    if b == c:
        return Triangle.Isosceles
    if c == a:
        return Triangle.Isosceles

    if a == b and b == c:
        return Triangle.Equilateral

    return Triangle.Scalene
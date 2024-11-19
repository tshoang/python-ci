import pytest

from triangle import triangle, Triangle


def test_valid_triangle() -> None:
    assert triangle(2, 3, 4) == Triangle.Scalene

    assert triangle(3, 3, 4) == Triangle.Isosceles
    assert triangle(4, 3, 3) == Triangle.Isosceles
    assert triangle(3, 4, 3) == Triangle.Isosceles

    assert triangle(2, 2, 2) == Triangle.Equilateral


def test_invalid_triangle() -> None:
    with pytest.raises(ValueError):
        triangle(0, 3, 3)
    with pytest.raises(ValueError):
        triangle(3, 0, 3)
    with pytest.raises(ValueError):
        triangle(3, 3, 0)
    with pytest.raises(ValueError):
        triangle(-1, 3, 3)
    with pytest.raises(ValueError):
        triangle(3, -1, 3)
    with pytest.raises(ValueError):
        triangle(3, 3, -1)
    with pytest.raises(ValueError):
        triangle(4, 2, 2)
    with pytest.raises(ValueError):
        triangle(2, 4, 2)
    with pytest.raises(ValueError):
        triangle(2, 2, 4)

    with pytest.raises(ValueError):
        triangle(5, 2, 2)
    with pytest.raises(ValueError):
        triangle(2, 5, 2)
    with pytest.raises(ValueError):
        triangle(2, 2, 5)

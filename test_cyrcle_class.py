import pytest
import math
from geo_fig import Cyrcle, Square, Rectangle, Triangle


@pytest.mark.parametrize("a", [3])
def test_cyrcle_has_attr_name(a):
    cyr = Cyrcle(a)
    assert cyr.name == 'Cyrcle', 'Name is incorrect!'


@pytest.mark.parametrize("a", [3, 6, 10])
def test_cyrcle_get_area(a):
    cyr = Cyrcle(a)
    assert cyr.get_area() == round(math.pi * a**2, 3) , 'Area is incorrect!'


@pytest.mark.parametrize("a", [3])
def test_cyrcle_get_angles(a):
    cyr = Cyrcle(a)
    assert cyr.get_angles() == 0, 'Count of angles is incorrect!'


@pytest.mark.parametrize("a", [1, 4, 10])
def test_cyrcle_get_perimeter(a):
    cyr = Cyrcle(a)
    assert cyr.get_perimeter() == 2 * math.pi * a


@pytest.mark.parametrize("a", [2])
@pytest.mark.parametrize("fig_obj", ['Square', 'Rectangle', 'Cyrcle', 'Triangle'])

def test_cyrcle_add_square(a, fig_obj):
    cyr = Cyrcle(a)
    if fig_obj == 'Square':
        fig = Square(5)
        assert cyr.add_square(fig) == round(cyr.get_area() + fig.get_area(), 3), \
            'Cannot calculate square of figures: cyrcle & square!'
    elif fig_obj == 'Rectangle':
        fig = Rectangle(5, 3)
        assert cyr.add_square(fig) == round(cyr.get_area() + fig.get_area(), 3), \
            'Cannot calculate square of figures: cyrcle & rectangle!'
    elif fig_obj == 'Cyrcle':
        fig = Cyrcle(4)
        assert cyr.add_square(fig) == round(cyr.get_area() + fig.get_area(), 3), \
            'Cannot calculate square of figures: cyrcle & cyrcle!'
    elif fig_obj == 'Triangle':
        fig = Triangle(3,5,7)
        assert cyr.add_square(fig) == round(cyr.get_area()+fig.get_area(), 3), \
            'Cannot calculate square of figures: cyrcle & triangle!'


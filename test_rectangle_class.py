import pytest
from geo_fig import Rectangle, Triangle, Square, Cyrcle


@pytest.mark.parametrize("a,b", [(3,2)])
def test_rect_has_attr_name(a, b):
    rect = Rectangle(a, b)
    assert rect.name == 'Rectangle', 'Name is incorrect!'


@pytest.mark.parametrize("a,b", [(3,2), (6,7), (10,18)])
def test_rect_get_area(a, b):
    rect = Rectangle(a, b)
    assert rect.get_area() == a * b, 'Area is incorrect!'


@pytest.mark.parametrize("a,b", [(3,2)])
def test_rect_get_angles(a, b):
    rect = Rectangle(a, b)
    assert rect.get_angles() == 4, 'Count of angles is incorrect!'


@pytest.mark.parametrize("a, b", [(1,2), (4, 5), (10, 15)])
def test_rect_get_perimeter(a, b):
    rect = Rectangle(a ,b)
    assert rect.get_perimeter() == (a+b)*2


@pytest.mark.parametrize("a, b", [(2, 3), (6, 9), (100, 215)])
@pytest.mark.parametrize("fig_obj", ['Square', 'Rectangle', 'Cyrcle', 'Triangle'])
def test_rect_add_square(a, b, fig_obj):
    rect = Rectangle(a, b)
    if fig_obj == 'Square':
        fig = Square(5)
        assert rect.add_square(fig) == a*b + fig.get_area(),'Cannot calculate square of figures: rectangle & square!'
    elif fig_obj == 'Rectangle':
        fig = Rectangle(5, 3)
        assert rect.add_square(fig) == a*b + fig.get_area(),'Cannot calculate square of figures: rectangle & rectangle!'
    elif fig_obj == 'Cyrcle':
        fig = Cyrcle(4)
        assert rect.add_square(fig) == a*b + fig.get_area(),'Cannot calculate square of figures: rectangle & cyrcle!'
    elif fig_obj == 'Triangle':
        fig = Triangle(3,5,7)
        assert rect.add_square(fig) == a*b + fig.get_area(),'Cannot calculate square of figures: rectangle & triangle!'


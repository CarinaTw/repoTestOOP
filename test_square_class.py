import pytest
from geo_fig import Square, Rectangle, Triangle, Cyrcle


@pytest.mark.parametrize("a", [3])
def test_square_has_attr_name(a):
    sq = Square(a)
    assert sq.name == 'Square', 'Name is incorrect!'


@pytest.mark.parametrize("a", [3, 6, 10])
def test_square_get_area(a):
    sq = Square(a)
    assert sq.get_area() == a * a, 'Area is incorrect!'


@pytest.mark.parametrize("a", [3])
def test_square_get_angles(a):
    sq = Square(a)
    assert sq.get_angles() == 4, 'Count of angles is incorrect!'


@pytest.mark.parametrize("a", [1, 4, 10])
def test_square_get_perimeter(a):
    sq = Square(a)
    assert sq.get_perimeter() == (a*2)*2


@pytest.mark.parametrize("a", [2, 6, 100])
@pytest.mark.parametrize("fig_obj", ['Square', 'Rectangle', 'Cyrcle', 'Triangle'])
def test_square_add_square(a, fig_obj):
    sq = Square(a)
    if fig_obj == 'Square':
        fig = Square(5)
        assert sq.add_square(fig) == a**2 + fig.get_area(),'Cannot calculate square of figures: square & square!'
    elif fig_obj == 'Rectangle':
        fig = Rectangle(5, 3)
        assert sq.add_square(fig) == a**2 + fig.get_area(),'Cannot calculate square of figures: square & rectangle!'
    elif fig_obj == 'Cyrcle':
        fig = Cyrcle(4)
        assert sq.add_square(fig) == a**2 + fig.get_area(),'Cannot calculate square of figures: square & cyrcle!'
    elif fig_obj == 'Triangle':
        fig = Triangle(3,5,7)
        assert sq.add_square(fig) == a**2 + fig.get_area(),'Cannot calculate square of figures: square & triangle!'


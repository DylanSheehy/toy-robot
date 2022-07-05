import pytest

from src.point import Point

@pytest.fixture
def mock_point():
    mock_point = Point(2,4)
    return mock_point

def test_add_function(mock_point):
    result = mock_point.add(Point(1,2))
    assert result.x == 3
    assert result.y == 6

def test_greater_than_function_true_outcome(mock_point):
    assert mock_point.greater_than(Point(1,2))

def test_greater_than_function_false_outcome(mock_point):
    assert not mock_point.greater_than(Point(3,4))

def test_less_than_function_true_outcome(mock_point):
    assert mock_point.less_than(Point(3,4))

def test_less_than_function_false_outcome(mock_point):
    assert not mock_point.less_than(Point(1,2))
import pytest

from src.table import Table
from src.point import Point

@pytest.fixture
def mock_table():
    mock_table = Table(Point(0,0),Point(3,3))
    return mock_table

def test_on_table_true(mock_table):
    p1 = Point(1,2)
    assert mock_table.on_table(p1)
    p2 = Point(2,3)
    assert mock_table.on_table(p2)

def test_on_table_fasle(mock_table):
    p1 = Point(-1,2)
    assert not mock_table.on_table(p1)
    p2 = Point(1,4)
    assert not mock_table.on_table(p2)
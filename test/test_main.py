import pytest
import os

from src.main import run

test_file = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'test_data.txt'
)

class DummyArguments:
    def __init__(self):
        self.file = test_file

def test_main_function_call(capsys):
    run(DummyArguments())
    captured = capsys.readouterr()
    assert captured.out == "I am currently at (3,3) facing NORTH\n"

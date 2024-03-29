from pollster_class import Pollster
import pytest


def test_correct_input():
    yougov: Pollster = Pollster("391")
    assert yougov.get_rating() == "2.9"
    assert Pollster("253").get_rating() == "2.5"


def test_incorrect_input():
    with pytest.raises(ValueError):
        fake: Pollster = Pollster("10000")
        fake.get_rating()

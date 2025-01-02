import pytest
from working import convert


def test_valid1():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"


    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


    assert convert("5:00 PM to 9:00 AM") == "17:00 to 09:00"


def test_invalid():
    with pytest.raises(ValueError):
        convert("9:00 AM to 25:00 PM")


def test_invalidd():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")


def test_invaliddd():
    with pytest.raises(ValueError):
        convert("9:00 to 5:00 PM")


def test_invalidddd():
    with pytest.raises(ValueError):
        convert("9:00 AM to 5:00 PM to 7:00 PM")


def test_invalid5():
    with pytest.raises(ValueError):
        convert("5:00 PM to 9:00")

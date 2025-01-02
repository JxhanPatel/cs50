from numb3rs import validate

def test_wrong_char():
    assert validate("10.168.0.A") == False
    assert validate("192.168.0.@") == False
    assert validate("512.168.0.%") == False

def test_invalid():
    assert validate("256.0.0.1") == False
    assert validate("hui") == False
    assert validate("10.433.0.1.1") == False


def test_valid():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("1.2.3.4") == True
    assert validate("11.99.22.88") == True


def test_range():
    assert validate("300.0.0.1") == False
    assert validate("5555.300.0.1") == False
    assert validate("222.168.300.1") == False

from plates import is_valid


def test_twoletters():
    assert is_valid("HU") == True
    assert is_valid("50") == False
    assert is_valid("C5") == False
    assert is_valid("5") == False


def test_len():
    assert is_valid("HICS50") == True
    assert is_valid("CS") == True
    assert is_valid("HELLOCS50") == False


def test_num():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("AAA022") == False


def test_punct():
    assert is_valid("CS50!") == False

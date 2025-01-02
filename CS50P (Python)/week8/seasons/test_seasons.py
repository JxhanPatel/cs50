import seasons


def test_convert():
    assert seasons.convert(365) == "Five hundred twenty-five thousand, six hundred minutes"
    assert seasons.convert(1) == "One thousand, four hundred forty minutes"


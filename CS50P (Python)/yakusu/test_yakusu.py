import project

# Test KANJI
def test_search_kanji():
    result = project.search_kanji('river')
    assert result == '川'

def test_no_kanji():
    result = project.search_kanji('xyz')
    assert result == 'Oh no! No Kanji found!'



# Test ROMAJI
def test_to_romaji():
    result = project.to_romaji('川')
    assert result == 'kawa'



# Test HIRAGANA
def test_to_hiragana():
    result = project.to_hiragana('nichi')
    assert result == 'にち'


# Test ENGLISH
def test_to_english():
    result = project.to_english('こんにちは')
    assert result == 'Hello'

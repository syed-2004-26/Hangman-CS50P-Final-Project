from project import word_match, indices, word_picker

def test_word_match():
    # Test correct guesses
    assert word_match("A", "APPLE") == True
    assert word_match("P", "APPLE") == True
    # Test incorrect guesses
    assert word_match("Z", "APPLE") == False
    # Test case sensitivity (though your main() handles .upper(), it's good to check logic)
    assert word_match("a", "APPLE") == False

def test_indices():
    # Test single occurrence
    assert indices("A", "APPLE") == [0]
    # Test multiple occurrences
    assert indices("P", "APPLE") == [1, 2]
    # Test no occurrences
    assert indices("Z", "APPLE") == []

def test_word_picker():
    # Test that it picks a word from a provided list
    sample_words = ["PYTHON", "CS50", "PROGRAMMING"]
    picked = word_picker(sample_words)
    assert picked in ["PYTHON", "CS50", "PROGRAMMING"]
    # Test that it returns the word in uppercase
    assert picked.isupper() == True

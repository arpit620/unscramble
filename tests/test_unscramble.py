import pytest
from unscramble import Unscramble
from collections import defaultdict

# a = Unscramble("search")
# b = a.find_words()

# print(b[5])

# Fixture yet to figure out
@pytest.fixture
def unscramble():
	words = Unscramble("Hello")
	return words

def test_load_dictionary():
	words = Unscramble("Search")
	dictionary = words._load_dictionary()
	assert isinstance(dictionary, list), "Dictionary not a list"
	assert len(dictionary) > 1, "Dictionary is less than 100"

def test_get_word_lenghts():
	words = Unscramble("Search")
	word_lengths = words._get_word_lengths(upto=4)
	assert word_lengths == [6,5,4], "Word length not matching"

def test_create_permutations():
	words = Unscramble("Search")
	word_permutations = words._create_permutations(upto=4)
	assert isinstance(word_permutations, list), "Not a list"
	assert len(word_permutations) > 1700

	total = words._total_permutations(word_permutations)
	assert total == 1800, "Permutations not 1800"

def test_get_defaultdict():
	words = Unscramble("Hello")
	sample_words = ["Hello", "World", "This", "is", "random", "string"]
	dictionary = words._get_defaultdict(sample_words)
	assert isinstance(dictionary, defaultdict), (
			"Defaultdict not returned")

def test_find_words():
	words = Unscramble("Hello")
	dict_words = words.find_words()
	assert len(dict_words[5])==1
	assert len(dict_words[4])==3
	assert len(dict_words[3])==0





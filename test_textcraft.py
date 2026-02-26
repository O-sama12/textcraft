import pytest
from textcraft import (
    to_lowercase, to_uppercase, to_snake_case, to_camel_case,
    to_kebab_case, remove_punctuation, normalize_spaces,
    word_count, char_count, sentence_count, slugify
)

# ── All functions to test ──────────────────────────────────
FUNCTIONS_SINGLE_ARG = [
    to_lowercase, to_uppercase, to_snake_case, to_camel_case,
    to_kebab_case, remove_punctuation, normalize_spaces,
    word_count, sentence_count, slugify
]

# ── Test invalid inputs raise TypeError ───────────────────
@pytest.mark.parametrize("func", FUNCTIONS_SINGLE_ARG)
@pytest.mark.parametrize("invalid_input", [
    None, 123, 3.14, ["hello"], {"key": "value"}, True
])
def test_raises_type_error_for_invalid_input(func, invalid_input):
    with pytest.raises(TypeError):
        func(invalid_input)

# ── char_count has extra param so test separately ─────────
@pytest.mark.parametrize("invalid_input", [
    None, 123, 3.14, ["hello"], {"key": "value"}, True
])
def test_char_count_raises_type_error(invalid_input):
    with pytest.raises(TypeError):
        char_count(invalid_input)

# ── Test valid string inputs still work correctly ─────────
def test_to_lowercase_valid():
    assert to_lowercase("HELLO") == "hello"

def test_to_lowercase_invalid():
    with pytest.raises(TypeError):
        to_lowercase(5)

def test_to_uppercase_valid():
    assert to_uppercase("hello") == "HELLO"

def test_to_snake_case_valid():
    assert to_snake_case("hello world") == "hello_world"

def test_to_camel_case_valid():
    assert to_camel_case("hello world") == "helloWorld"

def test_to_kebab_case_valid():
    assert to_kebab_case("hello world") == "hello-world"

def test_remove_punctuation_valid():
    assert remove_punctuation("hello!") == "hello"

def test_normalize_spaces_valid():
    assert normalize_spaces("hello   world") == "hello world"

def test_word_count_valid():
    assert word_count("hello world") == 2

def test_char_count_valid():
    assert char_count("hello") == 5

def test_sentence_count_valid():
    assert sentence_count("Hello. World.") == 2

def test_slugify_valid():
    assert slugify("Hello World") == "hello-world"

# ── Test empty string still works ─────────────────────────
@pytest.mark.parametrize("func", FUNCTIONS_SINGLE_ARG)
def test_empty_string_does_not_raise(func):
    try:
        func("")
    except TypeError:
        pytest.fail(f"{func.__name__} raised TypeError on empty string")
import textcraft

def text_case_conversion():
    assert textcraft.to_lowercase("Hello World!") == "hello world!"
    assert textcraft.to_uppercase("Hello World!") == "HELLO WORLD!"
    assert textcraft.to_snake_case("Hello World Test") == "hello_world_test"
    assert textcraft.to_camel_case("hello world test") == "helloWorldTest"
    assert textcraft.to_kebab_case("Hello World Test") == "hello-world-test"

def test_cleaning():
    assert textcraft.remove_punctuation("Hello, World!") == "Hello World"
    assert textcraft.normalize_spaces("Hello    World   Test") == "Hello World Test"

def test_stats():
    assert textcraft.word_count("Hello World Test") == 3
    assert textcraft.char_count("Hello") == 5
    assert textcraft.sentence_count("Hello world. This is a test!") == 2

def test_slugify():
    assert textcraft.slugify("Hello World! This is a Test.") == "hello-world-this-is-a-test"

def test_edge_cases_empty_string():
    """Test all functions with empty string input."""
    assert textcraft.to_lowercase("") == ""
    assert textcraft.to_uppercase("") == ""
    assert textcraft.to_snake_case("") == ""
    assert textcraft.to_camel_case("") == ""
    assert textcraft.to_kebab_case("") == ""
    assert textcraft.remove_punctuation("") == ""
    assert textcraft.normalize_spaces("") == ""
    assert textcraft.word_count("") == 0
    assert textcraft.char_count("") == 0
    assert textcraft.sentence_count("") == 0
    assert textcraft.slugify("") == ""

def test_edge_cases_numbers():
    """Test all functions with numeric-only input."""
    assert textcraft.to_lowercase("123") == "123"
    assert textcraft.to_uppercase("123") == "123"
    assert textcraft.to_snake_case("123") == "123"
    assert textcraft.to_camel_case("123") == "123"
    assert textcraft.to_kebab_case("123") == "123"
    assert textcraft.word_count("123") == 1
    assert textcraft.char_count("123") == 3

def test_edge_cases_special_characters():
    """Test functions with special characters."""
    assert textcraft.to_lowercase("Hello@World!") == "hello@world!"
    assert textcraft.remove_punctuation("Hello@World!") == "HelloWorld"
    assert textcraft.slugify("Hello@World!") == "helloworld"

def test_edge_cases_whitespace():
    """Test functions with whitespace-only input."""
    assert textcraft.to_camel_case("   ") == ""
    assert textcraft.normalize_spaces("   ") == ""
    assert textcraft.word_count("   ") == 0
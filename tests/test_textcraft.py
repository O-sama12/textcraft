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
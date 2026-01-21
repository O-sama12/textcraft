import textcraft
import pytest

def test_text_case_conversion():
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

def test_empty_string():
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

def test_special_chars_case_convertion():
    assert textcraft.to_lowercase("t3$T./'_-&%®#") == "t3$t./'_-&%®#", (
        "Case for function to_lowercase, failed")
    assert textcraft.to_uppercase("t3$T./'_-&%®#") == "T3$T./'_-&%®#", (
        "Case for function to_uppercase, failed")

def test_special_chars_snake_case():
    assert textcraft.to_snake_case("t3$t./' -&%®#") != "t3$t./'_-&%®#", (
        "Case for function to_snake_case, failed")

def test_special_chars_camel_case():
    assert textcraft.to_camel_case("t3$T./'_-&%®#") == "t3$T./'_-&%®#", (
        "Case for function to_camel_case, failed")

def test_special_chars_kebab_case():
    assert textcraft.to_kebab_case("t3$-t./'-&%®#") == "t3$-t./'-&%®#", (
        "Case for function to_kebab_case, failed")

def test_special_chars_remove_punctuation():
    assert textcraft.remove_punctuation("t3$t./'_?,!-&%@#()[]{}") == "t3t", (
        "Case for function remove_punctuation, failed")
    # ellipsis
    assert textcraft.remove_punctuation("test…") == "test", (
        "Case for function remove_punctuation, failed for ellipsis")
    # hyphen
    assert textcraft.remove_punctuation("test-") == "test", (
        "Case for function remove_punctuation, failed for hyphen")
    # en dash
    assert textcraft.remove_punctuation("test–") == "test", (
        "Case for function remove_punctuation, failed for en dash")
    # em dash
    assert textcraft.remove_punctuation("test—") == "test", (
        "Case for function remove_punctuation, failed for em dash")

def test_special_chars_normalize_spaces():
    assert textcraft.normalize_spaces("t3$t./'_-&%®#") == "t3$t./'_-&%®#", (
        "Case for function normalize_spaces, failed")

def test_special_chars_stats():
    assert textcraft.word_count("t3$t./'_-&%®#") == 1, (
        "Case for function word_count, failed")
    assert textcraft.char_count("t3$t./'_-&%®#") == 13, (
        "Case for function char_count, failed")
    
    assert textcraft.sentence_count("Case for function textcraft.sentence_count.") == 1, (
        "Second case for function sentence_count, failed")

def test_special_chars_slugify():
    assert textcraft.slugify("t3$t./'_-&%®#") == "t3t"

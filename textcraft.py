"""
textcraft.py

A lightweight python module for text transformation, cleaning and analysis

"""

__version__ = "0.1.3"

import re
import string
import unicodedata

__all__ = [
    "to_lowercase",
    "to_uppercase",
    "to_snake_case",
    "to_camel_case",
    "to_kebab_case",
    "remove_punctuation",
    "normalize_spaces",
    "word_count",
    "char_count",
    "sentence_count",
    "slugify",
]

# --------------------------
# Text casing
# --------------------------

def to_lowercase(text: str) -> str:
    """Convert text to lowercase."""
    return text.lower()

def to_uppercase(text: str) -> str:
    """Convert text to uppercase."""
    return text.upper()

def to_snake_case(text: str) -> str:
    """Convert text to snake_case."""
    if not text:
        return text
    return text.replace(" ", "_")

def to_camel_case(text: str) -> str:
    """Convert text to camelCase.

    Word boundaries (space, underscore, hyphen) between alphanumeric characters
    are removed and the following letter is capitalized. Special characters
    and non-boundary separators are preserved as-is.
    """
    if not text:
        return text

    boundaries = {' ', '_', '-'}
    result = []
    first_letter_done = False
    capitalize_next = False
    last_char_was_alnum = False

    for i, c in enumerate(text):
        if c in boundaries:
            # Look ahead past consecutive boundaries
            next_idx = i + 1
            while next_idx < len(text) and text[next_idx] in boundaries:
                next_idx += 1
            next_is_alnum = next_idx < len(text) and text[next_idx].isalnum()

            if last_char_was_alnum and next_is_alnum:
                # This is a word boundary - skip it and mark to capitalize next
                capitalize_next = True
            else:
                # Not a word boundary - preserve it
                result.append(c)
                last_char_was_alnum = False
        elif c.isalpha():
            if not first_letter_done:
                result.append(c.lower())
                first_letter_done = True
            elif capitalize_next:
                result.append(c.upper())
                capitalize_next = False
            else:
                result.append(c)
            last_char_was_alnum = True
        else:
            result.append(c)
            last_char_was_alnum = c.isalnum()

    return ''.join(result)

def to_kebab_case(text: str) -> str:
    """Convert text to kebab-case."""
    if not text or " " not in text:
        return text

    s = re.sub(r"([A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+)", 
               lambda mo: ' ' + mo.group(0).lower(), s)
    return '-'.join(re.sub(r"(\s|_|-)+", " ", s).split())

# --------------------------
# Cleaning utilities
# --------------------------

def remove_punctuation(text: str) -> str:
    return ''.join(
        ch for ch in text
        if unicodedata.category(ch)[0] not in ('P', 'S')
    )

def normalize_spaces(text: str) -> str:
    """Normalize multiple spaces to single spaces."""
    return " ".join(text.split())

# --------------------------
# Text statistics
# --------------------------

def word_count(text: str) -> int:
    """Returns number of words in text."""
    return len(text.split())

def char_count(text: str, include_spaces: bool = False) -> int:
    """Returns number of characters in text."""
    if include_spaces:
        return len(text)
    return len(text.replace(" ", ""))

def sentence_count(text: str) -> int:
    """Return number of sentences in text."""
    count = 0
    word_seen = False
    valid_word = True

    for ch in text:
        if ch.isalnum():
            word_seen = True

        elif ch in ".!?":
            if word_seen and valid_word:
                count += 1
            word_seen = False
            valid_word = True  # reset for next sentence

        elif ch.isspace():
            continue

        else:
            # symbol invalidates current word
            valid_word = False

    return count

# --------------------------
# Miscellaneous
# --------------------------

def slugify(text: str) -> str:
    """Convert text into a URL-friendly slug."""
    if not text:
        return ""
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    return re.sub(r'[\s\-_]+', '-', text).strip('-_')


    



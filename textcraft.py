"""
textcraft.py

A lightweight python module for text transformation, cleaning and analysis

"""

__version__ = "0.1.3"

import re
import string

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
    text = re.sub(r'[\s\-]+', '_', text)
    text = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', text)
    return text.lower()

def to_camel_case(text: str) -> str:
    """Convert text to camelCase."""
    words = re.split(r'[\s\-_]+', text)
    return words[0].lower() + ''.join(word.capitalize() for word in words[1:])

def to_kebab_case(text: str) -> str:
    """Convert text to kebab-case."""
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'([a-z0-9])([A-Z])', r'\1-\2', text)
    return text.lower()

# --------------------------
# Cleaning utilities
# --------------------------

def remove_punctuation(text: str) -> str:
    """Remove punctuation from text."""
    return text.translate(str.maketrans('', '', string.punctuation))

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
    return len(re.findall(r'[.!?]+', text))

# --------------------------
# Miscellaneous
# --------------------------

def slugify(text: str) -> str:
    """Convert text into a URL-friendly slug."""
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    return re.sub(r'[\s-]+', '-', text).strip('-')

    



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
    """Convert text to lowercase.
    
    Edge cases:
        - Empty string returns ""
        - Numbers and symbols are preserved
    """
    return text.lower()

def to_uppercase(text: str) -> str:
    """Convert text to uppercase.
    
    Edge cases:
        - Empty string returns ""
        - Numbers and symbols are preserved
    """
    return text.upper()

def to_snake_case(text: str) -> str:
    """Convert text to snake_case.
    
    Edge cases:
        - Empty string returns ""
        - Numbers are preserved
        - Special characters are preserved (not stripped)
    """
    text = re.sub(r'[\s\-]+', '_', text)
    text = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', text)
    return text.lower()

def to_camel_case(text: str) -> str:
    """Convert text to camelCase.
    
    Edge cases:
        - Empty string or whitespace-only returns ""
        - Numbers are preserved as-is
        - Special characters are preserved (not stripped)
    """
    words = re.split(r'[\s\-_]+', text)
    words = [w for w in words if w]  # Remove empty strings from split
    if not words:
        return ""
    return words[0].lower() + ''.join(word.capitalize() for word in words[1:])

def to_kebab_case(text: str) -> str:
    """Convert text to kebab-case.
    
    Edge cases:
        - Empty string returns ""
        - Numbers are preserved
        - Special characters are preserved (not stripped)
    """
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'([a-z0-9])([A-Z])', r'\1-\2', text)
    return text.lower()

# --------------------------
# Cleaning utilities
# --------------------------

def remove_punctuation(text: str) -> str:
    """Remove punctuation from text.
    
    Edge cases:
        - Empty string returns ""
        - Only ASCII punctuation is removed
        - Numbers are preserved
    """
    return text.translate(str.maketrans('', '', string.punctuation))

def normalize_spaces(text: str) -> str:
    """Normalize multiple spaces to single spaces.
    
    Edge cases:
        - Empty string or whitespace-only returns ""
        - Leading/trailing whitespace is trimmed
    """
    return " ".join(text.split())

# --------------------------
# Text statistics
# --------------------------

def word_count(text: str) -> int:
    """Returns number of words in text.
    
    Edge cases:
        - Empty string returns 0
        - Punctuation attached to words counts as part of the word
    """
    return len(text.split())

def char_count(text: str, include_spaces: bool = False) -> int:
    """Returns number of characters in text.
    
    Edge cases:
        - Empty string returns 0
        - Spaces are included/excluded based on flag
    """
    if include_spaces:
        return len(text)
    return len(text.replace(" ", ""))

def sentence_count(text: str) -> int:
    """Return number of sentences in text.
    
    Edge cases:
        - Empty string returns 0
        - Counts sentence-ending punctuation [.!?]
        - Symbols like '!' in middle of text count as sentence end
    """
    return len(re.findall(r'[.!?]+', text))

# --------------------------
# Miscellaneous
# --------------------------

def slugify(text: str) -> str:
    """Convert text into a URL-friendly slug.
    
    Edge cases:
        - Empty string returns ""
        - Non-ASCII characters are stripped
        - Numbers are preserved
    """
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    return re.sub(r'[\s-]+', '-', text).strip('-')

    



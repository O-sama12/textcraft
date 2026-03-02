# ✨ Textcraft

![PyPI](https://img.shields.io/pypi/v/textcraft-py)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/textcraft-py)
![CI](https://github.com/O-sama12/textcraft/actions/workflows/python-ci.yml/badge.svg)
![License](https://img.shields.io/github/license/O-sama12/textcraft)
![Build](https://github.com/O-sama12/textcraft/actions/workflows/build.yml/badge.svg)

🧵 A lightweight **Python module** for text transformation, cleaning, and basic analysis —  
beginner-friendly and open source.

---

## 📖 Overview

Textcraft is a simple Python library that provides common text manipulation functions. It's designed to be easy to use and understand, making it perfect for beginners and for quick text processing tasks.

---

## 📦 Installation

Install Textcraft using pip:

```bash
pip install textcraft-py
```

Or clone the repository:

```bash
git clone https://github.com/O-sama12/textcraft
```

then import the module directly:

```python
import textcraft
```

---

## 🚀 Getting Started

### Basic Usage

```python
import textcraft as txt

# Example text to work with
text = "Hello World! This is a TextCraft example."

# Text Case & Format Conversion
print(txt.to_lowercase(text))      # hello world! this is a textcraft example.
print(txt.to_uppercase(text))      # HELLO WORLD! THIS IS A TEXTCRAFT EXAMPLE.
print(txt.to_snake_case(text))     # hello_world!_this_is_a_textcraft_example.
print(txt.to_kebab_case(text))     # hello-world!-this-is-a-textcraft-example.
print(txt.to_camel_case(text))     # helloWorld!ThisIsATextcraftExample.

# Text Cleaning
print(txt.remove_punctuation(text))  # Hello World This is a TextCraft example
print(txt.normalize_spaces(text))    # Hello World! This is a TextCraft example.

# Text Statistics
print(txt.word_count(text))          # 8
print(txt.char_count(text))          # 43 (without spaces: 35)
print(txt.sentence_count(text))      # 1
print(txt.slugify(text))             # hello-world-this-is-a-textcraft-example
```

---

## 🚀 Features

### 🔤 Text Case & Format Conversion
- 🔡 `to_lowercase(text)` - Convert text to lowercase
- 🐫 `to_uppercase(text)` - Convert text to uppercase  
- 🐍 `to_snake_case(text)` - Transform text into `snake_case`
- 🔗 `to_kebab_case(text)` - Convert text into `kebab-case`
- 🐪 `to_camel_case(text)` - Convert text into `camelCase`

### 🧹 Text Cleaning Utilities
- 🧽 `remove_punctuation(text)` - Remove all punctuation characters from text
- 📐 `normalize_spaces(text)` - Normalize multiple spaces into a single space
- 🌐 `slugify(text)` - Generate URL-friendly slugs

### 📊 Basic Text Statistics
- 🧮 `word_count(text)` - Count number of words in text
- 🔢 `char_count(text, include_spaces=True/False)` - Count characters (with or without spaces)
- 📑 `sentence_count(text)` - Count number of sentences

---

## 🧪 Common Use Cases

### 1. Preparing text for processing
```python
raw_text = "  This   text   has   extra   spaces.  "
clean_text = txt.normalize_spaces(raw_text)  # "This text has extra spaces."
```

### 2. Creating URL-friendly strings
```python
title = "My Blog Post: An Introduction!"
slug = txt.slugify(title)  # "my-blog-post-an-introduction"
```

### 3. Formatting text for different contexts
```python
function_name = "my function name"
snake_case = txt.to_snake_case(function_name)  # "my_function_name"
kebab_case = txt.to_kebab_case(function_name)  # "my-function-name"
```

---

## 📝 Examples with Input → Output

| Function | Input | Output |
|----------|-------|--------|
| `to_lowercase()` | `"Hello World!"` | `"hello world!"` |
| `to_uppercase()` | `"Hello World!"` | `"HELLO WORLD!"` |
| `to_snake_case()` | `"Hello World"` | `"hello_world"` |
| `to_camel_case()` | `"hello world"` | `"helloWorld"` |
| `remove_punctuation()` | `"Hello, World!"` | `"Hello World"` |
| `word_count()` | `"Hello World"` | `2` |
| `slugify()` | `"Hello, World!"` | `"hello-world"` |
| `to_title_case()`| | `"Hello, World!"` | `"Hello World"` |

---

## ⚠️ Edge Cases & Notes

- Empty strings will return empty strings for most functions
- `to_camel_case()` handles various separators and converts them appropriately
- `sentence_count()` recognizes `.`, `!`, and `?` as sentence terminators
- `char_count()` can optionally include or exclude spaces
- `slugify()` removes punctuation and replaces spaces with hyphens

---

## 🤝 Contributing

This project is **beginner-friendly** and welcomes:
- 🐞 Bug reports
- 💡 Feature suggestions
- 🔧 Pull requests

Before contributing, please take a moment to read the [CONTRIBUTING.md](CONTRIBUTING.md) file.

---

## 📄 License

This project is licensed under the  
[MIT License](https://choosealicense.com/licenses/mit/).
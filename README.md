# ✨ Textcraft

![PyPI](https://img.shields.io/pypi/v/textcraft-py)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/textcraft-py)
![CI](https://github.com/O-sama12/textcraft/actions/workflows/python-ci.yml/badge.svg)
![License](https://img.shields.io/github/license/O-sama12/textcraft)
![Build](https://github.com/O-sama12/textcraft/actions/workflows/build.yml/badge.svg)

🧵 A lightweight **Python module** for text transformation, cleaning, and basic analysis —  
beginner-friendly and open source.

---

## 🚀 Features

### 🔤 Text Case & Format Conversion
- 🔡 Convert text to lowercase and uppercase
- 🐍 Transform text into `snake_case`
- 🐫 Convert text into `camelCase`
- 🔗 Convert text into `kebab-case`

### 🧹 Text Cleaning Utilities
- 🧽 Remove punctuation from text
- 📐 Normalize multiple spaces into a single space
- 🌐 Generate URL-friendly slugs using `slugify`

### 📊 Basic Text Statistics
- 🧮 Count number of words in text
- 🔢 Count characters (with or without spaces)
- 📑 Count number of sentences

---

## 📦 Installation

Install Textcraft using pip:

```python
pip install textcraft-py
```

or 

clone the repository:

```bash
git clone https://github.com/O-sama12/textcraft
```

then import the module directly:

```python
import textcraft
```


---

## 🧪 Usage / Examples

Basic usage of the `textcraft` module:

```python
import textcraft as txt

text = "This is a textcraft example"

print(txt.to_lowercase(text))   # this is a textcraft example
print(txt.to_uppercase(text))   # THIS IS A TEXTCRAFT EXAMPLE
print(txt.to_snake_case(text))  # this_is_a_textcraft_example
print(txt.to_kebab_case(text))  # this-is-a-textcraft-example
print(txt.to_camel_case(text))  # thisIsATextcraftExample
```

---

## 🤝 Contributing

This project is **beginner-friendly** and welcomes:
- 🐞 Bug reports
- 💡 Feature suggestions
- 🔧 Pull requests

---

## 📄 License

This project is licensed under the  
[MIT License](https://choosealicense.com/licenses/mit/).

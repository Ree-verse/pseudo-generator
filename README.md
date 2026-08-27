# Pseudo-generator

Realistic & simple pseudo generator written in Python.

## Preview

<p><img src="https://raw.githubusercontent.com/ree-verse/pseudo-generator/main/assets/preview.png" alt="pseudo-generator preview"></a></p>

## Character probabilities

The generator is designed to produce realistic-looking pseudos by alternating vowels and consonants whenever possible.

For each character, the generator first randomly chooses between two paths with equal probability:

* **50%**: if the previous character is a consonant, a vowel is selected; if the previous character is a vowel, a consonant is selected.
* **50%**: otherwise, a character is selected from the available character sets (`a-z`, `_`/`.` and digits, depending on the configuration).

When alternation is not selected or is not possible, the fallback selection is uniformly random among the lowercase alphabet, with special characters and digits added to the options when enabled.

With the default configuration (`CHAR_NUMBER = 5`, `SPECIAL_CHARACTERS = False`, `DIGITS = False`, `UPPER_CASE = False`), the generator therefore favors alternating consonant/vowel patterns while retaining enough randomness to avoid producing strictly regular names.

## Installation

```sh
git clone https://github.com/ree-verse/pseudo-generator
cd pseudo-generator
pip install -r requirements.txt
```

## Usage

```sh
cd pseudo-generator
python src/main.py
```

## Prerequisites
- `colorama` for proper color support

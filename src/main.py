"""
pseudo-generator | https://github.com/ree-verse/pseudo-generator

Copyright © 2026 Ree-verse. All rights reserved.
Licensed under the MIT License. See LICENSE in the project root for license information.
"""

__all__ = []
__version__ = "1.0.0"
__author__ = "Ree-verse"
__license__ = "MIT"
__doc__ = "pseudo-generator - Realistic & simple pseudo generator written in Python."

import logging
import random
import string

from colorama import Fore, Style

CHAR_NUMBER = 5
CONSONANTS = "bcdfghjklmnpqrstvwxz"
DIGITS = False
MAX_SPECIAL_CHARACTERS = max(1, (CHAR_NUMBER * 2) // 5)
MAX_DIGITS = max(1, (CHAR_NUMBER * 2) // 5)
PSEUDO_NUMBER = 30
SPECIAL_CHARACTERS = False
UPPER_CASE = False
VOWELS = "aeiouy"

logging.basicConfig(level=logging.INFO, format="%(asctime)s  %(levelname)s  %(message)s")
logger = logging.getLogger("pseudo-generator")


def colorize(text: str, color: str) -> str:
    return f"{color}{text}{Style.RESET_ALL}"


def random_case(characters: str) -> str:
    char = random.choice(characters)
    return char.upper() if UPPER_CASE and random.choice([True, False]) else char


number_special_characters = 0
def random_character(previous: str, index: int = 0) -> str:
    global number_special_characters
    choice = random.randint(1, 2)
    previous = previous.lower()

    if choice == 1 and previous in CONSONANTS:
        return random_case(VOWELS)
    elif choice == 2 and previous in VOWELS:
        return random_case(CONSONANTS)
    else:
        options = [string.ascii_lowercase]
        if SPECIAL_CHARACTERS and number_special_characters < MAX_SPECIAL_CHARACTERS:
            options.append(random.choice([".", "_"]))
        if DIGITS and index >= CHAR_NUMBER - MAX_DIGITS:
            options.append(string.digits)

        character = random_case(random.choice(options))
        if character in "._":
            number_special_characters += 1
        return character


print(colorize(
r"""
__________                       .___                                                         __
\______   \______ ____  __ __  __| _/____             ____   ____   ____   ________________ _/  |_  ___________
 |     ___/  ___// __ \|  |  \/ __ |/  _ \   ______  / ___\_/ __ \ /    \_/ __ \_  __ \__  \\   __\/  _ \_  __ \
 |    |   \___ \\  ___/|  |  / /_/ (  <_> ) /_____/ / /_/  >  ___/|   |  \  ___/|  | \// __ \|  | (  <_> )  | \/
 |____|  /____  >\___  >____/\____ |\____/          \___  / \___  >___|  /\___  >__|  (____  /__|  \____/|__|
              \/     \/           \/               /_____/      \/     \/     \/           \/
        made by ree-verse, v1.0.0

----------------------------------------------------------------------------------------------------------------
""", Fore.MAGENTA
))

for _ in range(PSEUDO_NUMBER):
    previous_letter = ""
    number_special_characters = 0
    # pseudo = [random_character(previous_letter, i) for i in range(CHAR_NUMBER)]
    pseudo = []
    for i in range(CHAR_NUMBER):
        character = random_character(previous_letter, i)
        pseudo.append(character)
        previous_letter = character
    logger.info(colorize(f"Pseudo: '{''.join(pseudo)}'", Fore.GREEN))

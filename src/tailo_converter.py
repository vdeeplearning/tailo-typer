"""Tai-lo tone-number converter.

Converts Taiwanese Hokkien Tai-lo written with tone numbers into
tone-marked Tai-lo.

Example:
    Gua2 e5 tshu3-ting2 u7 niau1-a2.
    -> Guá ê tshù-tíng ū niau-á.
"""

from __future__ import annotations

import re
import sys


TONE_MARKS: dict[str, dict[str, str]] = {
    "a": {"2": "á", "3": "à", "5": "â", "7": "ā", "8": "a̍"},
    "e": {"2": "é", "3": "è", "5": "ê", "7": "ē", "8": "e̍"},
    "i": {"2": "í", "3": "ì", "5": "î", "7": "ī", "8": "i̍"},
    "o": {"2": "ó", "3": "ò", "5": "ô", "7": "ō", "8": "o̍"},
    "u": {"2": "ú", "3": "ù", "5": "û", "7": "ū", "8": "u̍"},
    "m": {"2": "ḿ", "3": "m̀", "5": "m̂", "7": "m̄", "8": "m̍"},
    "n": {"2": "ń", "3": "ǹ", "5": "n̂", "7": "n̄", "8": "n̍"},
}

NO_MARK_TONES = {"1", "4"}

# Match one ASCII Tai-lo-looking syllable followed by one tone number.
# This intentionally avoids matching numbers that are not attached to letters.
TONE_NUMBER_PATTERN = re.compile(r"[A-Za-z]+[1-8]")


def preserve_case(original: str, marked: str) -> str:
    """Preserve uppercase letters when applying a tone mark."""
    if original.isupper():
        return marked.upper()
    return marked


def find_tone_target(syllable: str) -> int | None:
    """Return the index of the letter that should receive the tone mark.

    This MVP uses a simple Tai-lo-friendly heuristic:
    1. Prefer `a`
    2. Then `e`
    3. Then `oo`, marked on the first `o`
    4. Then `o`
    5. Then `i`
    6. Then `u`
    7. Then syllabic `m` or `n`

    This is intentionally isolated so the rule can be improved later.
    """
    lower = syllable.lower()

    for vowel in ("a", "e"):
        index = lower.find(vowel)
        if index != -1:
            return index

    oo_index = lower.find("oo")
    if oo_index != -1:
        return oo_index

    for vowel in ("o", "i", "u", "m", "n"):
        index = lower.find(vowel)
        if index != -1:
            return index

    return None


def apply_tone_mark(syllable: str, tone_number: str) -> str:
    """Apply one Tai-lo tone number to a syllable."""
    if tone_number in NO_MARK_TONES:
        return syllable

    target_index = find_tone_target(syllable)

    if target_index is None:
        return syllable

    original_letter = syllable[target_index]
    lower_letter = original_letter.lower()

    marked_letter = TONE_MARKS.get(lower_letter, {}).get(tone_number)

    if marked_letter is None:
        return syllable

    marked_letter = preserve_case(original_letter, marked_letter)

    return (
        syllable[:target_index]
        + marked_letter
        + syllable[target_index + 1 :]
    )


def convert_match(match: re.Match[str]) -> str:
    """Convert a regex match containing one syllable plus tone number."""
    token = match.group(0)
    syllable = token[:-1]
    tone_number = token[-1]
    return apply_tone_mark(syllable, tone_number)


def convert(text: str) -> str:
    """Convert all tone-number syllables in a string."""
    return TONE_NUMBER_PATTERN.sub(convert_match, text)


def main() -> None:
    """Run the converter from the command line."""
    if len(sys.argv) < 2:
        print("Usage: python src/tailo_converter.py \"Gua2 e5 tshu3\"")
        return

    input_text = " ".join(sys.argv[1:])
    print(convert(input_text))


if __name__ == "__main__":
    main()
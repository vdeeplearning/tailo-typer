"""Tai-lo tone-number converter.

Converts Taiwanese Hokkien Tai-lo written with tone numbers into
tone-marked Tai-lo.
"""

from __future__ import annotations

import argparse
import re
import sys


if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8")

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


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
TONE_NUMBER_PATTERN = re.compile(r"[A-Za-z]+[1-8]")


def preserve_case(original: str, marked: str) -> str:
    """Preserve uppercase letters when applying a tone mark."""
    if original.isupper():
        return marked.upper()
    return marked


def find_tone_target(syllable: str) -> int | None:
    """Return the index of the letter that should receive the tone mark."""
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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert Tai-lo tone-number input into tone-marked Tai-lo."
    )

    parser.add_argument(
        "text",
        nargs="*",
        help="Text to convert. If omitted, interactive mode starts.",
    )

    parser.add_argument(
        "--stdin",
        action="store_true",
        help="Read text from standard input and write converted text to standard output.",
    )

    parser.add_argument(
        "--file",
        help="Read text from a UTF-8 file and convert it.",
    )

    parser.add_argument(
        "--out",
        help="Write converted text to a UTF-8 output file instead of standard output.",
    )

    return parser.parse_args()


def output_result(text: str, output_path: str | None) -> None:
    """Write converted text either to stdout or to a UTF-8 file."""
    if output_path:
        with open(output_path, "w", encoding="utf-8", newline="") as file:
            file.write(text)
    else:
        print(text, end="")


def run_interactive_mode() -> None:
    """Run a simple interactive converter prompt."""
    print("TaiLoTyper interactive mode")
    print("Type Tai-lo with tone numbers. Press Enter on a blank line to quit.")
    print()

    while True:
        input_text = input("> ")

        if not input_text:
            break

        print(convert(input_text))


def main() -> None:
    """Run the converter from the command line."""
    args = parse_args()

    if args.file:
        with open(args.file, "r", encoding="utf-8") as file:
            input_text = file.read()
        output_result(convert(input_text), args.out)
        return

    if args.stdin:
        input_text = sys.stdin.read()
        output_result(convert(input_text), args.out)
        return

    if args.text:
        input_text = " ".join(args.text)
        output_result(convert(input_text), args.out)
        return

    run_interactive_mode()


if __name__ == "__main__":
    main()
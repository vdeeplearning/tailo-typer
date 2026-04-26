import re
import sys

TONE_MARKS = {
    "a": {"2": "á", "3": "à", "5": "â", "7": "ā", "8": "a̍"},
    "e": {"2": "é", "3": "è", "5": "ê", "7": "ē", "8": "e̍"},
    "i": {"2": "í", "3": "ì", "5": "î", "7": "ī", "8": "i̍"},
    "o": {"2": "ó", "3": "ò", "5": "ô", "7": "ō", "8": "o̍"},
    "u": {"2": "ú", "3": "ù", "5": "û", "7": "ū", "8": "u̍"},
    "m": {"2": "ḿ", "3": "m̀", "5": "m̂", "7": "m̄", "8": "m̍"},
    "n": {"2": "ń", "3": "ǹ", "5": "n̂", "7": "n̄", "8": "n̍"},
}

VOWEL_PRIORITY = ["a", "e", "o", "i", "u", "m", "n"]


def choose_tone_letter(syllable: str) -> int | None:
    lower = syllable.lower()

    # Tai-lo often treats oo as a vowel unit; mark the first o.
    if "oo" in lower:
        return lower.index("oo")

    for vowel in VOWEL_PRIORITY:
        index = lower.find(vowel)
        if index != -1:
            return index

    return None


def apply_tone(syllable: str, tone: str) -> str:
    if tone in {"1", "4"}:
        return syllable

    index = choose_tone_letter(syllable)

    if index is None:
        return syllable

    original = syllable[index]
    lower = original.lower()

    marked = TONE_MARKS.get(lower, {}).get(tone)

    if marked is None:
        return syllable

    if original.isupper():
        marked = marked.upper()

    return syllable[:index] + marked + syllable[index + 1:]


def convert_token(token: str) -> str:
    match = re.fullmatch(r"([A-Za-z]+)([1-8])", token)

    if not match:
        return token

    syllable, tone = match.groups()
    return apply_tone(syllable, tone)


def convert(text: str) -> str:
    # Convert letter sequences ending in tone numbers.
    return re.sub(
        r"[A-Za-z]+[1-8]",
        lambda match: convert_token(match.group(0)),
        text,
    )


if __name__ == "__main__":
    input_text = " ".join(sys.argv[1:])
    print(convert(input_text))
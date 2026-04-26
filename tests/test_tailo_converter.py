import pytest

from src.tailo_converter import convert, find_tone_target


@pytest.mark.parametrize(
    ("input_text", "expected"),
    [
        ("a1", "a"),
        ("a2", "á"),
        ("a3", "à"),
        ("a4", "a"),
        ("a5", "â"),
        ("a7", "ā"),
        ("a8", "a̍"),
    ],
)
def test_all_supported_tones_for_a(input_text, expected):
    assert convert(input_text) == expected


@pytest.mark.parametrize(
    ("input_text", "expected"),
    [
        ("gua2", "guá"),
        ("e5", "ê"),
        ("tshu3", "tshù"),
        ("u7", "ū"),
        ("ting2", "tíng"),
        ("tsit8", "tsi̍t"),
    ],
)
def test_basic_syllables(input_text, expected):
    assert convert(input_text) == expected


@pytest.mark.parametrize(
    ("input_text", "expected"),
    [
        ("tshu3-ting2", "tshù-tíng"),
        ("niau1-a2", "niau-á"),
        ("tai5-uan5", "tâi-uân"),
    ],
)
def test_hyphenated_words(input_text, expected):
    assert convert(input_text) == expected


@pytest.mark.parametrize(
    ("input_text", "expected"),
    [
        ("Gua2", "Guá"),
        ("U7", "Ū"),
        ("Tai5-uan5", "Tâi-uân"),
    ],
)
def test_capitalization(input_text, expected):
    assert convert(input_text) == expected


def test_sentence():
    assert (
        convert("Gua2 e5 tshu3-ting2 u7 tsit8 tsiah niau1-a2.")
        == "Guá ê tshù-tíng ū tsi̍t tsiah niau-á."
    )


def test_does_not_convert_unattached_numbers():
    assert convert("I have 2 cats and 1 dog.") == "I have 2 cats and 1 dog."


def test_does_not_convert_words_without_tone_numbers():
    assert convert("hello world") == "hello world"


@pytest.mark.parametrize(
    ("syllable", "expected_index"),
    [
        ("tai", 1),   # a wins
        ("gua", 2),   # a wins
        ("tshue", 4), # e wins over u
        ("too", 1),   # oo marks first o
        ("tsit", 2),  # i
        ("hun", 1),   # u
    ],
)
def test_find_tone_target(syllable, expected_index):
    assert find_tone_target(syllable) == expected_index
from src.tailo_converter import convert


def test_basic_tones():
    assert convert("gua2") == "guá"
    assert convert("e5") == "ê"
    assert convert("tshu3") == "tshù"
    assert convert("u7") == "ū"


def test_hyphenated_words():
    assert convert("tshu3-ting2") == "tshù-tíng"
    assert convert("niau1-a2") == "niau-á"


def test_checked_tone():
    assert convert("tsit8") == "tsi̍t"


def test_sentence():
    assert (
        convert("Gua2 e5 tshu3-ting2 u7 tsit8 tsiah niau1-a2.")
        == "Guá ê tshù-tíng ū tsi̍t tsiah niau-á."
    )
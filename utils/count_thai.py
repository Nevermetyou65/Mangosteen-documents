import re
import regex

UNICODE_THAI_CHAR = r"\u0E01-\u0E2F"
UNICODE_THAI_VOWEL = r"\u0E30-\u0E39\u0E40-\u0E47\u0E4C-\u0E4E"
UNICODE_THAI_INTONATION = r"\u0E48-\u0E4B"
UNICODE_LETTERS = r"\p{L}"
THAI_PATTERN = rf"[{UNICODE_THAI_CHAR}{UNICODE_THAI_VOWEL}{UNICODE_THAI_INTONATION}]"

THAI_CHAR = re.compile(THAI_PATTERN)
ALL_CHAR = regex.compile(
    rf"[{UNICODE_LETTERS}{UNICODE_THAI_VOWEL}{UNICODE_THAI_INTONATION}]"
)


def detect_thai(text: str) -> float:
    """Calculate percentage of Thai characters in text."""
    text_no_spaces = text.replace(" ", "")

    thai_char_count = sum(1 for _ in THAI_CHAR.finditer(text_no_spaces))
    total_char_count = sum(1 for _ in ALL_CHAR.finditer(text_no_spaces))

    if total_char_count == 0:
        score = 0.0
    else:
        score = (thai_char_count / total_char_count) * 100

    return score

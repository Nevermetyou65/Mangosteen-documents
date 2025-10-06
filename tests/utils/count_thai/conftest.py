import pytest


@pytest.fixture
def pure_thai_text():
    """Sample text with only Thai characters."""
    return "สวัสดีครับ นี่คือข้อความภาษาไทย ตัวอย่างสำหรับการทดสอบ"


@pytest.fixture
def pure_english_text():
    """Sample text with only English characters."""
    return "Hello this is a sample English text for testing purposes"


@pytest.fixture
def mixed_text():
    """Sample text with mixed Thai and English characters."""
    return "สวัสดี Hello นี่คือ mixed text ครับ"


@pytest.fixture
def empty_text():
    """Empty text."""
    return ""


@pytest.fixture
def whitespace_only_text():
    """Text with only whitespace."""
    return "     "


@pytest.fixture
def thai_with_special_chars():
    """Thai text with special characters and numbers."""
    return "สวัสดีครับ 123 !@# ทดสอบ"


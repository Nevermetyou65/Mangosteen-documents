import pytest
from unittest.mock import Mock


@pytest.fixture
def mock_logger():
    """Mock logger for testing."""
    logger = Mock()
    return logger


# Test data for filter_by_image function
@pytest.fixture
def json_with_few_pictures():
    """JSON data with less than 1 picture per page."""
    return {
        "page_stats": [
            {
                "page_id": 0,
                "block_counts": [
                    ["Text", 10],
                    ["Picture", 0],
                ]
            },
            {
                "page_id": 1,
                "block_counts": [
                    ["Text", 8],
                    ["Picture", 1],
                ]
            },
            {
                "page_id": 2,
                "block_counts": [
                    ["Text", 12],
                ]
            }
        ]
    }


@pytest.fixture
def json_with_many_pictures():
    """JSON data with 1 or more pictures per page."""
    return {
        "page_stats": [
            {
                "page_id": 0,
                "block_counts": [
                    ["Text", 5],
                    ["Picture", 2],
                ]
            },
            {
                "page_id": 1,
                "block_counts": [
                    ["Text", 3],
                    ["Picture", 3],
                ]
            }
        ]
    }


@pytest.fixture
def json_no_page_stats():
    """JSON data without page_stats."""
    return {
        "table_of_contents": [],
        "metadata": {}
    }


@pytest.fixture
def json_empty_page_stats():
    """JSON data with empty page_stats."""
    return {
        "page_stats": []
    }


# Test data for filter_by_lang function
@pytest.fixture
def thai_markdown_content():
    """Markdown content with predominantly Thai text."""
    return """
## หัวข้อภาษาไทย

นี่คือเนื้อหาภาษาไทยที่ใช้ในการทดสอบ
ระบบจะต้องตรวจจับว่าเป็นภาษาไทย

### หัวข้อย่อย

เนื้อหาเพิ่มเติมเป็นภาษาไทย
สำหรับการทดสอบระบบ
"""


@pytest.fixture
def english_markdown_content():
    """Markdown content with predominantly English text."""
    return """
## English Title

This is English content for testing purposes.
The system should detect this as English text.

### Subsection

More English content here
For testing the system
"""


@pytest.fixture
def mixed_markdown_content():
    """Markdown content with mixed Thai and English, but Thai dominant."""
    return """
## Thai Title - ภาษาไทย

This document contains mixed content.
เอกสารนี้มีเนื้อหาแบบผสม
More Thai content here - มีเนื้อหาภาษาไทยมากกว่า
เพื่อให้การทดสอบผ่าน
"""


@pytest.fixture
def sample_file_paths():
    """Sample file paths for testing."""
    return [
        "/path/to/file1.json",
        "/path/to/file2.json",
        "/path/to/file3.json",
    ]


@pytest.fixture
def sample_md_paths():
    """Sample markdown file paths for testing."""
    return [
        "/path/to/doc1.md",
        "/path/to/doc2.md",
        "/path/to/doc3.md",
    ]


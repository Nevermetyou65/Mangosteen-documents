# Test Suite Documentation

This directory contains the test suite for the Mangosteen Documents project.

## Structure

```
tests/
├── __init__.py
├── README.md
└── utils/
    ├── __init__.py
    ├── count_thai/
    │   ├── __init__.py
    │   ├── conftest.py          # Test fixtures for count_thai tests
    │   └── test_count_thai.py   # Tests for count_thai.py
    └── filters/
        ├── __init__.py
        ├── conftest.py          # Test fixtures for filter tests
        └── test_filter.py       # Tests for filter.py
```

## Running Tests

### Run all tests
```bash
pytest
```

### Run tests for a specific module
```bash
# Test count_thai module
pytest tests/utils/count_thai/

# Test filter module
pytest tests/utils/filters/
```

### Run a specific test file
```bash
pytest tests/utils/count_thai/test_count_thai.py
pytest tests/utils/filters/test_filter.py
```

### Run a specific test class or function
```bash
# Run specific test class
pytest tests/utils/count_thai/test_count_thai.py::TestDetectThai

# Run specific test function
pytest tests/utils/count_thai/test_count_thai.py::TestDetectThai::test_pure_thai_text
```

### Run with coverage
```bash
# Install pytest-cov if not already installed
# uv pip install pytest-cov

pytest --cov=utils --cov-report=html --cov-report=term
```

### Run with verbose output
```bash
pytest -v
```

### Run with output capture disabled (see print statements)
```bash
pytest -s
```

## Test Descriptions

### count_thai Tests (`tests/utils/count_thai/`)

Tests for the `detect_thai()` function that calculates the percentage of Thai characters in text.

**Test Structure:** Test class with 9 test methods

**Test Cases:**
- `test_pure_thai_text` - Validates detection of pure Thai text (score > 95)
- `test_pure_english_text` - Validates detection of pure English text (score = 0)
- `test_mixed_text` - Validates detection of mixed Thai/English content
- `test_empty_text` - Handles empty strings correctly
- `test_whitespace_only_text` - Handles whitespace-only strings
- `test_thai_with_special_chars` - Handles Thai text with numbers/special characters
- `test_return_type` - Validates return type is float
- `test_score_range` - Ensures scores are always in [0, 100] range
- `test_spaces_ignored` - Verifies spaces are correctly ignored in calculation

### filter Tests (`tests/utils/filters/`)

Tests for filtering functions used in document processing pipeline.

**Test Structure:** Individual test functions (not classes) using pytest-mock's `mocker` fixture

#### `filter_by_image()` Tests

**Test Cases:**
- `test_filter_by_image_keeps_files_with_few_pictures` - Files with < 1 pic/page are kept
- `test_filter_by_image_removes_files_with_many_pictures` - Files with >= 1 pic/page removed
- `test_filter_by_image_skips_files_without_page_stats` - Missing page_stats handled properly
- `test_filter_by_image_handles_multiple_files` - Batch processing works correctly
- `test_filter_by_image_handles_exceptions` - Exceptions are caught and logged
- `test_filter_by_image_with_empty_page_stats` - Empty page_stats array handled
- `test_filter_by_image_exact_threshold` - Edge case at exactly 1 pic/page
- `test_filter_by_image_logs_result_count` - Result count is logged

#### `filter_by_lang()` Tests

**Test Cases:**
- `test_filter_by_lang_keeps_thai_content` - Thai content (score > 0.5) is kept
- `test_filter_by_lang_removes_english_content` - English content (score <= 0.5) removed
- `test_filter_by_lang_handles_mixed_content` - Mixed content with Thai dominant kept
- `test_filter_by_lang_handles_multiple_files` - Batch processing works correctly
- `test_filter_by_lang_handles_exceptions` - File read errors caught and logged
- `test_filter_by_lang_threshold_edge_case` - Edge case near 0.5 threshold
- `test_filter_by_lang_empty_content` - Empty markdown files handled
- `test_filter_by_lang_logs_result_count` - Result count is logged
- `test_filter_by_lang_with_only_special_characters` - Special chars only handled

## Test Fixtures

### count_thai fixtures (`conftest.py`)
- `pure_thai_text` - Sample Thai text
- `pure_english_text` - Sample English text
- `mixed_text` - Mixed Thai/English text
- `empty_text` - Empty string
- `whitespace_only_text` - Whitespace only
- `thai_with_special_chars` - Thai with numbers/special chars

### filter fixtures (`conftest.py`)
- `mock_logger` - Mock logger for testing
- `json_with_few_pictures` - JSON with < 1 pic/page
- `json_with_many_pictures` - JSON with >= 1 pic/page
- `json_no_page_stats` - JSON without page_stats
- `json_empty_page_stats` - JSON with empty page_stats
- `thai_markdown_content` - Thai markdown sample
- `english_markdown_content` - English markdown sample
- `mixed_markdown_content` - Mixed language markdown
- `sample_file_paths` - Sample JSON file paths
- `sample_md_paths` - Sample markdown file paths

## Mocking Strategy

The filter tests use the **pytest-mock** plugin's `mocker` fixture to mock file I/O operations:

```python
def test_filter_by_image_keeps_files_with_few_pictures(
    mocker,
    json_with_few_pictures,
    mock_logger
):
    # Use mocker.patch() to mock the function
    mock_open_json = mocker.patch('utils.filter.open_json')
    mock_open_json.return_value = json_with_few_pictures
    # ... rest of test
```

**Benefits of pytest-mock:**
- Cleaner syntax compared to `unittest.mock`
- Automatic cleanup after each test
- Better integration with pytest fixtures
- No need for `@patch` decorators

**What is mocked:**
- `open_json()` is mocked to return test JSON data
- `open_md()` is mocked to return test markdown content

This allows testing the filtering logic without requiring actual files on disk.

**Reference:** [pytest-mock documentation](https://pytest-mock.readthedocs.io/)

## Writing New Tests

When adding new tests:

1. Add test fixtures to the appropriate `conftest.py`
2. Create test functions (or methods in test classes) following the naming convention `test_*`
3. Use descriptive docstrings
4. Include assertions with helpful error messages
5. Test both happy path and edge cases
6. Use `mocker` fixture for mocking when needed

**Example for filter tests (function-based):**
```python
def test_new_filter_feature(mocker, fixture_name, mock_logger):
    """Test description here."""
    # Setup
    mock_function = mocker.patch('utils.filter.function_to_mock')
    mock_function.return_value = expected_data
    
    # Execute
    result = function_under_test()
    
    # Assert
    assert result == expected_value, "Helpful error message"
    mock_function.assert_called_once()
```

**Example for count_thai tests (class-based):**
```python
class TestDetectThai:
    def test_new_feature(self, fixture_name):
        """Test description here."""
        # Setup
        # ... setup code
        
        # Execute
        result = detect_thai(fixture_name)
        
        # Assert
        assert result == expected_value, "Helpful error message"
```


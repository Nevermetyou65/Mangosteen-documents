# Changes to Test Suite

## Summary

The `test_filter.py` file has been refactored to use **pytest-mock** instead of `unittest.mock` and converted from test classes to individual test functions.

## What Changed

### Before (unittest.mock with classes)
```python
from unittest.mock import patch

class TestFilterByImage:
    @patch('utils.filter.open_json')
    def test_filter_keeps_files_with_few_pictures(
        self,
        mock_open_json,
        json_with_few_pictures,
        mock_logger
    ):
        mock_open_json.return_value = json_with_few_pictures
        # ... rest of test
```

### After (pytest-mock with functions)
```python
# No imports needed - mocker is a fixture

def test_filter_by_image_keeps_files_with_few_pictures(
    mocker,
    json_with_few_pictures,
    mock_logger
):
    mock_open_json = mocker.patch('utils.filter.open_json')
    mock_open_json.return_value = json_with_few_pictures
    # ... rest of test
```

## Benefits of pytest-mock

1. **Cleaner syntax** - No decorator needed, just use `mocker.patch()` directly
2. **Better pytest integration** - Works seamlessly with pytest fixtures
3. **Automatic cleanup** - Mocks are automatically cleaned up after each test
4. **More Pythonic** - Follows pytest conventions
5. **Easier to read** - The mocking is done in the test body, not in decorators

## Changes Made

### 1. Removed unittest.mock import
- **Removed:** `from unittest.mock import patch`
- **Added:** Using `mocker` fixture (provided by pytest-mock plugin)

### 2. Converted test classes to functions
- **Before:** 2 test classes (`TestFilterByImage`, `TestFilterByLang`)
- **After:** 17 individual test functions

### 3. Updated test names for clarity
All test functions now have descriptive prefixes:
- `test_filter_by_image_*` - for `filter_by_image()` tests
- `test_filter_by_lang_*` - for `filter_by_lang()` tests

### 4. Changed mocking approach
- **Before:** `@patch` decorators
- **After:** `mocker.patch()` calls in test body

## Test Results

All 26 tests still pass:
- ✅ 9 tests for `detect_thai()` (unchanged - still uses class)
- ✅ 8 tests for `filter_by_image()` (refactored to functions)
- ✅ 9 tests for `filter_by_lang()` (refactored to functions)

```bash
============================== 26 passed in 0.04s ==============================
```

## Migration Guide

If you want to add new tests for filter functions, use this pattern:

```python
def test_filter_by_[function]_[description](mocker, fixtures, mock_logger):
    """Clear description of what is being tested."""
    # Setup - Use mocker.patch() to mock functions
    mock_function = mocker.patch('module.function_to_mock')
    mock_function.return_value = expected_data
    
    # Execute - Call the function under test
    result = function_under_test(args)
    
    # Assert - Verify results and mock calls
    assert result == expected
    mock_function.assert_called_once()
```

## Documentation Updated

The following files were updated to reflect these changes:
- ✅ `tests/README.md` - Updated mocking strategy section and examples
- ✅ `tests/TEST_SUMMARY.md` - Updated test descriptions and structure
- ✅ `tests/CHANGES.md` - This file (explains the changes)

## References

- [pytest-mock documentation](https://pytest-mock.readthedocs.io/)
- [pytest fixtures documentation](https://docs.pytest.org/en/stable/fixture.html)


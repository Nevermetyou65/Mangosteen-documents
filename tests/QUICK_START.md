# Quick Start Guide - Updated Test Suite

## ✅ All Changes Complete!

The test suite has been successfully refactored to use **pytest-mock** instead of `unittest.mock`.

## What's New

### 🔄 Refactored `test_filter.py`
- **Before:** Test classes with `@patch` decorators from `unittest.mock`
- **After:** Individual test functions using `mocker` fixture from `pytest-mock`

### Key Changes:
1. ✅ Removed `unittest.mock` imports
2. ✅ Converted test classes to functions
3. ✅ Using `mocker.patch()` instead of `@patch` decorator
4. ✅ Updated test names for better clarity
5. ✅ Updated all documentation

## Running Tests

```bash
# Run all tests
uv run pytest

# Run with verbose output
uv run pytest -v

# Run specific test file
uv run pytest tests/utils/filters/test_filter.py -v

# Run specific test
uv run pytest tests/utils/filters/test_filter.py::test_filter_by_image_keeps_files_with_few_pictures -v
```

## Test Results

**26 tests - All Passing ✅** (0.04 seconds)

```
tests/utils/count_thai/  - 9 tests (class-based)
tests/utils/filters/     - 17 tests (function-based with pytest-mock)
```

## Example: New pytest-mock Pattern

```python
def test_filter_by_image_example(mocker, mock_logger):
    """Example showing pytest-mock usage."""
    # Setup - Use mocker.patch()
    mock_open_json = mocker.patch('utils.filter.open_json')
    mock_open_json.return_value = {"page_stats": [...]}
    
    # Execute
    result = filter_by_image(["/path/to/file.json"], mock_logger)
    
    # Assert
    assert len(result) == 1
    mock_open_json.assert_called_once()
```

## Benefits of pytest-mock

✅ **Cleaner code** - No decorators needed
✅ **Better integration** - Works seamlessly with pytest fixtures  
✅ **Automatic cleanup** - Mocks cleaned up after each test
✅ **More readable** - Mocking in test body, not decorators
✅ **Follows pytest conventions** - True pytest style

## Documentation

- 📖 **tests/README.md** - Complete documentation
- 📊 **tests/TEST_SUMMARY.md** - Detailed test coverage
- 🔄 **tests/CHANGES.md** - What changed and why
- ⚡ **tests/QUICK_START.md** - This file

## Files Modified

### Test Files
- ✅ `tests/utils/filters/test_filter.py` - Refactored to use pytest-mock

### Documentation
- ✅ `tests/README.md` - Updated with pytest-mock examples
- ✅ `tests/TEST_SUMMARY.md` - Updated test descriptions
- ✅ `tests/CHANGES.md` - Migration guide
- ✅ `tests/QUICK_START.md` - Quick reference

## Verification

All linter errors: **None** ✅
All tests passing: **26/26** ✅
Test execution time: **~0.04s** ✅

## Next Steps

To add new filter tests, follow this pattern:

```python
def test_filter_by_[function]_[what_it_tests](mocker, fixtures, mock_logger):
    """Clear docstring."""
    mock_func = mocker.patch('utils.filter.function_name')
    mock_func.return_value = test_data
    
    result = function_under_test(args)
    
    assert result == expected
    mock_func.assert_called()
```

## Reference

- [pytest-mock docs](https://pytest-mock.readthedocs.io/)
- [pytest fixtures](https://docs.pytest.org/en/stable/fixture.html)

---

**Everything is ready to use! 🎉**


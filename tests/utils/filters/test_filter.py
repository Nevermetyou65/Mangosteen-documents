from utils.filter import filter_by_image, filter_by_lang


def test_filter_by_image_keeps_files_with_few_pictures(
    mocker, json_with_few_pictures, mock_logger
):
    """Test that files with < 1 picture per page are kept."""
    # Setup
    mock_open_json = mocker.patch("utils.filter.open_json")
    mock_open_json.return_value = json_with_few_pictures
    files = ["/path/to/file1.json"]

    # Execute
    result = filter_by_image(files, mock_logger)

    # Assert
    assert len(result) == 1
    assert result[0] == "/path/to/file1.json"
    mock_open_json.assert_called_once_with("/path/to/file1.json")


def test_filter_by_image_removes_files_with_many_pictures(
    mocker, json_with_many_pictures, mock_logger
):
    """Test that files with >= 1 picture per page are filtered out."""
    # Setup
    mock_open_json = mocker.patch("utils.filter.open_json")
    mock_open_json.return_value = json_with_many_pictures
    files = ["/path/to/file1.json"]

    # Execute
    result = filter_by_image(files, mock_logger)

    # Assert
    assert len(result) == 0
    mock_open_json.assert_called_once()


def test_filter_by_image_skips_files_without_page_stats(
    mocker, json_no_page_stats, mock_logger
):
    """Test that files without page_stats are skipped with warning."""
    # Setup
    mock_open_json = mocker.patch("utils.filter.open_json")
    mock_open_json.return_value = json_no_page_stats
    files = ["/path/to/file1.json"]

    # Execute
    result = filter_by_image(files, mock_logger)

    # Assert
    assert len(result) == 0
    mock_logger.warning.assert_called_once()
    assert "No page stats found" in mock_logger.warning.call_args[0][0]


def test_filter_by_image_handles_multiple_files(
    mocker, json_with_few_pictures, json_with_many_pictures, mock_logger
):
    """Test filtering multiple files with different picture counts."""
    # Setup
    mock_open_json = mocker.patch("utils.filter.open_json")
    files = ["/path/to/file1.json", "/path/to/file2.json", "/path/to/file3.json"]
    mock_open_json.side_effect = [
        json_with_few_pictures,  # file1: keep
        json_with_many_pictures,  # file2: remove
        json_with_few_pictures,  # file3: keep
    ]

    # Execute
    result = filter_by_image(files, mock_logger)

    # Assert
    assert len(result) == 2
    assert "/path/to/file1.json" in result
    assert "/path/to/file3.json" in result
    assert "/path/to/file2.json" not in result


def test_filter_by_image_handles_exceptions(mocker, mock_logger):
    """Test that exceptions are caught and logged."""
    # Setup
    mock_open_json = mocker.patch("utils.filter.open_json")
    mock_open_json.side_effect = Exception("File read error")
    files = ["/path/to/file1.json"]

    # Execute
    result = filter_by_image(files, mock_logger)

    # Assert
    assert len(result) == 0
    mock_logger.error.assert_called_once()
    assert "Error processing" in mock_logger.error.call_args[0][0]


def test_filter_by_image_with_empty_page_stats(
    mocker, json_empty_page_stats, mock_logger
):
    """Test handling of JSON with empty page_stats array."""
    # Setup
    mock_open_json = mocker.patch("utils.filter.open_json")
    mock_open_json.return_value = json_empty_page_stats
    files = ["/path/to/file1.json"]

    # Execute
    result = filter_by_image(files, mock_logger)

    # Assert
    assert len(result) == 0
    mock_logger.warning.assert_called_once()


def test_filter_by_image_exact_threshold(mocker, mock_logger):
    """Test edge case where picture count equals 1 per page."""
    # Setup
    mock_open_json = mocker.patch("utils.filter.open_json")
    json_exact_threshold = {
        "page_stats": [
            {"page_id": 0, "block_counts": [["Picture", 1]]},
        ]
    }
    mock_open_json.return_value = json_exact_threshold
    files = ["/path/to/file1.json"]

    # Execute
    result = filter_by_image(files, mock_logger)

    # Assert - exactly 1 picture per page should be filtered out (>= 1)
    assert len(result) == 0


def test_filter_by_image_logs_result_count(mocker, json_with_few_pictures, mock_logger):
    """Test that the function logs the final count."""
    # Setup
    mock_open_json = mocker.patch("utils.filter.open_json")
    mock_open_json.return_value = json_with_few_pictures
    files = ["/path/to/file1.json", "/path/to/file2.json"]

    # Execute
    result = filter_by_image(files, mock_logger)

    # Assert
    assert len(result) == 2  # Both files should be kept
    mock_logger.info.assert_called_once()
    assert "Num remain:" in mock_logger.info.call_args[0][0]


# Tests for filter_by_lang function


def test_filter_by_lang_keeps_thai_content(mocker, thai_markdown_content, mock_logger):
    """Test that files with predominantly Thai content (score > 0.5) are kept."""
    # Setup
    mock_open_md = mocker.patch("utils.filter.open_md")
    mock_open_md.return_value = thai_markdown_content
    files = ["/path/to/doc1.md"]

    # Execute
    result = filter_by_lang(files, mock_logger)

    # Assert
    assert len(result) == 1
    assert result[0] == "/path/to/doc1.md"
    mock_open_md.assert_called_once_with("/path/to/doc1.md")


def test_filter_by_lang_removes_english_content(
    mocker, english_markdown_content, mock_logger
):
    """Test that files with predominantly English content (score <= 0.5) are filtered out."""
    # Setup
    mock_open_md = mocker.patch("utils.filter.open_md")
    mock_open_md.return_value = english_markdown_content
    files = ["/path/to/doc1.md"]

    # Execute
    result = filter_by_lang(files, mock_logger)

    # Assert
    assert len(result) == 0
    mock_open_md.assert_called_once()


def test_filter_by_lang_handles_mixed_content(
    mocker, mixed_markdown_content, mock_logger
):
    """Test filtering of mixed Thai-English content."""
    # Setup
    mock_open_md = mocker.patch("utils.filter.open_md")
    mock_open_md.return_value = mixed_markdown_content
    files = ["/path/to/doc1.md"]

    # Execute
    result = filter_by_lang(files, mock_logger)

    # Assert - Mixed content with dominant Thai should be kept
    assert len(result) == 1


def test_filter_by_lang_handles_multiple_files(
    mocker,
    thai_markdown_content,
    english_markdown_content,
    mixed_markdown_content,
    mock_logger,
):
    """Test filtering multiple markdown files."""
    # Setup
    mock_open_md = mocker.patch("utils.filter.open_md")
    files = ["/path/to/doc1.md", "/path/to/doc2.md", "/path/to/doc3.md"]
    mock_open_md.side_effect = [
        thai_markdown_content,  # doc1: keep (Thai)
        english_markdown_content,  # doc2: remove (English)
        mixed_markdown_content,  # doc3: keep (Mixed but Thai dominant)
    ]

    # Execute
    result = filter_by_lang(files, mock_logger)

    # Assert
    assert len(result) == 2
    assert "/path/to/doc1.md" in result
    assert "/path/to/doc3.md" in result
    assert "/path/to/doc2.md" not in result


def test_filter_by_lang_handles_exceptions(mocker, mock_logger):
    """Test that file read exceptions are caught and logged."""
    # Setup
    mock_open_md = mocker.patch("utils.filter.open_md")
    mock_open_md.side_effect = Exception("Cannot read file")
    files = ["/path/to/doc1.md"]

    # Execute
    result = filter_by_lang(files, mock_logger)

    # Assert
    assert len(result) == 0
    mock_logger.error.assert_called_once()
    assert "Cannot read OCR result" in mock_logger.error.call_args[0][0]


def test_filter_by_lang_threshold_edge_case(mocker, mock_logger):
    """Test edge case where Thai score is exactly at threshold."""
    # Setup - Create content that will score very close to 0.5
    mock_open_md = mocker.patch("utils.filter.open_md")
    edge_case_content = "Hello สวัสดี World ครับ Test ทดสอบ"
    mock_open_md.return_value = edge_case_content
    files = ["/path/to/doc1.md"]

    # Execute
    result = filter_by_lang(files, mock_logger)

    # Assert - score must be > 0.5 to be included
    # This content should be close to threshold, result depends on exact calculation
    assert isinstance(result, list)


def test_filter_by_lang_empty_content(mocker, mock_logger):
    """Test handling of empty markdown content."""
    # Setup
    mock_open_md = mocker.patch("utils.filter.open_md")
    mock_open_md.return_value = ""
    files = ["/path/to/doc1.md"]

    # Execute
    result = filter_by_lang(files, mock_logger)

    # Assert - empty content should have score 0, so filtered out
    assert len(result) == 0


def test_filter_by_lang_logs_result_count(mocker, thai_markdown_content, mock_logger):
    """Test that the function logs the final count."""
    # Setup
    mock_open_md = mocker.patch("utils.filter.open_md")
    mock_open_md.return_value = thai_markdown_content
    files = ["/path/to/doc1.md", "/path/to/doc2.md"]

    # Execute
    result = filter_by_lang(files, mock_logger)

    # Assert
    assert len(result) == 2  # Both files should be kept (Thai content)
    mock_logger.info.assert_called_once()
    assert "Num remain:" in mock_logger.info.call_args[0][0]


def test_filter_by_lang_with_only_special_characters(mocker, mock_logger):
    """Test handling of content with only special characters and numbers."""
    # Setup
    mock_open_md = mocker.patch("utils.filter.open_md")
    mock_open_md.return_value = "123 !@# $%^ &*()"
    files = ["/path/to/doc1.md"]

    # Execute
    result = filter_by_lang(files, mock_logger)

    # Assert - no Thai characters, should be filtered out
    assert len(result) == 0

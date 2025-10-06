from utils.count_thai import detect_thai


class TestDetectThai:
    """Test suite for detect_thai fupction."""

    def test_pure_thai_text(self, pure_thai_text):
        """Test detection with pure Thai text - should return close to 100."""
        score = detect_thai(pure_thai_text)
        assert score > 95.0, f"Expected score > 95 for pure Thai text, got {score}"
        assert score <= 100.0, f"Score should not exceed 100, got {score}"

    def test_pure_english_text(self, pure_english_text):
        """Test detection with pure English text - should return 0."""
        score = detect_thai(pure_english_text)
        assert score == 0.0, f"Expected score 0 for pure English text, got {score}"

    def test_mixed_text(self, mixed_text):
        """Test detection with mixed Thai and English text."""
        score = detect_thai(mixed_text)
        assert 0.0 < score < 100.0, (
            f"Expected score between 0 and 100 for mixed text, got {score}"
        )
        # Mixed text should have significant Thai content
        assert score > 40.0, (
            f"Expected score > 40 for mixed text with Thai, got {score}"
        )

    def test_empty_text(self, empty_text):
        """Test detection with empty text - should return 0.0."""
        score = detect_thai(empty_text)
        assert score == 0.0, f"Expected score 0 for empty text, got {score}"

    def test_whitespace_only_text(self, whitespace_only_text):
        """Test detection with whitespace only - should return 0.0."""
        score = detect_thai(whitespace_only_text)
        assert score == 0.0, f"Expected score 0 for whitespace only, got {score}"

    def test_thai_with_special_chars(self, thai_with_special_chars):
        """Test detection with Thai text including numbers and special characters."""
        score = detect_thai(thai_with_special_chars)
        # Special chars and numbers are not counted, so Thai percentage among letters should be high
        assert score > 0.0, (
            f"Expected score > 0 for Thai text with special chars, got {score}"
        )
        # Score could be 100 if all letter characters are Thai (numbers/special chars ignored)
        assert score <= 100.0, f"Score should not exceed 100, got {score}"

    def test_return_type(self, pure_thai_text):
        """Test that function returns a float."""
        score = detect_thai(pure_thai_text)
        assert isinstance(score, float), (
            f"Expected return type float, got {type(score)}"
        )

    def test_score_range(self):
        """Test that score is always in valid range [0, 100]."""
        test_cases = [
            "สวัสดีครับ",
            "Hello world",
            "Mixed ข้อความ 123",
            "",
            "   ",
        ]
        for text in test_cases:
            score = detect_thai(text)
            assert 0.0 <= score <= 100.0, (
                f"Score {score} out of range [0, 100] for text: '{text}'"
            )

    def test_spaces_ignored(self):
        """Test that spaces are correctly ignored in calculation."""
        text_with_spaces = "สวัสดี ครับ"
        text_without_spaces = "สวัสดีครับ"

        score_with_spaces = detect_thai(text_with_spaces)
        score_without_spaces = detect_thai(text_without_spaces)

        # Scores should be identical since spaces are ignored
        assert score_with_spaces == score_without_spaces, (
            f"Scores should be equal when spaces are removed: {score_with_spaces} vs {score_without_spaces}"
        )

from compress import string_compression
import pytest

COMPRESS = [
    ("aabbcc", "a2b2c2"),
    ("qqqqqqqq", "q8")
]

@pytest.mark.parametrize("input, output", COMPRESS)
def test_string_compress(input, output):
    assert string_compression(input) == output

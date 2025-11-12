import pytest
from src.rate_note import rate_note

@pytest.mark.parametrize("note", [5,6,7,8, 9])
def test_rate_note_unsuccessful(note):
    assert rate_note(note) == note


def test_rate_10_returns_acceptable():
     assert rate_note(10) == "acceptable"

def test_rate_12_returns_good():
     assert rate_note(12) == "good"
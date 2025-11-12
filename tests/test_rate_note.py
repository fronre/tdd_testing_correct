import pytest
from src.rate_note import rate_note


@pytest.mark.parametrize(
    'note, expected',
    [
        (7, 'unsuccessful'),
        (8, 'unsuccessful'),
        (9, 'unsuccessful'),
        (10, 'acceptable'),
        (11, 'acceptable'),
          (12, 'good'),
        (13, 'good'),
    ]
)
def test_rate_note_returns_unsuccessful(note, expected):
    actual_result = rate_note(note)
    assert actual_result == expected


def test_rate_14_returns_very_good():
      assert rate_note(14) == "very good"

def test_rate_16_returns_very_good():
      assert rate_note(16) == "very good"
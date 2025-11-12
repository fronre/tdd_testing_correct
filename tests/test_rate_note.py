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
        (14, 'very good'),
        (15, 'very good'),
        (16, 'very good'),
    ]
)
def test_rate_note_returns_unsuccessful(note, expected):
    actual_result = rate_note(note)
    assert actual_result == expected

def test_rate_17_returns_excellent():
   assert rate_note(17) == 'excellent'

def test_rate_18_returns_excellent():
    assert rate_note(18) == 'excellent'

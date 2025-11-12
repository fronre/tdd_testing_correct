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
        (17, 'excellent'),
        (18, 'excellent'),
        (19, 'excellent'),
        (20, 'excellent'),
        (21, 'Impossible note value'),
        (22, 'Impossible note value'),
        (-1, 'Impossible note value'),

    ]
)
def test_rate_note_returns_unsuccessful(note, expected):
    actual_result = rate_note(note)
    assert actual_result == expected



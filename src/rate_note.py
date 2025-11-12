def rate_note(note: int) -> str:
    if note < 10:
        return "unsuccessful"
    if note == 10:
        return "acceptable"
    return "good"

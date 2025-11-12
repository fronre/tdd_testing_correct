def rate_note(note: int) -> str:
    if note < 10:
       return "unsuccessful"
    if 10 < note < 12:
        return "acceptable"
    if note ==12:
       return "good"
    return "very good"


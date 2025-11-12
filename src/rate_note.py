def rate_note(note: int) -> str:
    if note < 10:
       return "unsuccessful"
    if 10 < note < 12:
        return "acceptable"
    if 12 <= note < 14:
       return " good"
    if 14 < note < 16:
        return "very good"



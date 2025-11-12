def rate_note(note: int) -> str:
    if note < 0 or note > 20:
        raise ValueError(f"Impossible note value: {note}. Must be between 0 and 20.")
    if note < 10:
       return "unsuccessful"
    if 10 < note < 12:
        return "acceptable"
    if 12 <= note < 14:
       return " good"
    if 14 < note <= 16:
        return "very good"
    if 16 < note <= 20:
        return "excellent"



DATA = [
    ("house that Jack built.", ""),
    ("malt", "that lay in the"),
    ("rat", "that ate the"),
    ("cat", "that killed the"),
    ("dog", "that worried the"),
    ("cow with the crumpled horn", "that tossed the"),
    ("maiden all forlorn", "that milked the"),
    ("man all tattered and torn", "that kissed the"),
    ("priest all shaven and shorn", "that married the"),
    ("rooster that crowed in the morn", "that woke the"),
    ("farmer sowing his corn", "that kept the"),
    ("horse and the hound and the horn", "that belonged to the")
]
def recite(start_verse: int, end_verse: int) -> list[str]:
    """Generates a list of verses from the song 'The House That Jack Built'.

    Args:
        start_verse (int): The index of the first verse to recite (1-12).
        end_verse (int): The index of the last verse to recite (1-12).

    Returns:
        list[str]: A list containing the requested verses.
    """

    if start_verse < 1 or end_verse > len(DATA) or start_verse > end_verse:
        raise ValueError("Verse indices must be between 1 and 12, and start_verse cannot be greater than end_verse.")

    def verse(i: int) -> str:
        if i == 0:
            return f'{DATA[i][0]}'
        else:
            return f'{DATA[i][0]} {DATA[i][1]} {verse(i - 1)}'

    verses: list[str] = [f'This is the {verse(v - 1)}' for v in range(start_verse, end_verse + 1)]

    return verses

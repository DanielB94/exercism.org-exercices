def is_isogram(phrase):
    clean_phrase = phrase.replace('-', '').replace(' ', '').lower()
    return len(clean_phrase) == len(set(clean_phrase))

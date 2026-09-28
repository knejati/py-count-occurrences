def count_occurrences(phrase: str, letter: str) -> int:
    count_letters = 0
    for char in phrase.lower():
        if char == letter.lower():
            count_letters += 1
    return count_letters


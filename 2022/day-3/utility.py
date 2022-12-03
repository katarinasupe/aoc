# priority rules:
# ord("letter") - ord("a") + 1
# ord("LETTER") - ord("A") + 27
def get_priority(letter: str):
    ascii_code = ord(letter)
    return ascii_code - ord("A") + 27 if letter.isupper() else ascii_code - ord("a") + 1

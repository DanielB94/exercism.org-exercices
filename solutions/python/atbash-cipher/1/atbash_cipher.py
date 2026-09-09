ALPHABET = "abcdefghijklmnopqrstuvwxyz"
REVERSED_ALPHABET = ALPHABET[::-1]

def translate_char(char):
        return REVERSED_ALPHABET[ALPHABET.index(char.lower())] if char.isalpha() else char

def encode(plain_text):
    encoded_text = ''.join([translate_char(digit) for digit in plain_text if digit.isalnum()])
    return " ".join([encoded_text[i: i + 5] for i in range(0, len(encoded_text), 5)])
        
def decode(ciphered_text):
    return ''.join([translate_char(digit) for digit in ciphered_text if digit.isalnum()])

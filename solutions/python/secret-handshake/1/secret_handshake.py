BIT = [(1, 'wink'), (2, 'double blink'), (4, 'close your eyes'), (8, 'jump')]

def commands(binary_str):
    bit_number = int(binary_str, 2)
    actions = [action for bit, action in BIT if bit_number & bit]
    return actions[::-1] if bit_number & 16 else actions

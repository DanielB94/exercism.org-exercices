def rows(letter):
    dist = ord(letter) - ord("A")
    letters = [chr(ord("A") + i) for i in range(dist + 1)]
    letters += letters[:-1][::-1]

    return [
        f'{" " * (dist - (ord(l) - ord("A")))}{l}{" " * (2 * (ord(l) - ord("A")) - 1)}{l}{" " * (dist - (ord(l) - ord("A")))}'
        if l != "A"
        else f'{" " * dist}A{" " * dist}'
        for l in letters
    ]

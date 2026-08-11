COLORS = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
def label(colors):
    result = (10 * COLORS.index(colors[0]) + COLORS.index(colors[1])) * (10 ** COLORS.index(colors[2]))
    units = [(1_000_000_000, 'gigaohms'), (1_000_000, 'megaohms'), (1_000, 'kiloohms'), (1, 'ohms')]

    for limit, name in units:
        if result >= limit:
            return f'{result // limit} {name}'
    return '0 ohms'
    
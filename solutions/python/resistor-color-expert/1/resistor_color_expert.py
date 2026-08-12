COLORS = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
UNITS = [(1_000_000_000, 'gigaohms'), (1_000_000, 'megaohms'), (1_000, 'kiloohms'), (1, 'ohms')]
TOLERANCES = {'grey': '0.05%', 'violet': '0.1%', 'blue': '0.25%', 'green': '0.5%', 'brown': '1%', 'red': '2%', 'gold': '5%', 'silver': '10%'}

def resistor_label(colors):
    if len(colors) == 1: return '0 ohms'
    tolerance = TOLERANCES[colors[-1]]
    result = 0
    if len(colors) == 4:
        result = (10 * COLORS.index(colors[0]) + COLORS.index(colors[1])) * (10 ** COLORS.index(colors[2]))
    else:
        result = (100 * COLORS.index(colors[0]) + COLORS.index(colors[1]) * 10 + COLORS.index(colors[2])) * (10 ** COLORS.index(colors[3]))
    
    for limit, name in UNITS:
        if result >= limit:
            value = result / limit
            return f'{value:g} {name} ±{tolerance}'
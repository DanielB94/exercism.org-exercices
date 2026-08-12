COLORS = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
UNITS = [(1_000_000_000, 'gigaohms'), (1_000_000, 'megaohms'), (1_000, 'kiloohms'), (1, 'ohms')]
TOLERANCES = {'grey': '0.05%', 'violet': '0.1%', 'blue': '0.25%', 'green': '0.5%', 'brown': '1%', 'red': '2%', 'gold': '5%', 'silver': '10%'}

def resistor_label(colors):
    if len(colors) == 1: return '0 ohms'

    digits = int(''.join(str(COLORS.index(c)) for c in colors[:-2]))
    
    result = digits * (10 ** COLORS.index(colors[-2]))
    
    for limit, name in UNITS:
        if result >= limit:
            return f"{result / limit:g} {name} ±{TOLERANCES[colors[-1]]}"
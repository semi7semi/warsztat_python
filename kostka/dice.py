import random


print("""
wprowadz jaki rzut chcesz wykonac xDy+z np. '3D6+2'
x - ilosc rzutow
Dy - oznacza rodzaj kosc (D3, D4, D6, D8, D10, D12, D20, D100)
z - modyfikator +/- wartosc
""")


def dice_type(code):
    """funkcja dzieli wprowadzony lancych kodu kosci na czesci
    z ktorych mozna zaimportowac dane do dalszych obliczen

    xDy + z
    split dzieli lancuch na 3 czesci:
    x - liczbe kosci
    Dy - typ kosci
    z - modyfikator"""
    possible_dices = ("D3", "D4", "D6", "D8", "D12", "D20", "D100")
    for i in possible_dices:
        if i in code:
            prefix, sufix = code.split(i)
            return prefix, i, sufix


def roll(data):
    """Symulacja rzutu kosci oraz wykonanie obliczen"""
    result = []
    try:
        n = int(dice_type(data)[1][1:])
    except TypeError:
        return "Zly kod kosci"
    try:
        x = int(dice_type(data)[0])
    except ValueError:
        return "Zła wartosc x"
    try:
        z = int(dice_type(data)[2])
    except ValueError:
        return "Zła wartosc y"
    for _ in range(x):
        dice_value = random.randint(1, n)
        result.append(dice_value)
    wynik = sum(result) + z
    return wynik


print(roll("4D6-2"))
print(roll("3D5+2"))
print(roll("D8+2"))
print(roll("4D8-s"))

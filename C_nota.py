def ne_interval_0_10(v: float) -> bool:
    return 0 <= v <= 10

def pesho_notat(p1: float, p2: float, provim: float) -> float:
    """Kthen mes = p1*0.3 + p2*0.3 + provim*0.4; invalid → -1."""
    if not (ne_interval_0_10(p1) and ne_interval_0_10(p2) and ne_interval_0_10(provim)):
        return -1
    return p1 * 0.3 + p2 * 0.3 + provim * 0.4

def etiketa(mes: float) -> str:
    """<5 'Dobët', 5–6.9 'Mjaftueshëm', 7–8.9 'Mirë', ≥9 'Shkëlqyeshëm'."""
    if mes < 5:
        return 'Dobët'
    elif mes < 7:
        return 'Mjaftueshëm'
    elif mes < 9:
        return 'Mirë'
    else:
        return 'Shkëlqyeshëm'

def nota_finale(p1: float, p2: float, provim: float) -> tuple:
    """Kthen (mes_rounded, etiketa); përdor dy funksionet më sipër."""
    mes = pesho_notat(p1, p2, provim)
    if mes == -1:
        return -1
    mes_rounded = round(mes, 2)
    return (mes_rounded, etiketa(mes_rounded))

# Main
p1 = float(input("p1: "))
p2 = float(input("p2: "))
provim = float(input("provim: "))
rez = nota_finale(p1, p2, provim)

if rez == -1:
    print("Gabim")
else:
    print(f"Mes: {rez[0]} | Etiketa: {rez[1]}")

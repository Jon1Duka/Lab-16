def valido_interval(v: float, min_v: float, max_v: float) -> bool:
    """True nëse min_v <= v <= max_v."""
    return min_v <= v <= max_v

def cmimi_me_tatim(neto: float, tatim_perqind: float) -> float:
    """Kthen neto*(1 + tatim/100); nëse neto<0 ose tatim jashtë [0,100] → -1."""
    if neto < 0 or not valido_interval(tatim_perqind, 0, 100):
        return -1
    return neto * (1 + tatim_perqind / 100)

def rumbullakos_dy_shifra(v: float) -> float:
    """Kthen v të rrumbullakosur në 2 shifra decimale."""
    return round(v, 2)

def cmimi_total(neto: float, tatim_perqind: float, tarifa_fikse: float) -> float:
    """Validim → cmim me tatim → + tarifa → round(2)."""
    cmim_tatimuar = cmimi_me_tatim(neto, tatim_perqind)
    if cmim_tatimuar == -1:
        return -1
    total = cmim_tatimuar + tarifa_fikse
    return rumbullakos_dy_shifra(total)

# Main
neto = float(input("Neto: "))
tatim = float(input("Tatim (%): "))
tarifa = float(input("Tarifa fikse: "))
total = cmimi_total(neto, tatim, tarifa)

if total == -1:
    print("Gabim")
else:
    print(f"Totali: {total}")

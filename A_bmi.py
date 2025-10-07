def valido_pozitiv(x: float) -> bool:
    """Kthen True nëse x > 0, përndryshe False."""
    return x > 0

def llogarit_bmi(pesha_kg: float, gjatesia_m: float) -> float:
    """Kthen BMI = pesha / (gjatesia**2). Nëse inputet jo pozitive → kthe -1."""
    if not (valido_pozitiv(pesha_kg) and valido_pozitiv(gjatesia_m)):
        return -1
    return pesha_kg / (gjatesia_m ** 2)

def kategorizo_bmi(bmi: float) -> str:
    """Kthen etiketë: <18.5 'Nën peshë', 18.5–24.9 'Normal', 25–29.9 'Mbi peshë', ≥30 'Obez'."""
    if bmi < 18.5:
        return 'Nën peshë'
    elif bmi < 25:
        return 'Normal'
    elif bmi < 30:
        return 'Mbi peshë'
    else:
        return 'Obez'

# Main
pesha = float(input("Pesha (kg): "))
gjatesia = float(input("Gjatësia (m): "))
bmi = llogarit_bmi(pesha, gjatesia)

if bmi == -1:
    print("Gabim")
else:
    print(f"BMI: {round(bmi, 2)} - {kategorizo_bmi(bmi)}")

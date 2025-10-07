def trim(s: str) -> str:
    """Heq hapësirat në fillim/fund: s.strip()."""
    return s.strip()

def normalizo_hapesirat(s: str) -> str:
    """Zëvendëson blloqet e shumta të hapësirave me një të vetme."""
    rezultat = ""
    ne_hapesire = False
    for c in s:
        if c == " ":
            if not ne_hapesire:
                rezultat += " "
                ne_hapesire = True
        else:
            rezultat += c
            ne_hapesire = False
    return rezultat

def format_card_title(s: str) -> str:
    """trim → normalizo_hapesirat → kapitalizim i fjalës së parë."""
    s = trim(s)
    s = normalizo_hapesirat(s)
    if len(s) == 0:
        return ""
    return s[0].upper() + s[1:]

# Main
teksti = input("Teksti: ")
titulli = format_card_title(teksti)
print(f"Titulli: {titulli}")

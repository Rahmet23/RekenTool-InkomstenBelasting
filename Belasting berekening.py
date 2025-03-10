# Invoer winst uit onderneming
wuo = float(input('Winst uit onderneming: '))
# Invoer urencriterium
urenctriterium = int(input('Hoeveel uren heb je gewerkt totaal: '))

# Aftrekken en kortingen
zelfstandigafrek = 2470
starteraftrek = 2123

# Dit is de precentage na de MKBvrijstelling
MKBwinstvrijstelling = 0.873

ondernemingaftrek = zelfstandigafrek + starteraftrek
belastbarewuo = wuo - ondernemingaftrek - MKBwinstvrijstelling


# ________________________________________________________________________________________

def urencriteriumtijd(wuo, urenctriterium):

    if urenctriterium > 1224:
        nwwuo = wuo - zelfstandigafrek
        return nwwuo
    else:
        nwwuo = wuo

    return nwwuo

nwwuo = urencriteriumtijd(wuo, urenctriterium)
print(nwwuo)

def zelfstandigenaftrek(nwwuo):
    starteraftreknw = input('Heb je ondernemerrecht op startersaftrek (ja/nee): ').strip().lower()
    if starteraftreknw == 'ja':
        nwwuo = (nwwuo - starteraftrek) * MKBwinstvrijstelling
        return nwwuo
    else:
        nwwuo = nwwuo * MKBwinstvrijstelling
        return nwwuo


nwwuo = zelfstandigenaftrek(nwwuo)
# ________________________________________________________________________________________


# ________________________________________________________________________________________


def belastingtarief(nwwuo):

    schijf2 = 76817
    tarief1 = 0.3748
    tarief3 = 0.495

    belasting = 0

    if nwwuo > schijf2:
        belasting = 14407 + 14383 + ((nwwuo - schijf2) * tarief3)
    else:
        belasting = nwwuo * tarief1

    return belasting
print('beslasting tarief = ', belastingtarief(nwwuo))


# ________________________________________________________________________________________

def metbijheffing(wuo, ondernemingaftrek, MKBwinstvrijstelling):
    bijheffing = 0
    extraheffing1 = (0.1202 * (wuo - 76817))
    if extraheffing1 < 0:
        extraheffing1 = 0
    extraheffing2 = 0.1202 * (ondernemingaftrek + MKBwinstvrijstelling)
    if extraheffing2 > extraheffing1:
        bijheffing = bijheffing + extraheffing1
    else:
        bijheffing = extraheffing2
    return bijheffing
print(metbijheffing(wuo, ondernemingaftrek, MKBwinstvrijstelling))

# ________________________________________________________________________________________

def heffingskorting(nwwuo):
    print(f"NWWUO: {nwwuo}")  # Debug om input te checken
    if nwwuo < 0:
        nwwuo = 0
    # Algemene heffingskorting
    algemene_heffingskorting = 3068 - (max(0, (nwwuo - 28406)) * 0.06337)
    if algemene_heffingskorting < 0:
        algemene_heffingskorting = 0
    print(f"algemene heffing: {algemene_heffingskorting}")

    # Arbeidskorting 1: Controleer of deze minimaal 980 is
    arbeidskorting1 = nwwuo * 0.08053
    if arbeidskorting1 > 980:
        arbeidskorting1 = 980
    print(f"Arbeidskorting 1: {arbeidskorting1}")

    # Arbeidskorting 2
    arbeidskorting2 = arbeidskorting1 + (max(0, (nwwuo - 12169)) * 0.3003)
    if arbeidskorting2 > 5220:
        arbeidskorting2 = 5220
    if arbeidskorting2 < 0:
        arbeidskorting2 = 0
    print(f"Arbeidskorting 2: {arbeidskorting2}")

    # Arbeidskorting 3
    arbeidskorting3 = arbeidskorting2 + (max(0, (nwwuo - 26288)) * 0.02258)
    if arbeidskorting3 > 5599:
        arbeidskorting3 = 5599
    if arbeidskorting3 < 0:
        arbeidskorting3 = 0
    print(f"Arbeidskorting 3: {arbeidskorting3}")

    # Correcte afbouw arbeidskorting
    uiteindelijke_arbeidskorting = arbeidskorting3 - (max(0, (nwwuo - 43071)) * 0.0651)
    if uiteindelijke_arbeidskorting < 0:
        uiteindelijke_arbeidskorting = 0
    print(f"Uiteindelijke Arbeidskorting: {uiteindelijke_arbeidskorting}")

    # Totale heffingskorting
    totale_heffingskorting = algemene_heffingskorting + uiteindelijke_arbeidskorting
    print(f"Totale Heffingskorting: {totale_heffingskorting}")

    return float(totale_heffingskorting)
#print(heffingskorting(nwwuo))


def ZVWbijdragen(nwwuo):
    if nwwuo > 75860:
        nwwuo = 75860
    ZVWBijdragen = nwwuo * 0.0526

    # Zorg ervoor dat de maximale bijdrage niet boven 3990 komt
    if ZVWBijdragen > 3990:
        ZVWBijdragen = 3990

    return ZVWBijdragen

print(ZVWbijdragen(nwwuo))

# ________________________________________________________________________________________

# Eindberekening
belasting = belastingtarief(nwwuo)
bijheffing = metbijheffing(wuo, ondernemingaftrek, MKBwinstvrijstelling)
korting = heffingskorting(nwwuo)
ZVB = ZVWbijdragen(nwwuo)
# Correcte uiteindelijke belasting

# hier regel je dat te betalen belasting niet onder 0 kan
def Laatste(belasting, bijheffing, korting, ZVB):
    laatste = belasting + ZVB + bijheffing - korting
    if laatste < 0:
        laatste = 0
    return laatste
laatste2 = Laatste(belasting, bijheffing, korting, ZVB)

print('___________________________________________________________________')

print(f"belasting: {belasting:.0f}")
print(f"Bijheffing: {bijheffing:.0f}")
print(f"Korting: {korting:.0f}")
print(f"Te betalen belasting: {laatste2:.0f}")


























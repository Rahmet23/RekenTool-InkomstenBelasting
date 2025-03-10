from pathlib import Path
import tkinter as tk
from tkinter import Canvas, Entry, Text, Button, PhotoImage, messagebox

# Zorg ervoor dat dit pad klopt met jouw assets-map
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\rahme\Desktop\Python Project\Projecten\BelastingDataProj\.venv\build\assets\frame0")

print(f"Assets worden geladen vanuit: {ASSETS_PATH}")  # Debug print

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Functie om de belastingberekening uit te voeren
def bereken_belasting():
    try:
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
            arbeidskorting2 = arbeidskorting1 + ((nwwuo - 12169) * 0.3003)
            if arbeidskorting2 > 5220:
                arbeidskorting2 = 5220
            if arbeidskorting2 < 0:
                arbeidskorting2 = 0
            print(f"Arbeidskorting 2: {arbeidskorting2}")

            # Arbeidskorting 3
            arbeidskorting3 = arbeidskorting2 + ((nwwuo - 26288) * 0.02258)
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

        # print(heffingskorting(nwwuo))

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
        laatste = belasting + ZVB + bijheffing - korting
        print(f"Te betalen belasting: {laatste:.2f}")
        print(f"belasting: {belasting:.2f}")
        print(f"Bijheffing: {bijheffing}")
        print(f"Korting: {korting:.2f}")


    except ValueError:
        messagebox.showerror("Input Fout", "Voer geldige numerieke waarden in.")




# Koppel de functie aan de knop ZONDER de GUI te veranderen
#button_1.config(command=bereken_belasting)


# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer




window = tk.Tk()
window.geometry("1440x1024")
window.configure(bg="#2D26FF")


canvas = Canvas(
    window,
    bg = "#2D26FF",
    height = 1024,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
#Rectangle voor achtergrond
canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    23.0,
    19.0,
    338.0,
    1004.0,
    fill="#402E4B",
    outline="")

canvas.create_text(
    73.0,
    243.0,
    anchor="nw",
    text="Settings",
    fill="#FFFFFF",
    font=("Ligconsolata Bold", 48 * -1)
)

canvas.create_text(
    71.0,
    125.0,
    anchor="nw",
    text="Profiel",
    fill="#FFFFFF",
    font=("Ligconsolata Bold", 48 * -1)
)

canvas.create_text(
    71.0,
    58.0,
    anchor="nw",
    text="Hoofdmenu",
    fill="#FFFFFF",
    font=("Ligconsolata Bold", 48 * -1)
)

canvas.create_text(
    60.0,
    193.0,
    anchor="nw",
    text="Account Settings",
    fill="#FFFFFF",
    font=("Ligconsolata Bold", 30 * -1)
)

canvas.create_text(
    435.0,
    54.0,
    anchor="nw",
    text="Belasting Analyse",
    fill="#402E4B",
    font=("Ligconsolata Bold", 96 * -1)
)

#Rectangle voor achtergrond
canvas.create_rectangle(
    370.0,
    208.0,
    1408.0,
    1004.0,
    fill="#402E4B",
    outline="")

canvas.create_text(
    481.0,
    417.0,
    anchor="nw",
    text="Recht op Startersafterk (Ja/Nee):",
    fill="#FFFFFF",
    font=("Ligconsolata Bold", 20 * -1)
)

canvas.create_text(
    481.0,
    572.0,
    anchor="nw",
    text="Uitkomst Ingevoerde Antwoord:",
    fill="#FFFFFF",
    font=("Ligconsolata Bold", 20 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    829.5,
    463.0,
    image=entry_image_1
)
#entry_1 hier komt dus ja of nee te staan.
entry_1 = Entry(
    bd=0,
    bg="#99A1F5",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=481.0,
    y=443.0,
    width=697.0,
    height=38.0
)

canvas.create_text(
    481.0,
    328.0,
    anchor="nw",
    text="Totaal Gewerkte Uren:",
    fill="#FFFFFF",
    font=("Ligconsolata Bold", 20 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    829.5,
    377.0,
    image=entry_image_2
)
#Entry_2 Hier komt mijn gewerkte uren te staan.
entry_2 = Entry(
    bd=0,
    bg="#99A1F5",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=481.0,
    y=357.0,
    width=697.0,
    height=38.0
)

canvas.create_text(
    481.0,
    230.0,
    anchor="nw",
    text="Winst Uit Onderneming:",
    fill="#FFFFFF",
    font=("Ligconsolata Bold", 20 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    829.5,
    284.0,
    image=entry_image_3
)
#entry_3 Hier in komt WUO dus wanneer ik run moet ik eerst hier mijn wuo invoeren.
entry_3 = Entry(
    bd=0,
    bg="#99A1F5",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=481.0,
    y=264.0,
    width=697.0,
    height=38.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    829.5,
    666.5,
    image=entry_image_4
)
#entry_4 hier komt alle text van de antwoorden van mijn belasting berekening
entry_4 = Text(
    bd=0,
    bg="#99A1F5",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=481.0,
    y=598.0,
    width=697.0,
    height=135.0
)
# button_image_1 en alles met button onder hier is dus wanneer ik er op klik dat dan al mijn ingevoerde gegevens worden geprint en dan bij entry_4 worden geprint en zichtbaar
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))

# Knop plaatsen
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=bereken_belasting,  # **De knop start de berekening**
    relief="flat"
)
button_1.place(x=449.0, y=508.0, width=162.0, height=52.0)

window.resizable(False, False)
window.mainloop()

file = open("spese.txt", "r")
spese = []

contenuto = file.read()

righe = contenuto.split("\n")

for riga in righe:

    if riga == "":
        continue

    parti = riga.split("-")

    descrizione = parti[0]

    importo = float(parti[1])

    spesa = {
        "descrizione": descrizione,
        "importo": importo
    }

    spese.append(spesa)

file.close()
file = open("spese.txt", "a")
while True:

    descrizione = input("Inserisci una spesa (scrivi fine per terminare): ")

    if descrizione.lower() == "fine":
        break

    costo = float(input("Inserisci il costo della spesa: "))

    spesa = {
        "descrizione": descrizione,
        "importo": costo
    }

    spese.append(spesa)

    file.write(f"{spesa['descrizione']} - {spesa['importo']:.2f}\n")


totale_spese = 0
totale = len(spese)

if totale == 0:
    print("Non hai aggiunto nessun elemento")

else:
    print()
    print(f"Hai inserito {totale} spese.")
    print("Hai inserito:")

    # Calcolo totale e salvataggio nel file
    for spesa in spese:
        print(f" -{spesa['descrizione']} - {spesa['importo']:.2f} €")
        totale_spese = totale_spese + spesa["importo"]

    # Calcolo massimo
    massimo = spese[0]["importo"]

    for spesa in spese:
        if spesa["importo"] > massimo:
            massimo = spesa["importo"]

    # Calcolo minimo
    minimo = spese[0]["importo"]

    for spesa in spese:
        if spesa["importo"] < minimo:
            minimo = spesa["importo"]

    # Calcolo media
    media = totale_spese / totale

    # Risultati
    print()
    print(f"Totale: {totale_spese:.2f} €")
    print(f"Media: {media:.2f} €")
    print(f"Spesa più alta: {massimo:.2f} €")
    print(f"Spesa più bassa: {minimo:.2f} €")


file.close()
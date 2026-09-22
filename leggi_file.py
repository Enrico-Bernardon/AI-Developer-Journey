file = open("spese.txt", "r")

contenuto = file.read()

righe = contenuto.split("\n")

spese = []

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
totale_spese = 0 
totale = len(spese)
if totale == 0:
    print("Non hai aggiunto nessun elemento")

else:
    print()
    print(f"Hai inserito {totale} spese.")
    print("Hai inserito:")

    for spesa in spese:
        print(f" -{spesa['descrizione']} - {spesa['importo']:.2f} €")
        totale_spese = totale_spese + spesa["importo"]

    massimo = spese[0]["importo"]

    for spesa in spese:
        if spesa["importo"] > massimo:
            massimo = spesa["importo"]

    minimo = spese[0]["importo"]

    for spesa in spese:
        if spesa["importo"] < minimo:
            minimo = spesa["importo"]
    

    media = totale_spese / totale


    print(f"Totale: {totale_spese:.2f} €")
    print(f"Media: {media:.2f} €")
    print(f"Spesa più alta: {massimo:.2f} €")
    print(f"Spesa più bassa: {minimo:.2f} €")

print(spese)
file.close()
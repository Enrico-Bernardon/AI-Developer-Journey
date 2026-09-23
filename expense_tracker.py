#Funzione per il Totale
def calcola_totale(spese):
    totale = 0

    for spesa in spese:
        totale = totale + spesa["importo"]

    return totale
#Funzione per la Media
def calcola_media(spese):
    totale = calcola_totale(spese)
    return totale / len(spese)
#Funzione per trovare il Massimo
def trova_massimo(spese):
    massimo = spese[0]["importo"]

    for spesa in spese:
        if spesa["importo"] > massimo:
            massimo = spesa["importo"]

    return massimo
#Funzione per trovare il Minimo
def trova_minimo(spese):
    minimo = spese[0]["importo"]

    for spesa in spese:
        if spesa["importo"] < minimo:
            minimo = spesa["importo"]

    return minimo
#Funzione per Caricare la Spesa
def carica_spese():
    spese = []

    try:
        file = open("spese.txt", "r")

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

    except FileNotFoundError:
        file = open("spese.txt", "w")
        file.close()

    return spese
#Funzione che aggiunge una singola Spesa
def aggiungi_spesa(spese, file, descrizione):
    costo = float(input("Inserisci il costo della spesa: "))

    spesa = {
        "descrizione": descrizione,
        "importo": costo
    }

    spese.append(spesa)
    file.write(f"{spesa['descrizione']} - {spesa['importo']:.2f}\n")
spese = carica_spese()

file = open("spese.txt", "a")

while True:

    descrizione = input("Inserisci una spesa (scrivi fine per terminare): ")

    if descrizione.lower() == "fine":
        break

    aggiungi_spesa(spese, file, descrizione)

numero_spese = len(spese)

if numero_spese == 0:
    print("Non hai aggiunto nessun elemento")

else:
    print()
    print(f"Hai inserito {numero_spese} spese.")
    print("Hai inserito:")

    for spesa in spese:
        print(f" -{spesa['descrizione']} - {spesa['importo']:.2f} €")

    # Calcolo totale 
    totale_spese = calcola_totale(spese)

    # Calcolo media
    media = calcola_media(spese)

    # Calcolo massimo
    massimo = trova_massimo(spese)

    # Calcolo minimo
    minimo = trova_minimo(spese)


    # Risultati
    print()
    print(f"Totale: {totale_spese:.2f} €")
    print(f"Media: {media:.2f} €")
    print(f"Spesa più alta: {massimo:.2f} €")
    print(f"Spesa più bassa: {minimo:.2f} €")


file.close()
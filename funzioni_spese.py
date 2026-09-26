#Funzione per calcolare il Totale
def calcola_totale(spese):
    totale = 0

    for spesa in spese:
        totale = totale + spesa["importo"]

    return totale

#Funzione per calcolare la Media
def calcola_media(spese):
    totale = calcola_totale(spese)

    return totale / len(spese)
#Funzione trovare il Massimo
def trova_massimo(spese):
    massimo = spese[0]["importo"]

    for spesa in spese:
        if spesa["importo"] > massimo:
            massimo = spesa["importo"]

    return massimo
#Funzione trovare il Minimo
def trova_minimo(spese):
    minimo = spese[0]["importo"]

    for spesa in spese:
        if spesa["importo"] < minimo:
            minimo = spesa["importo"]

    return minimo
#Funzione per caricare la spesa
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
#Funzione per aggiungere la spesa
def aggiungi_spesa(spese, file):
    #Ciclo per vedere se la spesa è Vuota 
    while True:
        descrizione = input("Inserisci la descrizione della spesa: ")

        descrizione = descrizione.strip()

        if descrizione == "":
            print("La descrizione non può essere vuota.")
        else:
            break
    #Ciclo per vedere se il costo è >0 
    while True:
        try:
            costo = float(input("Inserisci il costo della spesa: "))

            if costo < 0:
                print("Il costo deve essere maggiore di 0.")
            else:
                break

        except ValueError:
            print("Inserisci un numero valido.")

    spesa = {
        "descrizione": descrizione,
        "importo": costo
    }

    spese.append(spesa)
    file.write(f"{spesa['descrizione']} - {spesa['importo']:.2f}\n")

#Funzione per mostrare la spesa
def mostra_spese(spese):
     for spesa in spese:
        print(f" -{spesa['descrizione']} - {spesa['importo']:.2f} €")
#Funzione per mostrare le statistiche 
def mostra_statistiche(spese):
    numero_spese = len(spese)

    if numero_spese == 0:
        print("Non hai aggiunto nessun elemento")

    else:
        print(f"Hai inserito {numero_spese} spese.")

        totale_spese = calcola_totale(spese)
        media = calcola_media(spese)
        massimo = trova_massimo(spese)
        minimo = trova_minimo(spese)

        print(f"Totale: {totale_spese:.2f} €")
        print(f"Media: {media:.2f} €")
        print(f"Spesa più alta: {massimo:.2f} €")
        print(f"Spesa più bassa: {minimo:.2f} €")
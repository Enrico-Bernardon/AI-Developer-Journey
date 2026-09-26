#Creato import per rendere più pulito il file
from funzioni_spese import (
    calcola_totale,
    calcola_media,
    trova_massimo,
    trova_minimo,
    carica_spese,
    aggiungi_spesa,
    mostra_spese,
    mostra_statistiche
)

spese = carica_spese()

file = open("spese.txt", "a")

#Ciclo per creare un menu interagibile
while True:
    print("===== EXPENSE TRACKER =====")
    print("1. Aggiungi spesa")
    print("2. Visualizza spese")
    print("3. Mostra statistiche")
    print("4. Esci")

    scelta = input("Scegli un'opzione: ")

    if scelta == "1":
        aggiungi_spesa(spese, file)

    elif scelta == "2":
        mostra_spese(spese)

    elif scelta == "3":
        mostra_statistiche(spese)

    elif scelta == "4":
        break

    else:
        print("Scelta non valida. Inserisci un'opzione da 1 a 4.")

file.close()





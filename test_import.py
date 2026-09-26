from funzioni_spese import (
    calcola_totale,
    calcola_media,
    trova_massimo,
    trova_minimo
)

spese = [
    {"descrizione": "Pizza", "importo": 10},
    {"descrizione": "Cinema", "importo": 25},
    {"descrizione": "Benzina", "importo": 50},
    {"descrizione": "Spesa", "importo": 15}
]

print(f"Totale: {calcola_totale(spese)}")
print(f"Media: {calcola_media(spese)}")
print(f"Massimo: {trova_massimo(spese)}")
print(f"Minimo: {trova_minimo(spese)}")

from funzioni_spese import (
    calcola_totale,
    calcola_media,
    trova_massimo,
    trova_minimo,
    carica_spese
)

spese = carica_spese()

print(spese)

from funzioni_spese import aggiungi_spesa

spese = []

file = open("spese.txt", "a")

aggiungi_spesa(spese, file)

file.close()

from funzioni_spese import mostra_spese
mostra_spese(spese)

from funzioni_spese import mostra_statistiche
spese = []

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
    
    
    
    
    
    totale_spese = 0


 
totale = len(spese) 

if totale == 0:
   print("Non hai aggiunto nessun elemento")
else:
    print()
    print(f"Hai inserito {totale} spese.")
    print("Hai inserito:")

    for spesa in spese:
      print(f" -{spesa['descrizione']} - {spesa['importo']}")
      totale_spese = totale_spese + spesa['importo']

print(totale_spese)
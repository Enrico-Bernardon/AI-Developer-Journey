spese = []

while True:

    descrizione = input("Inserisci una spesa (scrivi fine per terminare): ")
    costo = input("Inserisci il costo della spesa (scrivi fine per terminare): " )

     
    if descrizione.lower() == "fine":
        
         break
     
    spesa = {
    "descrizione": descrizione,
    "importo": costo
}
        
    
        
    

    spese.append(spesa)
    

 
totale = len(spese) 

if totale == 0:
   print("Non hai aggiunto nessun elemento")
else:
    print()
    print(f"Hai inserito {totale} spese.")
    print("Hai inserito:")

    for spesa in spese:
      print(f" -{spesa['descrizione']} - {spesa['importo']}")
     
    

   

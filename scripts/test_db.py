import sys
import os

# Aggiungiamo la cartella root al percorso di ricerca di Python 
# così possiamo importare i nostri moduli anche se eseguiamo lo script da qui.
sys.path.append(os.getcwd())

from apps.api.database import SessionLocal, engine
from apps.api import models
from datetime import datetime

def test_db():
    print("--- TEST DATABASE SPESOMETRO ---")
    
    # 1. Creiamo le tabelle (se non esistono già)
    print("Inizializzazione tabelle...")
    models.Base.metadata.create_all(bind=engine)
    
    # 2. Apriamo una sessione di test
    db = SessionLocal()
    
    try:
        # 3. Creiamo uno scontrino di test
        print("Inserimento scontrino di prova...")
        test_receipt = models.Receipt(
            store_name="Supermercato AI",
            total_amount=10.50,
            date=datetime.now(),
            status="draft"
        )
        db.add(test_receipt)
        db.flush() # Otteniamo l'ID senza salvare definitivamente
        
        # 4. Aggiungiamo un prodotto allo scontrino
        print(f"Inserimento prodotto per lo scontrino ID: {test_receipt.id}...")
        test_item = models.Item(
            name="Pane fresco",
            price=1.50,
            quantity=1.0,
            category="Alimentari",
            receipt_id=test_receipt.id
        )
        db.add(test_item)
        
        # 5. Salviamo (Commit)
        db.commit()
        print("Dati salvati con successo!")
        
        # 6. Verifica: Leggiamo i dati appena scritti
        print("\nVerifica lettura dati:")
        receipts = db.query(models.Receipt).all()
        for r in receipts:
            print(f"- Scontrino ID {r.id}: {r.store_name} ({r.total_amount}€)")
            for i in r.items:
                print(f"  > Prodotto: {i.name} - {i.price}€")
                
    except Exception as e:
        print(f"ERRORE DURANTE IL TEST: {e}")
        db.rollback()
    finally:
        # Chiudiamo sempre la sessione!
        db.close()

if __name__ == "__main__":
    test_db()

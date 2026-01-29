from typing import List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, database, schemas

# --- INIZIALIZZAZIONE ---

# Creiamo le tabelle nel database basandoci sui modelli definiti in models.py
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Spesometro API")

# --- ROTTE (ENDPOINT) ---

@app.get("/", tags=["Generale"])
def read_root():
    """Pagina di benvenuto dell'API."""
    return {
        "message": "Benvenuto in Spesometro API", 
        "docs": "/docs",
        "db_status": "initialized"
    }

@app.post("/receipts/", response_model=schemas.Receipt, tags=["Scontrini"])
def create_receipt(receipt: schemas.ReceiptCreate, db: Session = Depends(database.get_db)):
    """
    Crea un nuovo scontrino nel database insieme ai suoi prodotti.
    
    - 'db: Session = Depends(...)': Chiediamo a FastAPI di fornirci una sessione del DB 
      usando la funzione get_db che abbiamo definito prima.
    """
    # 1. Creiamo l'oggetto scontrino (Receipt) dai dati ricevuti
    db_receipt = models.Receipt(
        store_name=receipt.store_name,
        total_amount=receipt.total_amount,
        date=receipt.date,
        status=receipt.status
    )
    
    # 2. Aggiungiamo lo scontrino alla sessione del DB
    db.add(db_receipt)
    db.flush() # flush() genera l'ID dello scontrino senza salvare definitivamente (commit)
    
    # 3. Creiamo e colleghiamo i prodotti (items)
    for item_data in receipt.items:
        db_item = models.Item(**item_data.model_dump(), receipt_id=db_receipt.id)
        db.add(db_item)
    
    # 4. Salviamo tutto definitivamente nel file .db
    db.commit()
    # 5. Rinfreschiamo l'oggetto per avere tutti i dati aggiornati (incluso l'ID)
    db.refresh(db_receipt)
    
    return db_receipt

@app.get("/receipts/", response_model=List[schemas.Receipt], tags=["Scontrini"])
def read_receipts(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    """
    Legge la lista degli scontrini salvati.
    
    - 'skip': quanti scontrini saltare (per la paginazione)
    - 'limit': massimo numero di scontrini da restituire
    """
    receipts = db.query(models.Receipt).offset(skip).limit(limit).all()
    return receipts

@app.get("/health", tags=["Generale"])
def health():
    """Controllo dello stato di salute del sistema."""
    return {"status": "ok"}

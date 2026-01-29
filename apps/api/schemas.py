from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import datetime

# --- SCHEMI DI VALIDAZIONE (PYDANTIC) ---
# In FastAPI, usiamo Pydantic per definire la "forma" dei dati che 
# viaggiano attraverso le nostre API. 
# Immaginali come dei contratti: se i dati non rispettano questa forma, 
# FastAPI risponderà automaticamente con un errore.

class ItemBase(BaseModel):
    """
    Schema base per un prodotto. 
    Contiene le proprietà comuni sia alla creazione che alla lettura.
    """
    name: str
    quantity: float = 1.0
    price: float
    category: str = "Altro"

class ItemCreate(ItemBase):
    """
    Schema usato quando creiamo un nuovo prodotto.
    Identico alla base, ma separato per chiarezza futura (es. validazioni extra).
    """
    pass

class Item(ItemBase):
    """
    Schema per la lettura di un prodotto.
    Include l'ID che viene generato dal database.
    """
    id: int
    receipt_id: int

    # Configurazione per permettere a Pydantic di leggere dati da oggetti del DB (SQLAlchemy)
    model_config = ConfigDict(from_attributes=True)


class ReceiptBase(BaseModel):
    """
    Schema base per uno scontrino.
    """
    store_name: str
    date: Optional[datetime] = None
    total_amount: float
    status: str = "draft"

class ReceiptCreate(ReceiptBase):
    """
    Schema usato per creare uno scontrino.
    Includiamo subito anche i prodotti relativi se presenti.
    """
    items: List[ItemCreate] = []

class Receipt(ReceiptBase):
    """
    Schema completo per la lettura dello scontrino.
    Include l'ID e la lista completa dei prodotti (Items).
    """
    id: int
    items: List[Item] = []

    # Permette la conversione automatica da modello SQLAlchemy a schema Pydantic
    model_config = ConfigDict(from_attributes=True)

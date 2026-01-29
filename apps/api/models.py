from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

# --- MODELLI DEL DATABASE ---
# In SQLAlchemy, ogni classe rappresenta una tabella nel database.

class Receipt(Base):
    """
    Rappresenta uno scontrino intero.
    """
    __tablename__ = "receipts"

    # id: Chiave primaria (univoca per ogni scontrino)
    id = Column(Integer, primary_key=True, index=True)
    
    # store_name: Nome del negozio (es. 'Conad', 'Esselunga')
    store_name = Column(String)
    
    # date: Data e ora dello scontrino (default: ora attuale se non specificata)
    date = Column(DateTime, default=datetime.utcnow)
    
    # total_amount: Totale speso (es. 45.50)
    total_amount = Column(Float)
    
    # image_path: Percorso del file immagine salvato sul server
    image_path = Column(String, nullable=True)
    
    # status: Stato dello scontrino ('draft' = da revisionare, 'confirmed' = ok)
    status = Column(String, default="draft")

    # Relazione con i prodotti: 
    # Uno scontrino (Receipt) può avere molti prodotti (Items).
    items = relationship("Item", back_populates="receipt", cascade="all, delete-orphan")

class Item(Base):
    """
    Rappresenta un singolo prodotto all'interno di uno scontrino.
    """
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    
    # rreceipt_id: Questa colonna collega il prodotto allo scontrino corrispondente (Foreign Key).
    receipt_id = Column(Integer, ForeignKey("receipts.id"))
    
    # name: Nome del prodotto (es. 'Mele')
    name = Column(String)
    
    # quantity: Quantità (es. 2.0)
    quantity = Column(Float, default=1.0)
    
    # price: Prezzo unitario o totale del prodotto
    price = Column(Float)
    
    # category: Categoria (es. 'Alimentari', 'Casa')
    category = Column(String, default="Altro")

    # Relazione inversa: ogni prodotto appartiene a uno scontrino (Receipt).
    receipt = relationship("Receipt", back_populates="items")

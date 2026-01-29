from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# --- CONFIGURAZIONE DATABASE ---
# Creiamo la cartella 'data' se non esiste. Qui verrà salvato il file del database SQLite.
os.makedirs("data", exist_ok=True)

# Definiamo l'indirizzo del database. 
# 'sqlite:///...' indica che useremo un file locale chiamato spesometro.db
SQLALCHEMY_DATABASE_URL = "sqlite:///./data/spesometro.db"

# L'engine è il "motore" che gestisce la connessione fisica al file del database.
# 'check_same_thread: False' serve solo per SQLite quando usato con FastAPI.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# SessionLocal è una classe che useremo per creare ogni singola "sessione" di lavoro
# (pensa a una sessione come a un'operazione di apertura e chiusura del database).
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base è la classe da cui erediteranno tutti i nostri modelli (tabelle).
# Serve a SQLAlchemy per mappare le classi Python alle tabelle del DB.
Base = declarative_base()

# Questa funzione (Dependency) serve a FastAPI per fornirci una connessione al DB
# in modo pulito: la apre quando serve e la chiude automaticamente dopo l'uso.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

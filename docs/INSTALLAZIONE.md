# Avvio locale (dev)

## 1) Crea e attiva un virtualenv
```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate  # Windows
```

## 2) Installa le dipendenze
```bash
pip install -r requirements.txt
```

## 3) Avvia l'API (Backend)
In un terminale separato:
```bash
uvicorn apps.api.main:app --reload
```
L'API sarà disponibile su `http://localhost:8000`.

## 4) Avvia l'interfaccia (Frontend)
In un altro terminale:
```bash
streamlit run apps/ui/app.py
```
L'interfaccia sarà disponibile su `http://localhost:8501`.

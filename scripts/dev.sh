#!/bin/bash

# Funzione per fermare i processi all'uscita
cleanup() {
    echo ""
    echo "Spegnimento server in corso..."
    kill $API_PID 2>/dev/null
    exit
}

# Cattura l'interruzione (Ctrl+C)
trap cleanup SIGINT SIGTERM

# Vai alla root del progetto
cd "$(dirname "$0")/.."

# Verifica se il venv esiste
if [ -d ".venv" ]; then
    echo "Attivazione ambiente virtuale..."
    source .venv/bin/activate
else
    echo "ERRORE: Ambiente virtuale (.venv) non trovato."
    echo "Esegui prima: python -m venv .venv && pip install -r requirements.txt"
    exit 1
fi

echo "---------------------------------------"
echo "🚀 Avvio Spesometro in modalità Sviluppo"
echo "---------------------------------------"

# 1. Avvio API (Backend) in background
echo "📦 Avvio API su http://localhost:8000..."
uvicorn apps.api.main:app --host 0.0.0.0 --port 8000 --reload &
API_PID=$!

# Aspetta un attimo che l'API sia pronta
sleep 2

# 2. Avvio Streamlit (UI)
echo "🎨 Avvio UI su http://localhost:8501..."
streamlit run apps/ui/app.py --server.port 8501 --server.address 0.0.0.0

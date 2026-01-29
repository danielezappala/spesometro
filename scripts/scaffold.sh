#!/usr/bin/env bash
set -euo pipefail

PROJECT_NAME="${1:-spesometro}"

mkdir -p "$PROJECT_NAME"/{apps/api,apps/ui,test_data/receipts,data/receipts}

# requirements
cat > "$PROJECT_NAME/requirements.txt" << 'EOF'
fastapi
uvicorn[standard]
streamlit
pydantic
python-multipart
EOF

# FastAPI hello
cat > "$PROJECT_NAME/apps/api/main.py" << 'EOF'
from fastapi import FastAPI

app = FastAPI(title="Spesometro API")

@app.get("/health")
def health():
    return {"status": "ok"}
EOF

# Streamlit hello (calls API health)
cat > "$PROJECT_NAME/apps/ui/app.py" << 'EOF'
import os
import requests
import streamlit as st

st.set_page_config(page_title="Spesometro", layout="centered")
st.title("Spesometro (MVP)")

api_url = os.getenv("SPESOMETRO_API_URL", "http://localhost:8000")

st.caption(f"API: {api_url}")

if st.button("Check API"):
    try:
        r = requests.get(f"{api_url}/health", timeout=3)
        st.success(r.json())
    except Exception as e:
        st.error(f"API non raggiungibile: {e}")

st.divider()
st.subheader("Upload scontrino (placeholder)")
st.file_uploader("Carica una foto dello scontrino", type=["jpg", "jpeg", "png"])
EOF

# .gitignore additions (keeps repo clean)
cat > "$PROJECT_NAME/.gitignore" << 'EOF'
# Python
__pycache__/
*.py[cod]
.venv/
venv/
.env

# Local runtime data (NOT versioned)
data/
*.db

# OS/editor
.DS_Store
.idea/
.vscode/
EOF

# Minimal run instructions
cat > "$PROJECT_NAME/LOCAL_RUN.md" << 'EOF'
# Avvio locale (dev)

## 1) Crea e attiva un virtualenv
```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# .venv\\Scripts\\activate  # Windows

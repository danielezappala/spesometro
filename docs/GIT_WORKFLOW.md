# Workflow Git per il Team

Per collaborare in modo ordinato su Spesometro, seguiamo questa strategia di ramificazione (branching).

## I Branch Principali

1. **`main`**: È il ramo "sacro". Contiene solo codice stabile e testato. Non si lavora mai direttamente qui.
2. **`dev`**: È il ramo di integrazione. Qui convergono i lavori di tutti gli sviluppatori prima di finire nel `main`.

## Branch di Lavoro Personali
Ogni sviluppatore lavora sul proprio ramo dedicato:
- `daniele/dev`
- `giuseppe/dev`
- `...`

## Flusso di Lavoro (Esempio per Giuseppe)

### 1. Iniziare a lavorare
Se vuoi partire dal lavoro attuale di Daniele:
```bash
git fetch origin
git checkout -b giuseppe/dev origin/daniele/dev
```

### 2. Salvare e pubblicare il lavoro
```bash
git add .
git commit -m "Descrizione chiara della modifica"
git push -u origin giuseppe/dev
```

### 3. Integrare le modifiche (Merge)
Quando una funzionalità è pronta, si richiede l'unione del proprio branch verso il branch `dev` (tramite Pull Request su GitHub).

## Promemoria Credenziali
Per il push, GitHub richiede un **Personal Access Token** invece della password standard. Se Git rimane bloccato, usa:
`git config --global credential.helper store`
Così dovrai inserire il token una sola volta.

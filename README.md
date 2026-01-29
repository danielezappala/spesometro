# Spesometro

## Descrizione

**Spesometro** è un progetto MVP pensato per registrare scontrini (in particolare del supermercato) e analizzare le spese in modo semplice e incrementale.

L’obiettivo principale non è l’automazione perfetta, ma **ottenere dati affidabili grazie alla revisione dell’utente** e ricavare insight chiari su cosa incide di più sulla spesa.

---

## 📚 Documentazione Tecnica

Abbiamo organizzato la documentazione in sezioni specifiche nella cartella `docs/`:

1.  🚀 **[Guida all'Installazione](./docs/INSTALLAZIONE.md)**: Come configurare l'ambiente e avviare i server.
2.  🗄️ **[Struttura Database](./docs/DATABASE.md)**: Dettagli sulle tabelle e le relazioni dei dati.
3.  🌿 **[Workflow Git](./docs/GIT_WORKFLOW.md)**: Come collaborare tra più sviluppatori usando i branch.

---

## 🚧 Stato del progetto (MVP)

Il progetto è attualmente in fase di sviluppo attivo sull'integrazione Backend-Frontend.

### Funzionalità Core (In Sviluppo)
*   [x] Scaffolding Progetto (FastAPI + Streamlit)
*   [x] Database SQLite e Modelli Dati
*   [x] API per creazione e lettura scontrini
*   [ ] Caricamento immagini scontrini
*   [ ] Integrazione Motore OCR/AI per estrazione prodotti
*   [ ] Dashboard statistiche Streamlit

---

## Metodo di lavoro
* Cicli brevi (1–2 settimane)
* Prima funziona, poi si migliora
* Refactoring solo dopo aver dimostrato valore
* Uso di AI consentito seguendo le regole in `.agent/custom_rules.md`

---

## Licenza
MIT

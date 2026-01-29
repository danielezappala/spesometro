# Spesometro

## Descrizione

**Spesometro** è un progetto MVP pensato per registrare scontrini (in particolare del supermercato) e analizzare le spese in modo semplice e incrementale.

L’obiettivo principale non è l’automazione perfetta, ma **ottenere dati affidabili grazie alla revisione dell’utente** e ricavare insight chiari su cosa incide di più sulla spesa.

---

## Obiettivo dell’MVP

> Caricare una foto di scontrino, ottenere la lista prodotti (nome, quantità, prezzo), correggerla manualmente e visualizzare la **percentuale di spesa per categoria**.

---

## Funzionalità incluse (MVP)

* Caricamento di una **foto dello scontrino**
* Estrazione di un **elenco prodotti** (nome, quantità, prezzo)
* **Correzione manuale** dei prodotti:

  * modifica
  * eliminazione
  * aggiunta
* Assegnazione a **categorie fisse predefinite**
* Aggregazione di più scontrini
* Statistica principale:

  * **percentuale di spesa per categoria**

---

## Fuori scope (per ora)

* Multi‑utente / login
* Categorie personalizzabili
* Analisi avanzate o predittive
* UI raffinata

---

## Stack tecnologico

* **Python**
* **FastAPI** – API backend
* **SQLite** – persistenza locale dei dati
* **Streamlit** – interfaccia utente minimale

Lo stack è volutamente semplice per favorire:

* rapidità di sviluppo
* facilità di apprendimento
* iterazioni frequenti

---

## Stato del progetto

🚧 **MVP in sviluppo**
Il progetto viene sviluppato per cicli brevi, con focus su funzionalità funzionanti prima dell’ottimizzazione.

---

## Metodo di lavoro

* Cicli brevi (1–2 settimane)
* Prima funziona, poi si migliora
* Refactoring solo dopo aver dimostrato valore
* Uso di AI consentito, con responsabilità di comprensione del codice

---

## Setup rapido (scaffolding)
Per rigenerare lo scaffolding di base (struttura cartelle + file minimi):

```bash
bash scripts/scaffold.sh

---

## Avvio del progetto

(Istruzioni verranno aggiunte dopo il setup iniziale.)

---

## Licenza

MIT


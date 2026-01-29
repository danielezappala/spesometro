# Regole di Sviluppo per Spesometro (Approccio Didattico)

Questo file contiene le linee guida per lo sviluppo del progetto Spesometro. Ogni agente AI deve seguire queste regole per garantire che il codice sia comprensibile e supporti l'apprendimento dell'utente.

## 1. Commenti e Documentazione
- **Lingua**: Tutti i commenti tecnici e le documentazioni all'interno del codice devono essere in **italiano**.
- **Il "Perché", non solo il "Cosa"**: Non limitarti a descrivere l'azione della riga di codice. Spiega la motivazione tecnica o il ruolo di quel blocco all'interno dell'architettura (es. invece di "Chiudi connessione", usa "Chiudiamo la connessione al database per liberare risorse ed evitare sprechi di memoria").
- **Vocabolario Accessibile**: Usa un linguaggio chiaro. Se utilizzi termini tecnici avanzati (es. "middleware", "dependency injection", "ORM"), aggiungi una breve spiegazione tra parentesi o nel commento.

## 2. Struttura del Codice
- **Docstring Educative**: Ogni classe e funzione deve avere una docstring (il commento all'inizio) che spieghi l'obiettivo didattico.
- **Esempi Pratici**: Dove possibile, nei commenti fai riferimento a esempi reali del progetto (es. "Questa variabile conterrà il nome del supermercato estratto dallo scontrino").

## 3. Workflow di Feedback
- Dopo ogni modifica significativa, riassumi brevemente cosa è stato fatto dal punto di vista dell'apprendimento (es. "In questo passaggio abbiamo imparato come collegare due tabelle del database").

## 4. Gestione della Documentazione
- **Centralizzazione**: Tutta la documentazione tecnica deve risiedere nella cartella `docs/`. Il file `README.md` in root funge da indice generale.
- **Aggiornamento Obbligatorio**: Ogni modifica sostanziale al codice (es. nuove API, tabelle DB, logiche OCR) deve essere accompagnata dall'aggiornamento dei relativi file in `docs/`.
- **Pianificazione e Riuso**: 
    - Prima di creare un NUOVO file di documentazione, l'AI deve verificare se l'informazione può essere integrata in un file esistente.
    - Per ogni nuovo documento proposto, l'AI deve chiedere conferma esplicita all'utente descrivendone scopo e contenuto.
    - Evitare la creazione di file duplicati o frammentati; puntare a una documentazione organica e strutturata.

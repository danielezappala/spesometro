# Documentazione Database

In Spesometro utilizziamo **SQLite** come database per la sua semplicità e portabilità (tutti i dati sono salvati in un singolo file locale).

## Percorso del file
Il database si trova in: `data/spesometro.db`

## Modelli (Tabelle)

### 1. Scontrini (`Receipt`)
Rappresenta l'entità principale caricata dall'utente.
- `id`: Identificativo univoco.
- `store_name`: Nome del supermercato o negozio.
- `date`: Data e ora dell'acquisto.
- `total_amount`: Somma totale indicata sullo scontrino.
- `image_path`: Percorso dell'immagine originale sul server.
- `status`: Stato della revisione (`draft` o `confirmed`).

### 2. Prodotti (`Item`)
Rappresenta i singoli articoli estratti da uno scontrino.
- `id`: Identificativo univoco del prodotto.
- `receipt_id`: Collegamento (Foreign Key) allo scontrino di appartenenza.
- `name`: Nome o descrizione del prodotto.
- `quantity`: Quantità (es. 2 confezioni, 0.5kg).
- `price`: Prezzo dell'articolo.
- `category`: Categoria merceologica (es. Alimentari, Casa).

## Relazione
Esiste una relazione **Uno-a-Molti** tra `Receipt` e `Item`.
- Uno scontrino può contenere molti prodotti.
- Se uno scontrino viene eliminato, tutti i prodotti collegati vengono rimossi automaticamente (`cascade delete`).

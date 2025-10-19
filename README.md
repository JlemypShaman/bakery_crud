# 🥖 Bakery CRUD (Flask + SQLite)

## Opis
Prosta aplikacja webowa CRUD dla piekarni.

## Uruchomienie
```bash
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
python app.py
```
Otwórz przeglądarkę i przejdź do http://127.0.0.1:5000/
"# bakery_crud" 
"# bakery_crud" 



## Nowe pola (etap B)
Dodano dwa nowe atrybuty w modelu `Product`:
- **ingredients** – lista składników produktu (tekst).
- **is_gluten_free** – informacja, czy produkt jest bezglutenowy (boolean).

Nowe pola obsługiwane są we wszystkich endpointach REST i widoczne w UI.

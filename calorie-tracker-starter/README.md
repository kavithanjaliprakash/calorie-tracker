# AI Calorie Tracker

Photograph or name any food, packaged or home-cooked, and log calories, protein, fat and sugar for the amount you actually ate.

Status: Phase 0 (setup). The app currently shows a setup check page.

## Run locally

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate    Mac/Linux: source .venv/bin/activate
pip install -r requirements.txt
cp .streamlit/secrets.toml.example .streamlit/secrets.toml   # then fill in values
streamlit run app.py
```

## Structure

- `app.py`: home / today screen
- `pages/`: add food, history, goals
- `services/`: gemini.py, off_api.py, db.py
- `data/`: units.csv, INDB extract

# ...existing code...
"""Ein kleines Beispiel-Modul mit read_data, Vorverarbeitung und einfachem 'Modell'."""
from typing import Dict
from pathlib import Path
import json
import pandas as pd


def read_data(path: str) -> pd.DataFrame:
    """Lädt eine CSV- oder JSON-Datei in ein pandas.DataFrame."""
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Datei nicht gefunden: {path}")
    if p.suffix.lower() == ".csv":
        return pd.read_csv(p)
    if p.suffix.lower() == ".json":
        return pd.read_json(p)
    raise ValueError(f"Ununterstütztes Format: {p.suffix}")


def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    """Einfache Vorverarbeitung: fehlende Werte entfernen."""
    return df.dropna().reset_index(drop=True)


def train_dummy_model(df: pd.DataFrame) -> Dict:
    """Platzhalter-Training: berechnet Mittelwerte numerischer Spalten."""
    numeric = df.select_dtypes(include="number")
    return {"means": numeric.mean().to_dict()}


def save_model(model: Dict, path: str) -> None:
    Path(path).write_text(json.dumps(model))


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python 03_model.py <datafile>")
        sys.exit(1)
    df = read_data(sys.argv[1])
    df = preprocess(df)
    model = train_dummy_model(df)
    save_model(model, "model.json")
# ...existing code...
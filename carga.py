from pathlib import Path

import pandas as pd

RAW = Path(__file__).parent / "Data" / "raw"


def cargar_datos():
    clientes = pd.read_csv(RAW / "cliente.csv")
    ventas = pd.read_csv(RAW / "ventas.csv")
    return clientes, ventas

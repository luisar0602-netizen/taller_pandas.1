from pathlib import Path

import pandas as pd

PROCESSED = Path(__file__).parent / "Data" / "processed"


def validar_premerge(clientes, ventas):
    """Revisa que el merge se pueda hacer. Devuelve True si todo está bien, False si no.

    Revisar:
    - Que exista la columna "id_cliente" en los dos dataframes.
    - Que "id_cliente" no esté repetido en clientes.
    - Que "id_cliente" tenga el mismo tipo en los dos dataframes.
    - Cuántas ventas no tienen cliente asociado (esto solo se informa, no falla).
    """
    columnas_requeridas = {"id_cliente"}
    if not columnas_requeridas.issubset(clientes.columns) or not columnas_requeridas.issubset(ventas.columns):
        print("[merge] Error: faltan columnas requeridas.")
        return False

    if clientes["id_cliente"].duplicated().any():
        print("[merge] Error: 'id_cliente' está duplicado en clientes.")
        return False

    if clientes["id_cliente"].dtype != ventas["id_cliente"].dtype:
        print("[merge] Error: 'id_cliente' tiene tipos distintos en clientes y ventas.")
        return False

    ventas_sin_cliente = ventas.loc[~ventas["id_cliente"].isin(clientes["id_cliente"]), "id_cliente"]
    print(f"[merge] Ventas sin cliente asociado: {len(ventas_sin_cliente)}")
    return True


def unir(clientes, ventas):
    """Une ventas con clientes usando "id_cliente" y guarda el resultado en Data/processed/merge.csv.

    Pistas:
    - Usar pd.merge(...) o ventas.merge(...).
    - Usar how="left" para no perder ventas.
    - Usar validate="m:1" para confirmar que cada venta tiene un solo cliente.
    - Guardar con df.to_csv(...) en PROCESSED / "merge.csv".
    """
    if not validar_premerge(clientes, ventas):
        return None

    PROCESSED.mkdir(parents=True, exist_ok=True)
    df = ventas.merge(clientes, on="id_cliente", how="left", validate="m:1")
    df.to_csv(PROCESSED / "merge.csv", index=False)
    print(f"[merge] Archivo guardado en: {PROCESSED / 'merge.csv'}")
    return df

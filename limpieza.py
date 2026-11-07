import pandas as pd


def _quitar_espacios(df):
    df = df.copy()
    for col in df.select_dtypes(include=["object", "string"]).columns:
        df[col] = df[col].str.strip()
    return df


def limpiar_clientes(clientes):
    print("\n[clientes] Nulos por columna:")
    print(clientes.isnull().sum())
    print(f"[clientes] Filas duplicadas: {clientes.duplicated().sum()}")

    clientes = _quitar_espacios(clientes)
    clientes["ciudad"] = clientes["ciudad"].str.title()
    clientes = clientes.drop_duplicates().reset_index(drop=True)

    print(f"[clientes] Filas tras limpieza: {len(clientes)}")
    return clientes


def limpiar_ventas(ventas):
    print("\n[ventas] Nulos por columna:")
    print(ventas.isnull().sum())
    print(f"[ventas] Filas duplicadas: {ventas.duplicated().sum()}")

    ventas = _quitar_espacios(ventas)
    ventas["producto"] = ventas["producto"].fillna("Sin especificar")
    ventas["fecha_venta"] = pd.to_datetime(ventas["fecha_venta"], format="%Y-%m-%d")
    ventas = ventas.drop_duplicates().reset_index(drop=True)

    print(f"[ventas] Filas tras limpieza: {len(ventas)}")
    return ventas


def limpiar_datos(clientes, ventas):
    return limpiar_clientes(clientes), limpiar_ventas(ventas)

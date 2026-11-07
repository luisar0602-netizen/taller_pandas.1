import pandas as pd

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 20)


def analizar(df):
    print("\nInfo general:")
    df.info()
    print("\nEstadísticas numéricas:")
    print(df.describe())

    ingresos_por_categoria(df)
    canal_que_mas_vende(df)
    clientes_vip_vs_regular(df)
    metodo_pago_mas_usado(df)
    top5_clientes(df)


def ingresos_por_categoria(df):
    """Pregunta 1: ¿Qué categoría genera más ingresos?

    Pista: df.groupby("categoria")["total"].sum().sort_values(ascending=False)
    """
    ingresos = df.groupby("categoria")["total"].sum().sort_values(ascending=False)
    print("\nIngresos por categoría:")
    print(ingresos)
    print(f"Categoría con más ingresos: {ingresos.index[0]} ({ingresos.iloc[0]:,.0f})")


def canal_que_mas_vende(df):
    """Pregunta 2: ¿Qué canal vende más?

    Pista: agrupar por "canal" y usar .agg(ventas=("id_venta", "count"), ingresos=("total", "sum")).
    """
    canales = df.groupby("canal").agg(ventas=("id_venta", "count"), ingresos=("total", "sum")).sort_values(["ventas", "ingresos"], ascending=False)
    print("\nVentas e ingresos por canal:")
    print(canales)
    print(f"Canal que más vende: {canales.index[0]} ({canales.iloc[0]['ventas']} ventas)")


def clientes_vip_vs_regular(df):
    """Pregunta 3: ¿Los clientes VIP compran más que los Regulares?

    Pista: como hay más clientes Regular que VIP, compare promedios por cliente, no totales.
    Calcular: número de clientes (nunique), compras y gasto total por segmento,
    y luego dividir compras y gasto entre el número de clientes.
    """
    resumen = (
        df.groupby("segmento_cliente")
        .agg(clientes=("id_cliente", "nunique"), compras=("id_venta", "count"), gasto_total=("total", "sum"))
        .assign(
            compras_promedio=lambda x: x["compras"] / x["clientes"],
            gasto_promedio=lambda x: x["gasto_total"] / x["clientes"],
        )
        .sort_index()
    )
    print("\nCompras y gasto promedio por cliente según segmento:")
    print(resumen)

    vip = resumen.loc["VIP"]
    regular = resumen.loc["Regular"]
    if vip["compras_promedio"] > regular["compras_promedio"]:
        mensaje = "Los clientes VIP compran más que los Regulares en promedio."
    else:
        mensaje = "Los clientes VIP no compran más que los Regulares en promedio."
    print(mensaje)


def metodo_pago_mas_usado(df):
    """Pregunta 4: ¿Qué método de pago es más usado?

    Pista: df["metodo_pago"].value_counts()
    """
    pagos = df["metodo_pago"].value_counts()
    print("\nMétodo de pago más usado:")
    print(pagos)
    print(f"Método de pago más usado: {pagos.index[0]} ({pagos.iloc[0]} ventas)")


def top5_clientes(df):
    """Pregunta 5: ¿Top 5 clientes con más compras?

    Pista: agrupar por ["id_cliente", "nombre_cliente"], contar compras y sumar total,
    ordenar por compras (y por gasto como desempate) y tomar las primeras 5 con .head(5).
    """
    top = (
        df.groupby(["id_cliente", "nombre_cliente"])
        .agg(compras=("id_venta", "count"), gasto_total=("total", "sum"))
        .sort_values(["compras", "gasto_total"], ascending=[False, False])
        .head(5)
    )
    print("\nTop 5 clientes con más compras:")
    print(top)

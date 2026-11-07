from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

SALIDA = Path(__file__).parent / "Data" / "processed" / "graficos"


def _guardar_grafico(fig, nombre_archivo):
    SALIDA.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    fig.savefig(SALIDA / nombre_archivo, bbox_inches="tight")
    plt.close(fig)


def grafico_ventas_por_categoria(df):
    """Gráfico de barras: total vendido por categoría.

    Pistas:
    - Calcular datos = df.groupby("categoria")["total"].sum()
    - datos.plot(kind="bar") dibuja las barras.
    - plt.title, plt.xlabel y plt.ylabel ponen los textos.
    - plt.savefig(SALIDA / "ventas_por_categoria.png", bbox_inches="tight") guarda la imagen.
    - plt.show() la muestra en pantalla y plt.close() la cierra.
    """
    datos = df.groupby("categoria")["total"].sum().sort_values(ascending=False)
    fig, ax = plt.subplots()
    datos.plot(kind="bar", ax=ax, color="steelblue")
    ax.set_title("Total vendido por categoría")
    ax.set_xlabel("Categoría")
    ax.set_ylabel("Ingresos")
    _guardar_grafico(fig, "ventas_por_categoria.png")
    print(f"[graficos] Guardado: {SALIDA / 'ventas_por_categoria.png'}")


def grafico_ventas_por_canal(df):
    """Gráfico de barras: total vendido por canal (Online contra Tienda).

    Usa los mismos pasos que la función anterior, cambiando la columna "categoria" por "canal".
    """
    datos = df.groupby("canal")["total"].sum().sort_values(ascending=False)
    fig, ax = plt.subplots()
    datos.plot(kind="bar", ax=ax, color="darkorange")
    ax.set_title("Total vendido por canal")
    ax.set_xlabel("Canal")
    ax.set_ylabel("Ingresos")
    _guardar_grafico(fig, "ventas_por_canal.png")
    print(f"[graficos] Guardado: {SALIDA / 'ventas_por_canal.png'}")


def graficar(df):
    grafico_ventas_por_categoria(df)
    grafico_ventas_por_canal(df)

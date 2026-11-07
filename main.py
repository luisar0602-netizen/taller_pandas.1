import analisis
import carga
import graficos
import limpieza
import merge

MENU = """
===== MENÚ =====
1. Cargar datos
2. Limpiar datos
3. Validar y unir (merge)
4. Análisis del merge
5. Gráficos (introducción)
6. Salir
"""


def main():
    clientes = ventas = df_merge = None

    while True:
        print(MENU)
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            clientes, ventas = carga.cargar_datos()
            df_merge = None
            print(f"Clientes: {clientes.shape} | Ventas: {ventas.shape}")
        elif opcion == "2":
            if clientes is None:
                print("Primero cargue los datos (opción 1).")
                continue
            clientes, ventas = limpieza.limpiar_datos(clientes, ventas)
            df_merge = None
        elif opcion == "3":
            if clientes is None:
                print("Primero cargue los datos (opción 1).")
                continue
            df_merge = merge.unir(clientes, ventas)
        elif opcion == "4":
            if df_merge is None:
                print("Primero realice el merge (opción 3).")
                continue
            analisis.analizar(df_merge)
        elif opcion == "5":
            if df_merge is None:
                print("Primero realice el merge (opción 3).")
                continue
            graficos.graficar(df_merge)
        elif opcion == "6":
            print("Hasta luego.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()

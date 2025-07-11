def comprar_entrada(stock, compradores):
    try:
        print("\n-- Comprar Entrada --")
        nombre = input("Nombre del comprador: ").strip()
        if nombre in compradores:
            print("Error: el nombre ya existe.")
            return stock

        print("Seleccione función:")
        print("1. Movimiento Origen con los Tripulantes Shamanes (50 entradas)")
        print("2. Movimiento Origen con Sonrisa MC (60 entradas)")
        opcion = input("Función (1 ó 2): ").strip()
        if opcion not in ('1', '2'):
            print("Error: opción de función inválida.")
            return stock

        if opcion == '1':
            if stock['f1'] <= 0:
                print("Error: no hay stock disponible para la función 1.")
                return stock
            stock['f1'] -= 1
        else:
            if stock['f2'] <= 0:
                print("Error: no hay stock disponible para la función 2.")
                return stock
            stock['f2'] -= 1
        compradores[nombre] = opcion
        print(f"Entrada registrada en función {opcion}! Stock restantes: \n"
            f"  Función 1: {stock['f1']} \n  Función 2: {stock['f2']}")
        return stock
    except Exception as error:
        print("Error con el nombre del comprador ", error)


def cambiar_show(stock, compradores):
    try:
        print("\n-- Cambiar Show --")
        nombre = input("Nombre del comprador: ").strip()
        if nombre not in compradores:
            print("Error: comprador no encontrado.")
            return stock

        actual = compradores[nombre]
        nueva = '2' if actual == '1' else '1'
        if stock[f'f{nueva}'] <= 0:
            print(f"Error: no hay stock disponible para la función {nueva}.")
            return stock

        confirm = input(f"Cambiar de función {actual} a {nueva}? (S/N): ").strip().upper()
        if confirm != 'S':
            print("Cambio cancelado.")
            return stock

        # Ajustar stock
        stock[f'f{actual}'] += 1
        stock[f'f{nueva}'] -= 1
        compradores[nombre] = nueva
        print(f"Cambio exitoso. Ahora está en función {nueva}.")
        return stock
    except Exception as error:
        print("Error con el nombre del comprador ", error)


def mostrar_totales(stock, compradores):
    print("\n-- Totales de Entradas --")
    vendidos_f1 = 50 - stock['f1']
    vendidos_f2 = 60 - stock['f2']
    print(f"Función 1: Disponibles {stock['f1']}, Vendidas {vendidos_f1}")
    print(f"Función 2: Disponibles {stock['f2']}, Vendidas {vendidos_f2}")



stock = {'f1': 50, 'f2': 60}
compradores = {}

while True:
    try:
        print("\nMENU PRINCIPAL CONCIERTO MOVIMIENTO ORIGEN")
        print("1.- Comprar entrada.")
        print("2.- Cambiar show.")
        print("3.- Mostrar stock.")
        print("4.- Salir.")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == '1':
            stock = comprar_entrada(stock, compradores)
        elif opcion == '2':
            stock = cambiar_show(stock, compradores)
        elif opcion == '3':
            mostrar_totales(stock, compradores)
        elif opcion == '4':
            print("\nPrograma terminado...")
            break
        else:
            print("Debe ingresar una opción válida!!")
    except Exception as error:
            print("Error con el nombre del comprador ", error)

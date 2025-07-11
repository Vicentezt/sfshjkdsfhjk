# Diccionario de stock: "Marca-Modelo" : precio
stock = {
    "HP-ProBook": 600000,
    "HP-Pavilion": 450000,
    "DELL-Inspiron": 750000,
    "DELL-XPS": 1200000,
    "LENOVO-IdeaPad": 550000,
    "LENOVO-ThinkPad": 980000
}

# Función Opción 1
def stock_marca(marca):
    marca = marca.upper()
    encontrados = []
    for modelo_completo, precio in stock.items():
        partes = modelo_completo.upper().split("-")
        if len(partes) == 2:
            marca_actual, modelo_actual = partes
            if marca_actual == marca:
                encontrados.append((modelo_completo, precio))
    if encontrados:
        print(f"Modelos encontrados para la marca {marca}:")
        for modelo, precio in encontrados:
            print(f"- {modelo}: ${precio}")
    else:
        print("No existen modelos de esa marca.")

# Función Opción 2
def busqueda_precio(p_min, p_max):
    resultados = []
    for modelo, precio in stock.items():
        if p_min <= precio <= p_max:
            resultados.append(modelo)
    if resultados:
        print("Modelos encontrados en el rango de precios:")
        for modelo in resultados:
            print(modelo)
    else:
        print("No hay notebooks en ese rango de precios.")

# Función Opción 3
def actualizar_precio(modelo, p):
    modelo_upper = modelo.upper()
    existe = False
    for key in stock.keys():
        if key.upper() == modelo_upper:
            stock[key] = p
            existe = True
            break
    return existe

# --------------------------------------------
# MENÚ PRINCIPAL FUERA DE FUNCIONES
# --------------------------------------------

while True:
    print("\n*** MENU PRINCIPAL ***")
    print("1. Stock marca.")
    print("2. Búsqueda por precio.")
    print("3. Actualizar precio.")
    print("4. Salir.")
    
    opcion = input("Seleccione una opción (1-4): ")
    
    if opcion == "1":
        marca = input("Ingrese la marca: ")
        stock_marca(marca)

    elif opcion == "2":
        try:
            p_min = int(input("Ingrese precio mínimo: "))
            p_max = int(input("Ingrese precio máximo: "))
            
            if p_min >= p_max or p_min < 0 or p_max < 0:
                print("Debe ingresar valores correctos!!")
            else:
                busqueda_precio(p_min, p_max)
        except ValueError:
            print("Debe ingresar valores numéricos!!")

    elif opcion == "3":
        while True:
            modelo = input("Ingrese el modelo (Marca-Modelo): ")
            try:
                nuevo_precio = int(input("Ingrese el nuevo precio: "))
                resultado = actualizar_precio(modelo, nuevo_precio)
                if resultado:
                    print("Precio actualizado!!")
                else:
                    print("El modelo no existe!!")
            except ValueError:
                print("Debe ingresar un valor numérico para el precio.")
            
            continuar = input("¿Desea actualizar otro precio? (si/no): ").strip().lower()
            if continuar != "si":
                break

    elif opcion == "4":
        print("Programa finalizado.")
        break

    else:
        print("Opción inválida. Intente nuevamente.")

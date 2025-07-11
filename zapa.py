#Funciones
MAX_RESERVAS = 20
def reservar_zapatillas(reservas):
    """
    Registra una nueva reserva si no se supera el stock máximo,
    el nombre no está repetido y se ingresa la clave correcta.
    reservas: dict nombre -> [pares, vip]
    """
    try:
        print("\n-- Reservar Zapatillas --")
        if len(reservas) >= MAX_RESERVAS:
            print("Lo sentimos, no quedan reservas disponibles.")
            return

        nombre = input("Nombre del comprador: ").strip()
        if nombre in reservas:
            print("Error: el nombre ya existe en las reservas.")
            return

        clave = input("Digite la palabra secreta para confirmar la reserva: ").strip()
        if clave != "EstoyEnListaDeReserva":
            print("Error: palabra clave incorrecta. Reserva no realizada.")
            return

        # Reserva registrada con 1 par, VIP por defecto False
        reservas[nombre] = [1, False]
        print(f"Reserva realizada exitosamente para {nombre}.")
    except Exception as error:
        print("Error con la reserva ", error)


def buscar_zapatillas(reservas):
    """
    Busca una reserva por nombre y ofrece opción VIP para 2 pares.
    """
    try:
        print("\n-- Buscar Zapatillas Reservadas --")
        nombre = input("Nombre del comprador a buscar: ").strip()
        if nombre not in reservas:
            print("No se encontró ninguna reserva con ese nombre.")
            return

        pares, vip = reservas[nombre]
        estado = 'VIP' if vip else 'estándar'
        print(f"Reserva encontrada: {nombre} - {pares} par(es) ({estado}).")

        if not vip:
            opcion = input("¿Desea pagar adicional para VIP y reservar 2 pares? (s/n): ").strip().lower()
            if opcion == 's':
                reservas[nombre] = [2, True]
                print(f"Reserva actualizada a VIP. Ahora {nombre} tiene 2 pares reservados.")
            else:
                print("Manteniendo reserva actual.")
    except Exception as error:
        print("Error con buscar la reserva ", error)


def cancelar_reserva(reservas):
    """
    Cancela la reserva si existe.
    """
    try:
        print("\n-- Cancelar Reserva --")
        nombre = input("Nombre del comprador cuya reserva desea cancelar: ").strip()
        if nombre in reservas:
            del reservas[nombre]
            print(f"La reserva de {nombre} ha sido cancelada.")
        else:
            print("No se encontró ninguna reserva con ese nombre.")
    except Exception as error:
        print("Error con cancelar la reserva ", error)



reservas = {}  # dict: nombre -> [pares, vip]
while True:
    try:
        print("\nTOTEM AUTOATENCIÓN RESERVA STRIKE")
        print("1.- Reservar zapatillas")
        print("2.- Buscar zapatillas reservadas")
        print("3.- Cancelar reserva de zapatillas")
        print("4.- Salir")
        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == '1':
            reservar_zapatillas(reservas)
        elif opcion == '2':
            buscar_zapatillas(reservas)
        elif opcion == '3':
            cancelar_reserva(reservas)
        elif opcion == '4':
            print("\nPrograma terminado...")
            break
        else:
                print("Debe ingresar una opción válida!!")
    except Exception as error:
            print("Error con el menú principal ", error)
        




        fgaklñnñnnnñnñnñnñnñnñnñnñnñnñdñññññññññgaiouqghijagjioiohjarghjiño
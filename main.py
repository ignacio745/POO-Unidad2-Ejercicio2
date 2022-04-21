from ClaseManejadorVIajerosFrecuentes import ManejadorViajerosFrecuentes
from Menu import Menu


if __name__=="__main__":
    unMenu = Menu(["Seleccione la opcion deseada", "Cargar csv", "Mostrar datos", "Consultar cantidad de millas dado un numero de viajero", "Acumular Millas dado un numero de viajero", "Canjear millas dado un numero de viajero", "Salir"])
    unManejadorViajeros = ManejadorViajerosFrecuentes()

    opcion = 0

    while opcion != 6:
        opcion = unMenu.input()

        if opcion == 1:
            unManejadorViajeros.leerCSV("viajeros.csv")
        
        elif opcion == 2:
            print("Datos de los viajeros del csv")
            unManejadorViajeros.listarViajeros()
        
        elif opcion == 3:
            unManejadorViajeros.consultarCantidadMillas()

        elif opcion == 4:
            unManejadorViajeros.acumularMillas()
        
        elif opcion == 5:
            unManejadorViajeros.canjearMillas()
        
        elif opcion == 6:
            unManejadorViajeros.guardarCSV("Viajeros actualizado.csv")

        if opcion != 6:
            input("Presione Enter para continuar")
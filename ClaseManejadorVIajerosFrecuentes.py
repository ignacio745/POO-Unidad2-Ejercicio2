from ClaseViajeroFrecuente import ViajeroFrecuente
from tabulate import tabulate
import csv

class ManejadorViajerosFrecuentes:
    __viajeros = []
    def __init__(self):
        self.__viajeros = []
    
    def agregarViajeroFrecuente(self, unViajeroFrecuente:ViajeroFrecuente):
        band = False
        if isinstance(unViajeroFrecuente, ViajeroFrecuente):
            self.__viajeros.append(unViajeroFrecuente)
            band = True
        return band


    def leerCSV(self, nombreArchivo):
        archivo = open(nombreArchivo)
        reader = csv.reader(archivo)
        self.__viajeros = []
        agregados = 0
        total = 0
        for fila in reader:
            if fila[0].isnumeric() and fila[1].isnumeric() and fila[4].isnumeric():
                unViajeroFrecuente = ViajeroFrecuente(int(fila[0]), fila[1], fila[2], fila[3])
                unViajeroFrecuente.acumularMillas(int(fila[4]))
                self.agregarViajeroFrecuente(unViajeroFrecuente)
                agregados +=1
            else:
                print("[ERROR] No se pudo agregar un viajero")
            total +=1
        print("Se cargaron {0} de {1} viajeros".format(agregados, total))

    
    def listarViajeros(self):
        print("{0:<10}{1:<9}{2:<15}{3:<15}{4}".format("Numero", "DNI", "Nombre", "Apellido", "Millas"))
        for unViajero in self.__viajeros:
            if isinstance(unViajero, ViajeroFrecuente):
                print("{0:<10}{1:<9}{2:<15}{3:<15}{4}".format(unViajero.getNumero(), unViajero.getDNI(), unViajero.getNombre(), unViajero.getApellido(), unViajero.getMillas()))


    def buscarViajeroPorNumero(self, numero:int):
        i = 0
        unViajero = self.__viajeros[0]
        while (unViajero.getNumero() != numero and i < len(self.__viajeros)-1):
            i += 1
            unViajero = self.__viajeros[i]
        if unViajero.getNumero() != numero:
            unViajero = None
        return unViajero
    

    def consultarCantidadMillas(self):
        numeroViajero = int(input("Ingrese el numero de viajero: "))

        unViajero = self.buscarViajeroPorNumero(numeroViajero)

        if isinstance(unViajero, ViajeroFrecuente):
            millas = unViajero.getMillas()
            print ("La cantidad de millas del viajero {0} es {1}".format(numeroViajero, millas))
        else:
            print("[ERROR] No se encuentra el viajero")
    

    def acumularMillas(self):
        numeroViajero = int(input("Ingrese el numero de viajero: "))

        unViajero = self.buscarViajeroPorNumero(numeroViajero)
        
        if isinstance(unViajero, ViajeroFrecuente):
            millas = int(input("Ingrese el numero de millas a acumular: "))
            unViajero.acumularMillas(millas)
            print ("Millas acumuladas")
        else:
            print ("[ERROR] No se encuentra el viajero")
        

    def canjearMillas(self):

        numeroViajero = int(input("Ingrese el numero de viajero: "))
        unViajero = self.buscarViajeroPorNumero(numeroViajero)
        
        if isinstance(unViajero, ViajeroFrecuente):
            millas = int(input("Ingrese el numero de millas a canjear: "))
            unViajero.canjearMillas(millas)
        else:
            print("[ERROR] No se encuentra el viajero")
    
    
    def guardarCSV(self, nombreArchivo):
        archivo = open(nombreArchivo, "w")
        writer = csv.writer(archivo)
        for unViajero in self.__viajeros:
            if isinstance(unViajero, ViajeroFrecuente):
                datos = [unViajero.getNumero(), unViajero.getDNI(), unViajero.getNombre(), unViajero.getApellido(), unViajero.getMillas()]
                writer.writerow(datos)
class ViajeroFrecuente:
    __num__viajero = 0
    __dni = ""
    __nombre = ""
    __apellido = ""
    __millas_acum = 0
    def __init__(self, num_viajero:int, dni:str, nombre:str, apellido:str):
        self.__num__viajero = num_viajero
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millas_acum = 0
    
    def cantidadTotalMillas(self):
        return self.__millas_acum
    
    def acumularMillas(self, millas:int): # Esta funcion deberia recibir las millas (como lo hace ahora)
                                          # O deberia pedirlas por input()?
        band = False
        if isinstance(millas, int):
            self.__millas_acum += millas
            band = True
        else:
            print("[ERROR] Las millas deben ser del tipo 'int'")
        return band
    
    # codigo alternativo
#    def acumularMillas(self):
#        millas = int(input("Ingrese el numero de millas a acumular: "))
#        self.__millas_acum += millas
#        print ("Millas acumuladas")
    
    def canjearMillas(self, millas:int):
        if isinstance(millas, int):
            if millas <= self.__millas_acum:
                self.__millas_acum -= millas
                print("Millas canjeadas")
            else:
                print("[ERROR] No puede canjear más millas de las que tiene")
        else:
            print("[ERROR] Las millas deben ser del tipo 'int'")

    
    def getNumero(self):
        return self.__num__viajero
    
    def getMillas(self):
        return self.__millas_acum
    
    def getDNI(self):
        return self.__dni
    
    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido
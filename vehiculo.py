class Vehiculo:
    '''
    classe que representa un objetode la clase vehiculo
    '''
    def __init__(self, marca:str, modelo:str, color:str=None, anio:int=2025):
        '''
        Constructor de la clase Vehiculo
        :param marca: la marca del vehiculo
        :param modelo: el modelo del vehiculo
        :param color: el color del  vehiculo
        :param anio: el anio del vehiculo
        '''
        self._marca = marca
        self._modelo = modelo
        self._color = color
        self._anio = anio

    def __str__(self):
         #return f'Vehiculo:[marca={self._marca}],modelo={self._modelo}'
         return f'Vehiculo:{self.__dict__.__str__()}'  #para incluir a todos los atributos se hace un diccionario


if __name__ == '__main__':
    v1 = Vehiculo('BMW', 'Arizona', 'color')
    print(v1._marca)
    print(v1._modelo)
    print(v1._color)
    #print(v1.__str__())
    print(v1)

    v2= Vehiculo('FORD', 'F150', 'AZUL', '2024')
    print(v2._marca)
    print(v2._modelo)
    print(v2._color)
    print(v2._anio)

    v3 = Vehiculo('FORD', 'F150', 'AZUL', 'Dos mil veintitres')
    print(v3._marca)
    print(v3._modelo)
    print(v3._color)
    print(v3._anio)

    v4 = Vehiculo('Chevrolet', 'sail')
    print(v4._marca)
    print(v4._modelo)

    v5 = Vehiculo(modelo='Fiesta', marca='Ford', color='negro')
    print(v5)






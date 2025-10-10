
import random
import datetime 
from typing import Callable, Any
class Vehiculo:
    def __init__(self,num_id:int,marca:str,modelo:str,color:str,anio:int,tipo_alimentacion:str,modalidad:str,tipo_freno:str,precio:float):
        self.num_id = num_id
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.anio = anio
        self.tipo_alimentacion = tipo_alimentacion # combustion interna o electrico
        self.modalidad = modalidad # versiones deportivas, todo terreno, urbano, etc
        self.tipo_frenos = tipo_freno # a tambor o a disco (en caso de autos abs o no)
        self.precio = precio

    def __str__(self) -> str:
        return f'{self.num_id},{self.marca},{self.modelo},{self.color},{self.anio},{self.tipo_alimentacion},{self.modalidad},{self.tipo_frenos}'

class Bicicleta(Vehiculo):
    def __init__(self, num_id, marca, modelo, color, anio, tipo_alimentacion, modalidad, tipo_freno,precio,rodado:str,talle:str,transmision:str):
        super().__init__(num_id, marca, modelo, color, anio, tipo_alimentacion, modalidad, tipo_freno,precio)
        tipo_alimentacion = None
        self.rodado = rodado
        self.talle = talle
        self.transmision = transmision
    
    def __str__(self) -> str:
        return f'{self.num_id},{self.marca},{self.modelo},{self.color},{self.anio},{self.tipo_alimentacion},{self.modalidad},{self.tipo_frenos},{self.rodado},{self.talle},{self.transmision}'

class Auto(Vehiculo):
    def __init__(self, num_id, marca, modelo, color, anio, tipo_alimentacion, modalidad,precio,tipo_freno,motor:int,cant_puertas:int,capacidad_tanque:float):
        super().__init__(num_id, marca, modelo, color, anio, tipo_alimentacion, modalidad, tipo_freno,precio)
        self.motor = motor # podria ser tamaño o potencia (a debatir)
        self.cant_puertas = cant_puertas
        self.capacidad_tanque = capacidad_tanque # en litros

class Motocicleta(Vehiculo):
    def __init__(self, num_id, marca, modelo, color, anio, tipo_alimentacion, modalidad,precio,tipo_freno,tamanio_motor:int,tipo_motor:str,tipo_ciclo:int):
        super().__init__(num_id, marca, modelo, color, anio, tipo_alimentacion, modalidad, tipo_freno,precio)
        self.tamanio_motor = tamanio_motor # puede agregarse como un atributo de clase madre, comparte con Auto
        self.tipo_motor = tipo_motor # monocilindrico, bicilindrico, etc
        self.tipo_ciclo = tipo_ciclo # 2 tiempos o 4 tiempos

class Concesionaria:

    def __init__(self,inventario = None):
        if inventario is None:
            self.inventario: list[Vehiculo] = []
    
    def agregar_vehiculo(self,vehiculo:Vehiculo):
        self.inventario.append(vehiculo)
    
    def agregar_bici(self):
        bicicleta:Bicicleta

        def validacion(mensaje_entrada:str,mensaje_salida:str,opciones:list[str]):
            variable_control = False
            while not variable_control:
                atributo = input(mensaje_entrada).lower()
                if atributo in opciones:
                    variable_control = True
                else:
                    print(f'{mensaje_salida}')
            return atributo

        opciones_modalidad = ['montaña','gravel','ruta','descenso']
        opciones_talle = ['xs','s','m','l','xl']
        opciones_frenos = ['mecanicos','hidraulicos']
        opciones_rodado = ['26','27.5','28','29']


                    
        marca = input(str('Ingrese la marca : '))
        modelo = input(str('Ingrese el modelo : '))
        transmision = input(str('Ingrese la transmision: '))
        color = input(str('Ingrese el color: '))

        validacion_anio = False
        while not(validacion_anio):
            try:
                anio = int(input('Ingrese el año (2015-2025): '))
                if 2015 <= anio < 2026:
                    validacion_anio = True
                else:
                    print(f'Solo modelos de 2015 a 2025')
            except ValueError:
                print(f'Ingresar un numero valido como año')


        modalidad = validacion(f'Ingrese la modalidad {opciones_modalidad}:',f'Solo modalidades declaradas {opciones_modalidad}',opciones_modalidad)
        talle = validacion(f'Ingrese el talle del cuadro {opciones_talle}: ',f'Solo ingresar talles validos {opciones_talle}',opciones_talle)
        tipo_freno = validacion(f'Ingrese el tipo de frenos de la bicicleta {opciones_frenos}',f'Solo ingresar tipo valid {opciones_frenos}',opciones_frenos)
        rodado = validacion(f'Ingrese el rodado de la bicicleta {opciones_rodado}',f'Solo ingresar rodados validos {opciones_rodado}',opciones_rodado)
        
        validacion_precio = False
        while not validacion_precio:
            try:
                precio = float(input('Ingrese el precio: ')) #
                if precio > 0:
                    validacion_precio = True
                else:
                    print(f'El precio debe un numero positivo')
            except ValueError:
                print(f'Se debe ingresar un numero')

        bicicleta = Bicicleta(
            num_id = random.sample(range(1,100), 1)[0],    #metodo sample genera valor unico
            marca = marca.capitalize(),
            modelo = modelo.capitalize(),
            color = color,
            anio = anio,
            tipo_alimentacion = None,
            modalidad = modalidad.capitalize(),
            tipo_freno = tipo_freno.capitalize(),
            precio = precio,
            rodado = rodado,
            talle = talle.capitalize(),
            transmision = transmision
        )
        self.inventario.append(bicicleta)
        with open('persistencia.txt','a',encoding='utf-8') as file:
            file.write(f'BICICLETA|{bicicleta.num_id}|{bicicleta.marca}|{bicicleta.modelo}|{bicicleta.color}|{bicicleta.anio}|{bicicleta.tipo_alimentacion}|{bicicleta.modalidad}|{bicicleta.tipo_frenos}|{bicicleta.precio}|{bicicleta.rodado}|{bicicleta.talle}|{bicicleta.transmision}\n')

    def eliminar_vehiculo(self):
        pass

    def modificar_precio(self):
        pass

    def venta_vehiculo(self):
        pass


def cargar_catalogo(catalogo):
    vehiculos = []
    with open('vehiculos_registro.txt',encoding='utf-8') as file:
        archivo = file.readlines()
        for linea in archivo:
            linea = linea.strip()
            datos = linea.split('|')
            tipo = datos[0]
            if tipo == 'BICICLETA':
                bici = Bicicleta(
                    num_id = datos[1],
                    marca = datos[2],
                    modelo = datos[3],
                    color =  datos[4],
                    anio = datos[5],
                    tipo_alimentacion = None,
                    modalidad = datos[7],
                    tipo_freno = datos[8],
                    precio = datos[9],
                    rodado = datos[10],
                    talle = datos[11],
                    transmision = datos[12])
                vehiculos.append(bici)
 
if __name__ == '__main__':
    vehiculos = cargar_catalogo('vehiculos_registro.txt')
    concesionaria = Concesionaria(vehiculos)
    concesionaria.agregar_bici()

    for v in concesionaria.inventario:
        print(v)

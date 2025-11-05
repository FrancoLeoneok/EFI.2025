

import random
from funcion import validacion,validacion_try

class Vehiculo:
    def __init__(self,num_id,marca:str,modelo:str,color:str,anio:int,tipo_alimentacion:str,modalidad:str,tipo_freno:str,precio:float):
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
    def __init__(self, num_id, marca, modelo, color, anio, tipo_alimentacion, modalidad,precio,tipo_freno,tamanio_motor, tipo_motor,tipo_ciclo):
        super().__init__(num_id, marca, modelo, color, anio, tipo_alimentacion, modalidad, tipo_freno,precio)
        self.tamanio_motor = tamanio_motor # puede agregarse como un atributo de clase madre, comparte con Auto
        self.tipo_motor = tipo_motor # monocilindrico, bicilindrico, etc
        self.tipo_ciclo = tipo_ciclo # 2 tiempos o 4 tiempos

class Concesionaria:

    def __init__(self,inventario):
        self.inventario: list[Vehiculo] = inventario
        
    
    def agregar_vehiculo(self,vehiculo:Vehiculo):
        self.inventario.append(vehiculo)
    
    def agregar_bici(self):
        bicicleta:Bicicleta
        opciones_modalidad = ['montaña','gravel','ruta','descenso']
        opciones_talle = ['xs','s','m','l','xl']
        opciones_frenos = ['mecanico','hidraulico']
        opciones_rodado = ['26','27.5','28','29']
                        
        marca = input(str('Ingrese la marca : '))
        modelo = input(str('Ingrese el modelo : '))
        transmision = input(str('Ingrese la transmision: '))
        color = input(str('Ingrese el color: '))
        anio = validacion_try('Ingrese el año (2015-2025): ','Solo años disponibles 2015 a 2025','Debe ingresar un numero entero',2015,2025)

        modalidad = validacion(f'Ingrese la modalidad {opciones_modalidad}:',f'Solo modalidades declaradas {opciones_modalidad}',opciones_modalidad)
        talle = validacion(f'Ingrese el talle del cuadro {opciones_talle}: ',f'Solo ingresar talles validos {opciones_talle}',opciones_talle)
        tipo_freno = validacion(f'Ingrese el tipo de frenos de la bicicleta {opciones_frenos}',f'Solo ingresar tipo valid {opciones_frenos}',opciones_frenos)
        rodado = validacion(f'Ingrese el rodado de la bicicleta {opciones_rodado}',f'Solo ingresar rodados validos {opciones_rodado}',opciones_rodado)
        
        precio = validacion_try('Ingrese el precio: ','El precio debe ser un entero positivo','Se debe ingresar un numero entero',0)
        
        bicicleta = Bicicleta(
            num_id= self.generador_id(),
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
        with open('inventario.txt','a',encoding='utf-8') as file:
            file.write(f'BICICLETA|{bicicleta.num_id}|{bicicleta.marca}|{bicicleta.modelo}|{bicicleta.color}|{bicicleta.anio}|{bicicleta.tipo_alimentacion}|{bicicleta.modalidad}|{bicicleta.tipo_frenos}|{bicicleta.precio}|{bicicleta.rodado}|{bicicleta.talle}|{bicicleta.transmision}\n')
   
    def agregar_auto(self):
        auto:Auto
        opciones_modalidad = ['hatchback','sedan','suv','muv',"coupe","convertible","camioneta"]
        opciones_frenos = ['tambor','disco', "abs"]
        opciones_alimentacion = ["combustion","electrica", "hibrido"]
        
        marca = input(str('Ingrese la marca : '))
        modelo = input(str('Ingrese el modelo : '))        
        color = input(str('Ingrese el color: '))
        anio = validacion_try('Ingrese el año (2000-2025): ','Solo años disponibles 2000 a 2025','Debe ingresar un numero entero',2000,2025)
        tipo_alimentacion = validacion(f"Ingrese el tipo de alimentacion {opciones_alimentacion}:", f"alimentacion {opciones_alimentacion}",opciones_alimentacion)
        modalidad = validacion (f"Ingrese la modalidad {opciones_modalidad}:",f"Solo modalidades declaradas {opciones_modalidad}",opciones_modalidad)
        tipo_freno = validacion(f"Ingrese el tipo de frenos del auto {opciones_frenos}",f"Solo ingresar tipo valid {opciones_frenos}",opciones_frenos)
        motor = input("ingrese el tamaño de motor: ")
        cant_puertas = int(input("ingrese la cantidad de puertas: "))
        capacidad_tanque = float(input("ingrese la capacidad del tanque de combustible: "))
                
        
        precio = validacion_try('Ingrese el precio: ','El precio debe ser un entero positivo','Se debe ingresar un numero entero',0)
        
        auto = Auto(
            num_id = self.generador_id(),
            marca = marca.capitalize(),
            modelo = modelo.capitalize(),
            color = color,
            anio = anio,
            tipo_alimentacion = tipo_alimentacion.capitalize(),
            modalidad = modalidad.capitalize(),
            tipo_freno = tipo_freno.capitalize(),
            precio = precio,
            motor = motor,
            cant_puertas = cant_puertas,
            capacidad_tanque = capacidad_tanque
           
        )
        self.inventario.append(auto)
        with open('inventario.txt','a',encoding='utf-8') as file:
            file.write(f'AUTO|{auto.num_id}|{auto.marca}|{auto.modelo}|{auto.color}|{auto.anio}|{auto.tipo_alimentacion}|{auto.modalidad}|{auto.tipo_frenos}|{auto.precio}|{auto.motor}|{auto.cant_puertas}|{auto.capacidad_tanque}\n')


    def agregar_moto(self):
        opciones_alimentacion = ["combustible", "electrica"]
        opciones_modalidad = ['deportiva','touring','offroad','urbana',"adventure"]
        opciones_frenos = ['tambor','disco',"abs"]
        opciones_tipo_motor = ['monocilindrico','bicilindrico','tricilindrico','cuatricilindrico']
        
        marca = input(str('Ingrese la marca : '))
        modelo = input(str('Ingrese el modelo : '))        
        color = input(str('Ingrese el color: '))
        anio = validacion_try('Ingrese el año (2012-2025): ','Solo años disponibles 2012 a 2025','Debe ingresar un numero entero',2012,2025)
        tipo_alimentacion = validacion(f"ingrese el tipo de alimentacion {opciones_alimentacion}:" ,f"Solo tipos de alimentacion señaladas {opciones_alimentacion}",opciones_alimentacion)
        modalidad = validacion(f'Ingrese la modalidad {opciones_modalidad}:',f'Solo modalidades declaradas {opciones_modalidad}',opciones_modalidad)        
        tipo_freno = validacion(f'Ingrese el tipo de frenos de la moto {opciones_frenos}',f'Solo ingresar tipo valid {opciones_frenos}',opciones_frenos)
        tamanio_motor = validacion_try("ingrese el tamaño del motor (en cc): ","El tamaño del motor debe ser un numero positivo","Se debe ingresar un numero entero",50)
        tipo_motor = validacion(f'Ingrese el tipo de motor {opciones_tipo_motor}',f'Solo ingresar tipos de motor validos {opciones_tipo_motor}',opciones_tipo_motor)
        tipo_ciclo = validacion_try("ingrese el tipo de ciclo (2 o 4 tiempos): ","El tipo de ciclo debe ser 2 o 4","Se debe ingresar un numero entero",2,4)
                
        
        precio = validacion_try('Ingrese el precio: ','El precio debe ser un entero positivo','Se debe ingresar un numero entero',0)
        
        moto = Motocicleta(
            num_id= self.generador_id(),
            marca = marca.capitalize(),
            modelo = modelo.capitalize(),
            color = color,
            anio = anio,
            tipo_alimentacion = tipo_alimentacion.capitalize(),
            modalidad = modalidad.capitalize(),
            tipo_freno = tipo_freno.capitalize(),
            precio = precio,
            tamanio_motor = tamanio_motor,
            tipo_motor = tipo_motor.capitalize(),
            tipo_ciclo = tipo_ciclo
           
        )
        self.inventario.append(moto)
        with open('inventario.txt','a',encoding='utf-8') as file:
            file.write(f'MOTOCICLETA|{moto.num_id}|{moto.marca}|{moto.modelo}|{moto.color}|{moto.anio}|{moto.tipo_alimentacion}|{moto.modalidad}|{moto.tipo_frenos}|{moto.precio}|{moto.tamanio_motor}|{moto.tipo_motor}|{moto.tipo_ciclo}\n')

    def generador_id(self):
        id_existente = True             
        while id_existente:
            nuevo_id = random.sample(range(1,1000), 1)[0]
            id_existente = False
            for x in self.inventario:
                if x.num_id == nuevo_id:
                    id_existente = True
        return nuevo_id

    def eliminar_vehiculo(self, num_id):
        hallado = False
        for x in self.inventario:
            if x.num_id == num_id:
                self.inventario.remove(x)
                hallado = True
                return f"El numero de ID {num_id} se elimino correctamente"
        return f"El numero de ID {num_id} no se encuentra"
                
    def modificar_precio(self, num_id, nuevo_precio :float):
        hallado = False
        for x in self.inventario:
            if x.num_id == num_id:
                x.precio = nuevo_precio
                hallado = True
                return f"el precio del vehiculo id {num_id} se cambio correctamente"
        return f"el numero id {num_id} no se encuentra"

    def venta_vehiculo(self, num_id):     
        hallado = False
        for x in self.inventario:
            if  x.num_id == num_id:
                self.inventario.remove(x)
                hallado = True
                with open('ventas.txt','a',encoding='utf-8') as file:     
                    file.write(f"{x.__class__.__name__},{x.num_id},{x.marca},{x.modelo}\n")                                 
                return f"Venta del vehiculo ID {num_id} Registrada"
        return f"El numero de ID {num_id} no se encuentra"
      
def cargar_catalogo(catalogo):
    vehiculos = []
    with open('inventario.txt',encoding='utf-8') as file:
         archivo = file.readlines()
         for linea in archivo:
             dato = linea.strip().split('|')
             tipo = dato [0]
             if tipo == 'BICICLETA':
                    _,num_id,marca,modelo,color,anio,_,modalidad,tipo_freno,precio,rodado,talle,transmision = linea.strip().split('|')
                    vehiculos.append(Bicicleta(num_id,marca,modelo,color,anio,_,modalidad,tipo_freno,precio,rodado,talle,transmision)) 
    return vehiculos

#agregar carga de autos y motos. 
#Ver def de Eliminar
# Agregar en ventas total y valor. 




if __name__ == '__main__':
        vehiculos = cargar_catalogo('vehiculos_registro.txt')
        concesionaria = Concesionaria(vehiculos)
        concesionaria.agregar_bici()
        for v in concesionaria.inventario:
            print(v)

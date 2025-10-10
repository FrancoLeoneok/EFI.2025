
#Parametrizacion
#Validaciones
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
    
    def eliminar_vehiculo(self, num_id: int):
        hallado = False
        for x in self.inventario:
            if x.num_id == num_id:
                self.inventario.remove(x)
                hallado = True
                return f"El numero de ID {num_id} se Elimino correctamente"
        if not hallado:
            return f"El numero de ID {num_id} no se encuentra"
            
        
        pass

    def modificar_precio(self):
        pass

    def venta_vehiculo(self, num_id : int):
        hallado = False
        for x in self.inventario:
            if x in num_id == num_id:
                self.inventario.remove(x)
                hallado = True
                with open('ventas.txt','a',encoding='utf-8') as file:     
                    file.write(f"{x.__class__.__name__},{Vehiculo.num_id},{Vehiculo.marca},{Vehiculo.modelo}\n")   #Se escribe en el txt ventas el vehiculo vendido.                              
                return f"Venta del vehiculo ID {num_id} Registrada"
        if not hallado:
            return f"El numero de ID {num_id} no se encuentra"
                    
        
        
        
        

    
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
                #print(bici)

if __name__ == '__main__':
    vehiculos = cargar_catalogo('vehiculos_registro.txt')
    concesionaria = Concesionaria(vehiculos)

    bici_nueva = Bicicleta(
        num_id= "6",
        marca = "orbea",
        modelo = "ze" ,
        color = "naranja",
        anio = "2020" ,
        tipo_alimentacion= None,
        modalidad = 'Todo terreno',
        tipo_freno = 'Hidraulico',
        precio = '1.200.000',
        rodado = '29',
        talle = 'L',
        transmision = '1x11'
        )
    concesionaria.agregar_vehiculo(bici_nueva)
    
    for elemento in concesionaria.inventario:
        print(elemento)


import random
def agregar_bici(concesionaria):
        from copia_clases import Bicicleta
        bicicleta:Bicicleta
        opciones_modalidad = ['montaña','gravel','ruta','descenso']
        opciones_talle = ['XS','S','M','L','XL']
        opciones_frenos = ['mecanicos','hidraulicos']
        opciones_rodado = ['26','27.5','28','29']

        marca = input(str('Ingrese la marca : '))
        modelo = input(str('Ingrese el modelo : '))
        transmision = input(str('Ingrese la transmision: '))
        color = input(str('Ingrese el color: '))

        def validacion(argumento,opciones,mensaje):
            variable_control = False
            while not variable_control:
                if argumento in opciones:
                    variable_control = True
                else:
                    print(f'{mensaje}')

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

        validacion_modalidad = False
        while not(validacion_modalidad):
            modalidad = input(f'Ingrese la modalidad {opciones_modalidad} : ') #
            if modalidad in opciones_modalidad:
                validacion_modalidad = True
            else:
                print(f'Solo Modalidades declaradas: {opciones_modalidad}')
        
        validacion_talle = False
        while not(validacion_talle):
            talle = input(str(f'Ingrese el talle del cuadro{opciones_talle} : '))
            if talle.capitalize() in opciones_talle:
                validacion_talle = True
            else:
                print(f'Solo talles declarados {opciones_talle}')

        validacion_frenos = False
        while not(validacion_frenos):
            tipo_freno = input(str(f'Ingrese el tipo de freno {opciones_frenos} : ')) # 
            if tipo_freno.strip() in opciones_frenos:
                validacion_frenos = True
            else:
                print(f'Solo tipo de frenos declarados {opciones_frenos}')

        validacion_rodado = False
        while not(validacion_rodado):
            rodado = input(str(f'Ingrese el rodado {opciones_rodado}: ')) #
            if rodado in opciones_rodado:
                validacion_rodado = True
            else:
                print(f'Rodados permitidos {opciones_rodado}')
        
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
        #anio = int(input('Ingrese el año: '))  # el año debe estar entre 2015 <= anio < 2026
        #modalidad = input(f'Ingrese la modalidad {opciones_modalidad} : ') #
        #rodado = input(str('Ingrese el rodado: ')) #
        #talle = input(str('Ingrese el talle del cuadro: ')) #
        bicicleta = Bicicleta(
            num_id = random.sample(range(1,100), 1)[0],    #metodo sample genera valor unico
            marca = marca,
            modelo = modelo,
            color = color,
            anio = anio,
            tipo_alimentacion = None,
            modalidad = modalidad,
            tipo_freno = tipo_freno,
            precio = precio,
            rodado = rodado,
            talle = talle,
            transmision = transmision
        )
        concesionaria.inventario.append(bicicleta)
        with open('persistencia.txt','a',encoding='utf-8') as file:
            file.write(f'BICICLETA|{bicicleta.num_id}|{bicicleta.marca}|{bicicleta.modelo}|{bicicleta.color}|{bicicleta.anio}|{bicicleta.tipo_alimentacion}|{bicicleta.modalidad}|{bicicleta.tipo_frenos}|{bicicleta.precio}|{bicicleta.rodado}|{bicicleta.talle}|{bicicleta.transmision}\n')

def eliminar_vehiculo(self, num_id: int):
        hallado = False
        for x in self.inventario:
            if x.num_id == num_id:
                self.inventario.remove(x)
                hallado = True
                return f"El numero de ID {num_id} se Elimino correctamente"
        if not hallado:
            return f"El numero de ID {num_id} no se encuentra"

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
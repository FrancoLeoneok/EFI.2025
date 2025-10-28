from clases import Concesionaria, cargar_catalogo

def mostrar_menu():
    print("MENU DE OPCIONES")
    print("="*30)
    print("1. Agregar bicicleta")
    print("2. Agregar auto")
    print("3. Agregar motocicleta")
    print("4. Listar inventario")
    print("5. Eliminar vehiculo (proximamente)")
    print("6. Vender Vehiculo (proximamente)")
    print("0. Salir")
    print("="*30)

def listar_inventario(concesionaria):
    for i, vehiculo in enumerate(concesionaria.inventario, 2):
        print(f"{i}. {vehiculo}")
    print("="*50)

def main():
    vehiculos = cargar_catalogo('inventario.txt') # carga el catalogo inicial
    concesionaria = Concesionaria(vehiculos)
    print(f"total de existencias: {len(concesionaria.inventario)-1} vehiculos")
    
    while True: # while del menu
        mostrar_menu()
        
        try:
            opcion = input("\nSeleccione una opción: ").strip()
            
            if opcion == "1":
                print("\n--- AGREGAR BICICLETA ---")
                concesionaria.agregar_bici()
                print("Se agreo la bicicleta")
                
            elif opcion == "2":
                print("\n--- AGREGAR AUTO ---")
                print("  Funcionalidad en desarrollo")
                # self.agregar_auto()
                
            elif opcion == "3":
                print("\n--- AGREGAR MOTOCICLETA ---")
                print("  Funcionalidad en desarrollo")
                # self.agregar_moto()
                
            elif opcion == "4":
                listar_inventario(concesionaria)
                
            elif opcion == "5":
                print("\n--- ELIMINAR VEHICULO ---")
                listar_inventario(concesionaria)
                try:
                    num_id = int(input("\nIngrese el ID del vehdculo a eliminar: "))
                    resultado = concesionaria.eliminar_vehiculo(num_id)
                    print(resultado)
                except ValueError:
                    print("debe ingresar un numero valido")
                
            elif opcion == "6":
                print("\n--- VENDER VEHICULO ---")
                print("  Funcionalidad en desarrollo")
                # self.venta_vehiculo()
                
            elif opcion == "0":
                print("\nSaliendo del sistema")
                break
                
            else:
                print("\nOpcion invslida, seleccione una opciion del menu.")

        except Exception as error:
            print(f"\nError inesperado: {error}")

if __name__ == '__main__':
    main()

from producto import Producto
from inventario import Inventario
import os

def limpiar_pantalla():
    # Limpiar la pantalla dependiendo del sistema operativo
    # Esta sentencia la saque de la web
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def mostrar_menu():
    # Mostrar el menú de opciones
    print("\nMENÚ DE GESTIÓN DE INVENTARIOS")
    print("--------------------------------------\n")
    print("1. AÑADIR PRODUCTO\n")
    print("2. ELIMINAR PRODUCTO\n")
    print("3. ACTUALIZAR PRODUCTO\n")
    print("4. BUSCAR PRODUCTO\n")
    print("5. MOSTRAR TODOS LOS PRODUCTOS\n")
    print("6. SALIR")
    print("\n--------------------------------------")

def main():
    inventario = Inventario()

    while True:
        limpiar_pantalla()  # Limpiar pantalla antes de mostrar el menú
        mostrar_menu()
        opcion = input("SELECCIONE UNA OPCIÓN: ")

        limpiar_pantalla()  # Limpiar pantalla después de seleccionar la opción

        if opcion == "1":
            id = input("INGRESE EL ID DEL PRODUCTO: ")
            nombre = input("INGRESE EL NOMBRE DEL PRODUCTO: ")
            cantidad = int(input("INGRESE LA CANTIDAD DEL PRODUCTO: "))
            precio = float(input("INGRESE EL PRECIO DEL PRODUCTO: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)
            input("\nPRESIONE ENTER PARA CONTINUAR...")

        elif opcion == "2":
            id = input("INGRESE EL ID DEL PRODUCTO A ELIMINAR: ")
            inventario.eliminar_producto(id)
            input("\nPRESIONE ENTER PARA CONTINUAR...")

        elif opcion == "3":
            id = input("INGRESE EL ID DEL PRODUCTO A ACTUALIZAR: ")
            print("-----------------------------------------------\n")
            cantidad = input("INGRESE LA NUEVA CANTIDAD (O PRESIONE ENTER PARA OMITIR): ")
            precio = input("INGRESE EL NUEVO PRECIO (O PRESIONE ENTER PARA OMITIR): ")

            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None

            inventario.actualizar_producto(id, cantidad, precio)
            input("\nPRESIONE ENTER PARA CONTINUAR...")

        elif opcion == "4":
            nombre = input("INGRESE EL NOMBRE DEL PRODUCTO A BUSCAR: ")
            print("-----------------------------------------------\n")
            inventario.buscar_producto(nombre)
            input("\nPRESIONE ENTER PARA CONTINUAR...")  # Pausa para que el usuario vea los resultados

        elif opcion == "5":
            inventario.mostrar_todos()
            input("\nPRESIONE ENTER PARA CONTINUAR...")  # Pausa para que el usuario vea los productos

        elif opcion == "6":
            print("SALIENDO DEL SISTEMA.")
            break

        else:
            print("OPCIÓN NO VÁLIDA. INTENTE DE NUEVO.")
            input("\nPRESIONE ENTER PARA CONTINUAR...")  # Pausa antes de limpiar y volver a mostrar el menú

if __name__ == "__main__":
    main()

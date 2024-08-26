from producto import Producto
import os

class Inventario:
    def __init__(self, archivo="txtinventario.txt"):
        self.productos = []
        self.archivo = archivo
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        #Carga los productos desde un archivo al iniciar el programa.
        try:
            with open(self.archivo, "r") as file:
                for linea in file:
                    datos = linea.strip().split(",")
                    if len(datos) == 4:
                        id, nombre, cantidad, precio = datos
                        producto = Producto(id, nombre, int(cantidad), float(precio))
                        self.productos.append(producto)
            print("INVENTARIO CARGADO DESDE EXITOSAMENTE.")
        except FileNotFoundError:
            print(f"ARCHIVO '{self.archivo}' NO ENCONTRADO. SE CREARA UNO NUEVO.")
            self.guardar_en_archivo()
        except PermissionError:
            print(f"NO SE TIENE PERMISO PARA LEER EL ARCHIVO '{self.archivo}'.")
        except Exception as e:
            print(f"OCURRIO UN ERROR AL CARGAR EL INVENTARIO: {e}")

    def guardar_en_archivo(self):
        #Guarda los productos en el archivo.
        try:
            with open(self.archivo, "w") as file:
                for producto in self.productos:
                    file.write(f"{producto.id},{producto.nombre},{producto.cantidad},{producto.precio}\n")
            print("-----------------------------------------------\n")
            print("INVENTARIO ACTUALIZADO EXITOSAMENTE.")
        except PermissionError:
            print(f"NO SE TIENE PERMISO PARA ESCRIBIR EN EL ARCHIVO '{self.archivo}'.")
        except Exception as e:
            print(f"OCURRIO UN ERROR AL GUARDAR EL INVENTARIO: {e}")

    def añadir_producto(self, producto):
        if self.buscar_por_id(producto.id):
            print(f"ERROR: YA EXISTE UN PRODUCTO CON ID {producto.id}.")
        else:
            self.productos.append(producto)
            self.guardar_en_archivo()

    def eliminar_producto(self, id):
        producto = self.buscar_por_id(id)
        if producto:
            self.productos.remove(producto)
            self.guardar_en_archivo()
            print(f"PRODUCTO CON ID {id} ELIMINADO.")
        else:
            print(f"NO SE ENCONTRO UN PRODUCTO CON ID {id}.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        producto = self.buscar_por_id(id)
        if producto:
            if cantidad is not None:
                producto.cantidad = cantidad
            if precio is not None:
                producto.precio = precio
            self.guardar_en_archivo()
            print(f"PRODUCTO CON ID {id} ACTUALIZADO.")
        else:
            print(f"NO SE ENCONTRO UN PRODUCTO CON ID {id}.")

    def buscar_producto(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        if resultados:
            for producto in resultados:
                print(f"ID: {producto.id}, NOMBRE: {producto.nombre}, CANTIDAD: {producto.cantidad}, PRECIO: {producto.precio}")
        else:
            print(f"NO SE ENCONTRARON PRODUCTOS CON EL NOMBRE '{nombre}'.")

    def mostrar_todos(self):
        if self.productos:
            for producto in self.productos:
                print(f"ID: {producto.id}, NOMBRE: {producto.nombre}, CANTIDAD: {producto.cantidad}, PRECIO: {producto.precio}")
        else:
            print("NO HAY PRODUCTOS EN EL INVENTARIO.")

    def buscar_por_id(self, id):
        for producto in self.productos:
            if producto.id == id:
                return producto
        return None

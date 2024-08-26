class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        # Constructor para inicializar los atributos de un producto.
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Métodos getters para acceder a los atributos del producto.
    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Métodos setters para modificar los atributos del producto.
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    # Método especial para representar el objeto como una cadena de texto.
    # Esto facilita la impresión de información del producto.
    def __str__(self):
        return f"ID: {self.id}, NOMBRE: {self.nombre}, CANTIDAD: {self.cantidad}, PRECIO: {self.precio:.2f}"

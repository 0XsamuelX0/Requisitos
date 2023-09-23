class CarroCompra:
    def __init__(self):
        self.productos = []
        self.usuarios = []
        self.bares = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def agregar_bar(self, bar):
        self.bares.append(bar)

    def mostrar_carro(self):
        print("Productos en el carrito:")
        for producto in self.productos:
            print(f"Nombre: {producto.nombre}, Precio: {producto.precio}, Stock: {producto.stock}")

        print("\nUsuarios:")
        for usuario in self.usuarios:
            usuario.Usuario_Crear()

        print("\nBares:")
        for bar in self.bares:
            bar.mostrar_info_bar()


if __name__ == "__main__":
    from crear_usuario import CrearUsuario
    from crear_bar import Bar

    carro = CarroCompra()

    producto1 = Producto("Producto 1", 10.0, 5)
    carro.agregar_producto(producto1)

    usuario1 = CrearUsuario("Juan", "Perez", 25)
    carro.agregar_usuario(usuario1)

    bar1 = Bar("Bar 1", "Dirección 1", "Ciudad 1")
    carro.agregar_bar(bar1)

    # Muestra el contenido del carro
    carro.mostrar_carro()

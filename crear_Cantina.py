class Bebida:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Bar:
    def __init__(self):
        self.enlistado = []

    def enlistar(self, bebida, precio):
        bebida_obj = Bebida(bebida, precio)
        self.enlistado.append(bebida_obj)

    def mostrar_enlistado(self):
        print("Enlistado de bebidas:")
        for bebida_obj in self.enlistado:
            print(f"Bebida: {bebida_obj.nombre}, Precio: {bebida_obj.precio}")

if __name__ == "__main__":
    bar = Bar()

    # Enlistamos algunas bebidas
    bar.enlistar("Cerveza", 5.0)
    bar.enlistar("Vino tinto", 7.0)
    bar.enlistar("Refresco", 2.0)

    # Mostramos el enlistado de bebidas
    bar.mostrar_enlistado()

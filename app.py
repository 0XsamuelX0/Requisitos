class Usuario:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def es_mayor_de_edad(self):
        return self.edad >= 18

    def crear_usuario(self):
        if self.es_mayor_de_edad():
            print("El usuario se puede crear:")
            print("Nombre:", self.nombre)
            print("Apellido:", self.apellido)
            print("Edad:", self.edad)
        else:
            print("El usuario", self.nombre, "no puede tener un registro ya que no cumple con la edad mínima de 18 años")

    def mostrar_usuario_creado(self):
        if self.es_mayor_de_edad():
            print("El usuario de nombre", self.nombre, "y de apellido", self.apellido, "ha sido creado")
        else:
            print("No se pudo crear el usuario debido a la edad insuficiente.")


class Bar:
    def __init__(self):
        self.enlistado = []

    def enlistar(self, bebida, precio):
        bebida_obj = {"nombre": bebida, "precio": precio}
        self.enlistado.append(bebida_obj)

    def mostrar_enlistado(self):
        print("Enlistado de bebidas:")
        for bebida_obj in self.enlistado:
            print(f"Bebida: {bebida_obj['nombre']}, Precio: {bebida_obj['precio']}")

def main():
    usuarios = [
        Usuario("Sebas", "Garcia", 20),
        Usuario("Jorge", "Garcia", 12),
        Usuario("Arnol", "Garcia", 22)
    ]

    for i, usuario in enumerate(usuarios, 1):
        print(f"-----------")
        print(f"Usuario #{i}")
        usuario.crear_usuario()
        usuario.mostrar_usuario_creado()

        bar = Bar()
        bar.enlistar("Guaro", 25000)
        bar.enlistar("Cerveza", 1500)
        bar.mostrar_enlistado()

if __name__ == "__main__":
    main()

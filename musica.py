# Simulador de Festival de Música

class Cancion:
    def __init__(self, titulo, artista, duracion=0, popularidad=0, lista_artistas=None):
        if lista_artistas is None:
            lista_artistas = []
        self.titulo = titulo
        self.artista = artista
        self.duracion = duracion
        self.popularidad = popularidad
        self.lista_artistas = lista_artistas

    def presentarse(self):
        print(f"Presentación en vivo: {self.titulo} de {self.artista} - Duración: {self.duracion} segundos")
    
    def mostrar_info(self):
        print(f"Título: {self.titulo}, Artista: {self.artista}, Duración: {self.duracion} segundos")

    def set_duracion(self, duracion):
        self.duracion = duracion

    def aumentar_popularidad(self):
        self.popularidad += 1

    def actuar(self):
        print(f"{self.artista} está actuando '{self.titulo}' en el escenario.")

    def despedirse(self):
        print(f"{self.artista} ha terminado su actuación de '{self.titulo}'. ¡Gracias por venir!")
    
    @staticmethod
    def iniciar_festival(lista_artistas):
        if not lista_artistas:
            print("No hay artistas en el festival.")
            return
        print("El festival de música ha comenzado con las siguientes actuaciones:")
        for artista in lista_artistas:
            artista.presentarse()
            artista.actuar()
            artista.despedirse()
        print("El festival de música ha concluido. ¡Gracias por asistir!")


class Cantante(Cancion):
    def __init__(self, titulo, artista, genero):
        super().__init__(titulo, artista)
        self.genero = genero

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Género: {self.genero}")


class DJ(Cancion):
    def __init__(self, titulo, artista, estilo):
        super().__init__(titulo, artista)
        self.estilo = estilo

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Estilo: {self.estilo}")


class Banda(Cancion):
    def __init__(self, titulo, artista, miembros):
        super().__init__(titulo, artista)
        self.miembros = miembros

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Miembros: {', '.join(self.miembros)}")


def main():
    print("===== Simulador de Festival de Música =====")
    lista_artistas = []

    while True:
        print("\n1. Registrar Cantante")
        print("2. Registrar DJ")
        print("3. Registrar Banda")
        print("4. Lista de artistas")
        print("5. Iniciar Festival")
        print("6. Salir")

        opcion = input("Seleccione una opción (1-6): ")

        if opcion in ['1', '2', '3']:
            titulo = input("Ingrese el título de la canción: ")
            artista = input("Ingrese el nombre del artista: ")
            duracion = int(input("Ingrese la duración de la canción en segundos: "))

            if opcion == '1':
                genero = input("Ingrese el género del cantante: ")
                cancion = Cantante(titulo, artista, genero)
            elif opcion == '2':
                estilo = input("Ingrese el estilo del DJ: ")
                cancion = DJ(titulo, artista, estilo)
            elif opcion == '3':
                miembros = input("Ingrese los nombres de los miembros de la banda separados por comas: ").split(',')
                cancion = Banda(titulo, artista, [m.strip() for m in miembros])

            cancion.set_duracion(duracion)
            lista_artistas.append(cancion)

            print("\n--- Información del artista registrado ---")
            cancion.mostrar_info()

        elif opcion == '4':
            if not lista_artistas:
                print("No hay artistas registrados.")
            else:
                print("\n--- Lista de Artistas Registrados ---")
                for artista in lista_artistas:
                    artista.mostrar_info()

        elif opcion == '5':
            Cancion.iniciar_festival(lista_artistas)

        elif opcion == '6':
            print("Saliendo del simulador. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


main()

import json
import os

class GestorTareas:
    def __init__(self):
        self.tareas = []
        self.archivo = "tareas.json"
        self.cargar()

    def guardar(self):
        with open(self.archivo, "w") as f:
            json.dump(self.tareas, f)

    def cargar(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, "r") as f:
                self.tareas = json.load(f)

    def añadir_tarea(self, nombre):
        self.tareas.append({"nombre": nombre, "completada": False})
        self.guardar()
        print(f"Tarea guardada: {nombre}")

    def listar_tareas(self):
        if not self.tareas:
            print("No tienes tareas.")
            return
        for i, tarea in enumerate(self.tareas):
            estado = "hecha" if tarea['completada'] else "pendiente"
            print(f"{i + 1}. {estado} {tarea['nombre']}")

    def completar_tarea(self, numero):
        if numero < 1 or numero > len(self.tareas):
            print("Numero de tarea no valido.")
            return
        self.tareas[numero - 1]['completada'] = True
        self.guardar()
        print(f"Tarea completada: {self.tareas[numero - 1]['nombre']}")

    def eliminar_tarea(self, numero):
        if numero < 1 or numero > len(self.tareas):
            print("Numero de tarea no valido.")
            return
        tarea = self.tareas.pop(numero - 1)
        self.guardar()
        print(f"Tarea eliminada: {tarea['nombre']}")

def menu():
    gestor = GestorTareas()
    while True:
        print("\n--- Todo CLI ---")
        print("1. Ver tareas")
        print("2. Añadir tarea")
        print("3. Completar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")
        opcion = input("Elige una opcion: ")
        if opcion == "1":
            gestor.listar_tareas()
        elif opcion == "2":
            nombre = input("Nombre de la tarea: ")
            gestor.añadir_tarea(nombre)
        elif opcion == "3":
            gestor.listar_tareas()
            if gestor.tareas:
                numero = int(input("Numero de tarea a completar: "))
                gestor.completar_tarea(numero)
        elif opcion == "4":
            gestor.listar_tareas()
            if gestor.tareas:
                numero = int(input("Numero de tarea a eliminar: "))
                gestor.eliminar_tarea(numero)
        elif opcion == "5":
            print("Hasta luego.")
            break
        else:
            print("Opcion no valida.")

menu()
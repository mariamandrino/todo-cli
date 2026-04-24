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
            estado = "hecha" if tarea["completada"] else "pendiente"
            print(f"{i + 1}.{estado} {tarea["nombre"]}")


gestor = GestorTareas()
gestor.añadir_tarea("Aprender GIT")
gestor.añadir_tarea("Terminar todo-cli")
gestor.listar_tareas()
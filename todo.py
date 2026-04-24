class GestorTareas:

    def __init__(self):
        self.tareas = []

    def añadir_tarea(self, nombre):
        self.tareas.append({"nombre": nombre, "completada": False})
        print(f"Tarea añadida: {nombre}")

    def listar_tareas(self):
        if not self.tareas:
            print("No tienes tareas.")
            return
        for i, tarea in enumerate(self.tareas):
            estado = "✓" if tareas["completada"] else "X"
            print(f"{i + 1}.{estado} {tarea["nombre"]}")


gestor = GestorTareas()

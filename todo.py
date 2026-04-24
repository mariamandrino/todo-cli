import json
import os
from rich.console import Console
from rich.table import Table
from rich import box

console = Console()

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
        console.print(f"[green]✓ Tarea añadida: {nombre}[/green]")

    def listar_tareas(self):
        if not self.tareas:
            console.print("[yellow]No tienes tareas todavía.[/yellow]")
            return
        tabla = Table(box=box.ROUNDED, show_header=True, header_style="bold cyan")
        tabla.add_column("Nº", style="dim", width=4)
        tabla.add_column("Tarea", min_width=20)
        tabla.add_column("Estado", width=10)
        for i, tarea in enumerate(self.tareas):
            if tarea['completada']:
                tabla.add_row(str(i + 1), f"[dim]{tarea['nombre']}[/dim]", "[green]hecha[/green]")
            else:
                tabla.add_row(str(i + 1), tarea['nombre'], "[yellow]pendiente[/yellow]")
        console.print(tabla)

    def completar_tarea(self, numero):
        if numero < 1 or numero > len(self.tareas):
            console.print("[red]Numero de tarea no valido.[/red]")
            return
        self.tareas[numero - 1]['completada'] = True
        self.guardar()
        console.print(f"[green]✓ Tarea completada: {self.tareas[numero - 1]['nombre']}[/green]")

    def eliminar_tarea(self, numero):
        if numero < 1 or numero > len(self.tareas):
            console.print("[red]Numero de tarea no valido.[/red]")
            return
        tarea = self.tareas.pop(numero - 1)
        self.guardar()
        console.print(f"[red]✗ Tarea eliminada: {tarea['nombre']}[/red]")

def menu():
    gestor = GestorTareas()
    while True:
        console.print("\n[bold cyan]╔══════════════════════╗[/bold cyan]")
        console.print("[bold cyan]║       Todo CLI       ║[/bold cyan]")
        console.print("[bold cyan]╚══════════════════════╝[/bold cyan]")
        console.print("  [cyan]1.[/cyan] Ver tareas")
        console.print("  [cyan]2.[/cyan] Añadir tarea")
        console.print("  [cyan]3.[/cyan] Completar tarea")
        console.print("  [cyan]4.[/cyan] Eliminar tarea")
        console.print("  [cyan]5.[/cyan] Salir")
        opcion = input("\nElige una opcion: ")
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
            console.print("\n[bold cyan]Hasta luego![/bold cyan]\n")
            break
        else:
            console.print("[red]Opcion no valida.[/red]")

menu()
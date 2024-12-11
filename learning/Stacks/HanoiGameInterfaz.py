#from Node import Node
#from Stack import Stack
import tkinter as tk
from tkinter import simpledialog, messagebox

class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node
    
    def set_next_node(self, next_node):
        if next_node != None and not isinstance(next_node, dict) and not isinstance(next_node, Node):
            raise TypeError("next_node must be of type Node, dict, or None")
        else:
            self.next_node = next_node


class Stack:
  def __init__(self, name):
    self.size = 0
    self.top_item = None
    self.limit = 1000
    self.name = name
  
  def push(self, value):
    if self.has_space():
      item = Node(value)
      item.set_next_node(self.top_item)
      self.top_item = item
      self.size += 1
    else:
      logging.warning('La pila esta llena ¡No queda espacio!')

  def pop(self):
    if self.size > 0:
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      return item_to_remove.get_value()
    logging.warning('La pila esta totalmente vacia!')

  def peek(self):
    if self.size > 0:
      return self.top_item.get_value()
    logging.warning('La pila esta totalmente vacia!')

  def has_space(self):
    return self.limit > self.size

  def is_empty(self):
    return self.size == 0
  
  def get_size(self):
    return self.size
  
  def get_name(self):
    return self.name
  
  def print_items(self):
    pointer = self.top_item
    print_list = []
    while(pointer):
      print_list.append(pointer.get_value())
      pointer = pointer.get_next_node()
    print_list.reverse()
    print("{0} Stack: {1}".format(self.get_name(), print_list))


import tkinter as tk
from tkinter import messagebox


class TorresDeHanoi:
    def __init__(self, master, num_discos, torre_objetivo):
        self.master = master
        self.master.title("Torres de Hanoi")
        self.master.geometry("900x600")
        self.master.configure(bg="#f4f4f9")

        # Configuración inicial
        self.num_discos = num_discos
        self.torre_objetivo = torre_objetivo
        self.movimientos = 0
        self.movimientos_minimos = 2 ** num_discos - 1

        # Inicialización de torres
        self.torres = [list(range(num_discos, 0, -1)), [], []]
        self.torre_origen = None

        # Configuración gráfica
        self.setup_gui()

    def setup_gui(self):
        # Panel izquierdo: Información del juego
        self.frame_info = tk.Frame(self.master, bg="#e0e7ff", relief=tk.RIDGE, bd=2)
        self.frame_info.pack(side=tk.LEFT, fill=tk.Y, padx=20, pady=20)

        # Título del juego
        tk.Label(self.frame_info, text="Torres de Hanoi", font=("Arial", 16, "bold"),
                 bg="#e0e7ff").pack(pady=10)

        instrucciones = (
            "Reglas del Juego:\n"
            "1. Mueve todos los discos de la torre inicial a la torre objetivo.\n"
            "2. Solo puedes mover un disco a la vez.\n"
            "3. No puedes colocar un disco grande sobre uno más pequeño.\n\n"
            "¡Buena suerte!"
        )
        tk.Label(self.frame_info, text=instrucciones, bg="#e0e7ff",
                 font=("Arial", 12), justify=tk.LEFT, wraplength=200).pack(pady=10)

        # Información de movimientos
        self.label_movimientos = tk.Label(
            self.frame_info, text=f"Movimientos: {self.movimientos}",
            font=("Arial", 14), bg="#e0e7ff", fg="#333333"
        )
        self.label_movimientos.pack(pady=10)

        # Información de la torre objetivo
        self.label_objetivo = tk.Label(
            self.frame_info, text=f"Torre objetivo: {self.torre_objetivo + 1}",
            font=("Arial", 14), bg="#e0e7ff", fg="#0056b3"
        )
        self.label_objetivo.pack(pady=10)

        # Botones de reinicio y cierre
        self.boton_reset = tk.Button(
            self.frame_info, text="Reiniciar Juego", command=self.resetear_juego,
            bg="#dc3545", fg="white", font=("Arial", 12), width=15
        )
        self.boton_reset.pack(pady=10)

        self.boton_cerrar = tk.Button(
            self.frame_info, text="Cerrar", command=self.master.quit,
            bg="#007bff", fg="white", font=("Arial", 12), width=15
        )
        self.boton_cerrar.pack(pady=10)

        # Lienzo para las torres
        self.canvas = tk.Canvas(self.master, width=700, height=400, bg="#dbe7ff")
        self.canvas.pack(pady=20)

        # Botones para seleccionar torres
        self.frame_botones = tk.Frame(self.master, bg="#f4f4f9")
        self.frame_botones.pack(pady=10)

        self.botones_torres = [
            tk.Button(self.frame_botones, text=f"Torre {i+1}",
                      command=lambda idx=i: self.seleccionar_torre(idx),
                      width=12, font=("Arial", 10, "bold"), bg="#4e79a7", fg="white",
                      activebackground="#f4d03f", activeforeground="black", relief=tk.GROOVE)
            for i in range(3)
        ]
        for boton in self.botones_torres:
            boton.pack(side=tk.LEFT, padx=10)

        # Dibujar torres iniciales
        self.dibujar_torres()

    def dibujar_torres(self):
        self.canvas.delete("all")
        colores = ['#ff5733', '#33ff57', '#3357ff', '#ff33a8', '#ffcc33', '#33ffff', '#ff33ff', '#8e44ad']

        for i, torre in enumerate(self.torres):
            x_centro = 200 * (i + 1)
            self.canvas.create_rectangle(x_centro - 100, 350, x_centro + 100, 370, fill="#8b4513")
            self.canvas.create_rectangle(x_centro - 10, 150, x_centro + 10, 350, fill="#8b4513")

            for j, disco in enumerate(torre):
                ancho = 20 * disco
                color = colores[disco - 1]
                y = 350 - (j + 1) * 20
                self.canvas.create_rectangle(
                    x_centro - ancho / 2, y, x_centro + ancho / 2, y + 20,
                    fill=color, outline="black"
                )

    def seleccionar_torre(self, idx):
        if self.torre_origen is None:
            if not self.torres[idx]:
                messagebox.showwarning("Movimiento inválido", "La torre seleccionada está vacía.")
                return
            self.torre_origen = idx
            self.botones_torres[idx].config(bg="yellow")
        else:
            if self.torre_origen == idx:
                messagebox.showwarning("Movimiento inválido", "No puedes mover un disco a la misma torre.")
                self.botones_torres[self.torre_origen].config(bg="#4e79a7")
                self.torre_origen = None
                return

            if self.es_movimiento_valido(self.torre_origen, idx):
                disco = self.torres[self.torre_origen].pop()
                self.torres[idx].append(disco)
                self.movimientos += 1
                self.label_movimientos.config(text=f"Movimientos: {self.movimientos}")
                self.dibujar_torres()

                if len(self.torres[self.torre_objetivo]) == self.num_discos:
                    messagebox.showinfo(
                        "¡Victoria!",
                        f"¡Completaste el juego en {self.movimientos} movimientos! "
                        f"(Mínimos: {self.movimientos_minimos})"
                    )
                    self.resetear_juego()
            else:
                messagebox.showerror("Movimiento inválido",
                                     "No puedes colocar un disco grande sobre uno más pequeño.")

            self.botones_torres[self.torre_origen].config(bg="#4e79a7")
            self.torre_origen = None

    def es_movimiento_valido(self, origen, destino):
        if not self.torres[origen]:
            return False
        if not self.torres[destino] or self.torres[origen][-1] < self.torres[destino][-1]:
            return True
        return False

    def resetear_juego(self):
        self.torres = [list(range(self.num_discos, 0, -1)), [], []]
        self.movimientos = 0
        self.label_movimientos.config(text=f"Movimientos: 0")
        self.torre_origen = None
        for boton in self.botones_torres:
            boton.config(bg="#4e79a7")
        self.dibujar_torres()


def iniciar_juego():
    root = tk.Tk()
    root.withdraw()

    # Configuración inicial
    num_discos = simpledialog.askinteger("Torres de Hanoi", "Número de discos (3-8):", minvalue=1, maxvalue=8)
    if num_discos:
        torre_objetivo = simpledialog.askinteger("Torres de Hanoi", "Selecciona torre objetivo (2 o 3):", minvalue=1,
                                                 maxvalue=3) - 1
        root.deiconify()
        TorresDeHanoi(root, num_discos, torre_objetivo)
        root.mainloop()


if __name__ == "__main__":
    iniciar_juego()

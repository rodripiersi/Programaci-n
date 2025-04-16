import tkinter as tk

def mostrarOpcion1():
    limpiarVentana()
    label = tk.Label(ventana, text="Elegiste la Opción 1", font=("Arial", 16))
    label.pack(pady=20)

    boton_volver = tk.Button(ventana, text="Volver", font=("Arial", 12), command=mostrarMenu)
    boton_volver.pack(pady=10)

def mostrarOpcion2():
    limpiarVentana()
    label = tk.Label(ventana, text="Elegiste la Opción 2", font=("Arial", 16))
    label.pack(pady=20)

    boton_volver = tk.Button(ventana, text="Volver", font=("Arial", 12), command=mostrarMenu)
    boton_volver.pack(pady=10)

def limpiarVentana():  
    # Recorremos todos los widgets (elementos gráficos) que están dentro de la ventana
    for widget in ventana.winfo_children():  
        # Eliminamos cada widget para limpiar la ventana completamente
        widget.destroy()

        
def mostrarMenu():
    limpiarVentana()
    label = tk.Label(ventana, text="Menú Principal", font=("Arial", 18, "bold"))
    label.pack(pady=20)

    boton1 = tk.Button(ventana, text="Opción 1", font=("Arial", 14), width=20, command=mostrarOpcion1)
    boton1.pack(pady=10)

    boton2 = tk.Button(ventana, text="Opción 2", font=("Arial", 14), width=20, command=mostrarOpcion2)
    boton2.pack(pady=10)

def main():
    global ventana
    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.geometry("400x300")
    ventana.title("Menú Centrado")

    # Mostrar el menú visual al inicio
    mostrarMenu()

    ventana.mainloop()

if __name__=="__main__":
    main()

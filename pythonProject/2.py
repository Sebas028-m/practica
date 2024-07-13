import tkinter as tk
from PIL import Image, ImageTk

# Función para cargar y configurar el ícono
def set_app_icon(window, icon_path):
    icon = Image.open(icon_path)
    window.iconphoto(True, ImageTk.PhotoImage(icon))

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ventana con Favicon")

# Llamar a la función para configurar el ícono (ruta relativa al mismo directorio)
set_app_icon(ventana, "favicon.ico")  # Asegúrate de que favicon.ico esté en el mismo directorio que 2.py

# Añadir widgets, botones, etc., según sea necesario
label = tk.Label(ventana, text="Hola Mundo!")
label.pack(padx=20, pady=20)

# Ejecutar el bucle principal de Tkinter
ventana.mainloop()

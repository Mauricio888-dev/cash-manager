import tkinter as tk
import database
root = tk.Tk()
root.geometry("720x500")

def dinero_en_cuenta():
    cantidad = database.calcular_dinero_en_cuenta(1)
    saldo_var.set(f"{cantidad} pesos")

    
saldo_var = tk.StringVar()
saldo_var.set("0")


def nuevo_registro():
    ventana2 = tk.Tk()
    ventana2.geometry("300x300")

    origen_lbl=tk.Label(ventana2, text="ingrese el origen")
    origent_input = tk.Entry(ventana2)

    añadido_lbl=tk.Label(ventana2, text="es ingreso o retiro: 0 = retiro, 1 = ingreso")
    añadido_input = tk.Entry(ventana2)

    cantidad_lbl=tk.Label(ventana2, text="ingrese la cantidad")
    cantidad_input = tk.Entry(ventana2)

    origen_lbl.pack()
    origent_input.pack()

    añadido_lbl.pack()
    añadido_input.pack()

    cantidad_lbl.pack()
    cantidad_input.pack()

    def registrar (): 
        valor_origen = origent_input.get()
        valor_añadido = añadido_input.get()
        valor_cantidad = cantidad_input.get()
        if valor_origen == '' or valor_añadido=='' or  valor_cantidad== '':
            print("eta vaina e seria")
        database.añadir_registro(valor_origen, valor_añadido,  valor_cantidad, 1)
        dinero_en_cuenta()
        ventana2.destroy()

    boton_registrar = tk.Button(ventana2, text="confirmar registro", command=registrar)
    #    database.añadir_registro(valor_origen, valor_añadido,  valor_cantidad, 1)
    boton_registrar.pack()
    ventana2.mainloop()
    

header = tk.Frame(root)
dinero = tk.Label(header, textvariable=saldo_var, fg="black", font=("Arial", 16))

actualizar_dinero = tk.Button(root, text="Calcular dinero", command=dinero_en_cuenta)
añadir_registro = tk.Button(root, text="Añadir registro", command=nuevo_registro)

header.pack(pady="30px")
dinero.pack()

actualizar_dinero.pack()
añadir_registro.pack()

root.mainloop()
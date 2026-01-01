import tkinter as tk
import database
root = tk.Tk()
root.geometry("720x500")

header = tk.Frame(root)
dinero = tk.Label(header, text="0 peso", fg="black", font=("Arial", 16))




header.pack(pady="30px")
dinero.pack()




root.mainloop()
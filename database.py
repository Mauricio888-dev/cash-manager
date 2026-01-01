import sqlite3

conexion = sqlite3.connect("cash_register_DB.db")
conexion.execute("PRAGMA foreign_keys = ON")

# Crear un cursor para ejecutar comandos SQL
cursor = conexion.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    money REAL

)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS registros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,    
    origen TEXT NOT NULL,
    añadido INTEGER,
    cantidad REAL,
    id_usuario INTENGER,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id)
)
""")
#
# Al usar la funcion registrar solo se requiere el nombre ya que se ingresa con un 0 en el campo "money"
#

def registrar (nombre):
    cursor.execute("INSERT INTO usuarios (nombre, money) VALUES (?, ?)", (nombre, 0))
    conexion.commit()  # Guardar cambios

def añadir_registro (origen, añadido, cantidad, id_usuario):
    cursor.execute("""INSERT INTO registros (origen, añadido, cantidad, id_usuario) 
        VALUES (?, ?, ?, ?)""", (origen, añadido, cantidad, id_usuario))
    conexion.commit()

def calcular_dinero_en_cuenta(id_user):
    # Consulta segura con parámetros
    cursor.execute("""
        SELECT SUM(
            CASE WHEN añadido = 0 THEN -cantidad ELSE cantidad END
        )
        FROM registros
        WHERE id_usuario = ?
    """, (id_user,))
    total = cursor.fetchone()[0] or 0
    cursor.execute("UPDATE usuarios SET money = ? WHERE id = ?", (total, id_user,))
    print(f"Dinero en cuenta del usuario {id_user}: {total}")
    return total

registrar("Mau")
añadir_registro("pago", 1, 500000, 1)
calcular_dinero_en_cuenta(1)

cursor.execute("SELECT * FROM usuarios")
for fila in cursor.fetchall():
    print(fila)
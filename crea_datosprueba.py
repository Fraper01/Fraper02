import sqlite3
import pandas as pd

def crear_data_prueba_sqlite():
    """Crea una base de datos SQLite 'ejemplo.db' con la tabla 'estudiantes' y datos de prueba."""
    conn = None
    try:
        conn = sqlite3.connect('ejemplo.db')
        cursor = conn.cursor()

        # Eliminar la tabla si ya existe para empezar con datos limpios
        cursor.execute("DROP TABLE IF EXISTS estudiantes")

        # Crear la tabla 'estudiantes'
        cursor.execute("""
            CREATE TABLE estudiantes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                sexo TEXT,
                edad INTEGER,
                puntuacion REAL
            )
        """)
        print("Tabla 'estudiantes' creada.")

        # Insertar algunos datos de prueba
        datos_estudiantes = [
            ('Ana', 'F', 20, 8.5),
            ('Carlos', 'M', 22, 7.9),
            ('Sofía', 'F', 21, 9.2),
            ('Javier', 'M', 19, 6.8),
            ('Lucía', 'F', 23, 8.8)
        ]
        cursor.executemany("INSERT INTO estudiantes (nombre, sexo, edad, puntuacion) VALUES (?, ?, ?, ?)", datos_estudiantes)
        conn.commit()
        print("Datos de prueba insertados en la tabla 'estudiantes'.")

    except sqlite3.Error as e:
        print(f"Error al crear la base de datos o la tabla: {e}")
    finally:
        if conn:
            conn.close()
            print("Conexión a la base de datos cerrada.")

if __name__ == "__main__":
    crear_data_prueba_sqlite()

    # Después de crear la base de datos, puedes ejecutar tu código original para leer los datos
    conn_lectura = None
    try:
        conn_lectura = sqlite3.connect('ejemplo.db')
        sql_query = "SELECT nombre, sexo, edad, puntuacion FROM estudiantes"
        df_from_sql = pd.read_sql_query(sql_query, conn_lectura)
        print("\nDataFrame leído desde la base de datos:")
        print(df_from_sql)

    except sqlite3.Error as e:
        print(f"\nError al leer desde la base de datos: {e}")
    finally:
        if conn_lectura:
            conn_lectura.close()
            print("Conexión de lectura cerrada.")
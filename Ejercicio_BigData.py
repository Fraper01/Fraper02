import pandas as pd

# Datos 
data = {
    'Número de pedido': [
        1, 2, 3, 4, 5,
        6, 7, 8, 9, 10,
        11, 12
    ],
    'Nombre del cliente': [
        'María López', 'Juan Pérez', 'Laura Hernández', 'Carlos Ramírez', 'Sofía Gómez',
        'Andrés Jiménez', 'Marta Ruiz', 'Luis Torres', 'Julia Vega', 'Pedro Silva',
        'Ana Rojas', 'Manuel Castillo'
    ],
    'Tipo de mercancía': [
        'Alimentos frescos', 'Electrónicos', 'Ropa', 'Medicinas', 'Muebles',
        'Alimentos secos', 'Electrodomésticos','Juguetes', 'Material escolar', 'Productos químicos',
        'Equipos médicos', 'Piezas industriales'
    ],
    'Peso (kg)': [
        20, 50, 120, 10, 800,
        500, 200, 150, 80, 600,
        100, 1200
    ],
    'Origen': [
        'Valencia', 'Barcelona', 'Alicante', 'Madrid', 'Zaragoza',
        'Salamanca', 'Sevilla', 'Madrid', 'Toledo', 'Valencia',
        'Barcelona', 'Cádiz'
    ],
    'Destino': [
        'Madrid', 'Sevilla', 'Málaga', 'Bilbao', 'Valladolid',
        'León', 'Granada', 'Palma de Mallorca', 'Albacete', 'Tarragona', 
        'Zaragoza', 'Las Palmas'
    ],
    'Medio de transporte': [
        'Camión', 'Avión', 'Camión', 'Avión', 'Camión',
        'Tren', 'Camión', 'Avión', 'Camión', 'Camión',
        'Tren', 'Barco'
    ],
    'Fecha de entrega': [
        '2025-01-05', '2025-01-04', '2025-01-06', '2025-01-03', '2025-01-07',
        '2025-01-08', '2025-01-06', '2025-01-05', '2025-01-07', '2025-01-04',
        '2025-01-06', '2025-01-09'
    ]
}

# Crear el DataFrame
df_entregaPedidos = pd.DataFrame(data)

# Mostrar la tabla
print("Tabla de Entrega de Pedidos:")
print(df_entregaPedidos)

#Guardar la tabla en un archivo CSV y Excel
df_entregaPedidos.to_csv('entregaPedidos.csv', index=False)

print("\nLa tabla ha sido creada con éxito. ")
print("El archivo 'entregaPedidos.csv' ha sido guardado.")

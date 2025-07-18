
class Consulta:
    CREATE = '''
			CREATE TABLE empleado (
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			NOMBRE VARCHAR(50) NOT NULL,
			CARGO VARCHAR(50) NOT NULL,
			SALARIO INT NOT NULL);
			'''
    DELETE_TABLE = "DROP TABLE empleado;"

    INSERT = "INSERT INTO empleado VALUES(NULL,?,?,?);"

    SELECT = "SELECT * FROM empleado;"

    UPDATE = "UPDATE empleado SET NOMBRE=?, CARGO=?, SALARIO=? WHERE ID="

    DELETE = "DELETE FROM empleado WHERE ID="

    BUSCAR = "SELECT * FROM empleado WHERE nombre LIKE '%' || ? || '%'"

    
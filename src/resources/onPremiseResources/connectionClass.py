import pyodbc
import logging

from src.interfaces.resources.dbConnection import IDBConnection

logger = logging.getLogger()
logger.setLevel(logging.INFO)

class BancoRelationalDBResource(IDBConnection):
    def __init__(self):
        server_address = 'localhost'
        db_name = 'Banco'
        connection_string = (
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={server_address};"
            f"DATABASE={db_name};"
            "Trusted_Connection=yes;"
        )
        try:
            self.connection = pyodbc.connect(connection_string)
            logger.info('Conexión a la base de datos exitosa')
        except pyodbc.Error as e:
            logger.error(f'Error de conexión: {e}')
            raise

    def db_connection(self, query, sp_type):
        logger.info('Inicio conexión a Banco')
        try:
            with self.connection.cursor() as cursor:
                logger.info('Conexión exitosa con Banco')
                logger.info(f'Inicio ejecución de la query de {sp_type}')
                cursor.execute(query)
                logger.info('Ejecución de la query exitosa')
                sp_type_list = [dict(line) for line in [zip(
                    [column[0] for column in cursor.description], row) for row in cursor.fetchall()]]
                return sp_type_list
        except pyodbc.Error as e:
            logger.error(f'Error durante la consulta: {e}')
            raise

    def db_connection_result(self, query, sp_type):
        logger.info('Inicio conexión a Banco')
        try:
            with self.connection.cursor() as cursor:
                logger.info('Conexión exitosa con Banco')
                logger.info(f'Inicio ejecución de la query de {sp_type}')
                cursor.execute(query)
                logger.info('Ejecución de la query exitosa')
                message = {"Message": "Se ha ejecutado de manera correcta el query"}
                return message
        except pyodbc.Error as e:
            logger.error(f'Error durante la consulta: {e}')
            raise

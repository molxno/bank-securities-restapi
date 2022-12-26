# Implementa la conexión a la db
import pyodbc
import logging

from src.interfaces.resources.dbConnection import IDBConnection

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class BancoRelationalDBResource(IDBConnection):

    def __init__(self):
        server_address = 'PMEDMOLANOSA'
        db_name = 'Banco'
        username = 'santiago'
        password = 'santiago'
        self.connection = pyodbc.connect(
            "DRIVER={SQL Server}; SERVER="+server_address+"; DATABASE ="+db_name+';UID='+username+';PWD=' + password)

    def db_connection(self, query, sp_type):
        # Metodo de conexion y consulta a Banco
        logger.info('Inicio conexión a Banco')

        with self.connection as connection:
            cursor = connection.cursor()
            # OK! conexión exitosa
            logger.info('Conexion exitosa con Banco')
            # Inicio de consulta
            logger.info(f'Inicio ejecución de la query de {sp_type}')
            cursor.execute(query)
            # consulta exitosa
            logger.info('Ejecucion de la query Exitosa')
            sp_type_list = [dict(line) for line in [zip(
                [column[0] for column in cursor.description], row) for row in cursor.fetchall()]]
            return sp_type_list

    def db_connection_result(self, query, sp_type):
        # Metodo de conexion y consulta a Banco
        logger.info('Inicio conexión a Banco')

        with self.connection as connection:
            cursor = connection.cursor()
            # OK! conexión exitosa
            logger.info('Conexion exitosa con Banco')
            # Inicio de consulta
            logger.info(f'Inicio ejecución de la query de {sp_type}')
            cursor.execute(query)
            # consulta exitosa
            logger.info('Ejecucion de la query Exitosa')
            message = {"Message": "Se ha ejecutado de manera correcta el query"}
            return message

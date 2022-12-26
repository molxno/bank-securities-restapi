# Implementa la consulta a bd
import logging
from re import U

from src.resources.onPremiseResources.connectionClass import BancoRelationalDBResource
from src.interfaces.DAO.titulosBancariosQuerie import QueriesDAO

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class TituloBancario(QueriesDAO):

    def get_titulos_bancarios(self):
        # Metodo para obtener titulos bacarios de bd ods
        logger.info(
            '#START de petición de titulos bancarios desde el Data Access Object')
        query = """ 
        SELECT 
            [ID]
            ,[Titulo]
            ,[Clasificacion]
            ,[Valor]
            ,[FechaCreacion]
            ,[FechaVencimiento]
            ,[PagoCuota]
        FROM
            [Banco].[dbo].[tblTitulosBancarios]
      """
        banco_db_resource = BancoRelationalDBResource()
        return banco_db_resource.db_connection(query, 'Todos los Titulos Bancarios')

    def get_titulo_bancario(self, ID):
        # Metodo para obtener titulo bacario en especifico de bd ods
        logger.info(
            '#START de petición de un titulo bancario en especifico desde el Data Access Object')
        query = "SELECT * FROM [Banco].[dbo].[tblTitulosBancarios] WHERE [ID] = " + str(
            ID)
        banco_db_resource = BancoRelationalDBResource()
        return banco_db_resource.db_connection(query, 'Titulo Bancario en especifico')

    def patch_paga_titulo_bancario(self, ID):
        # Metodo para registrar el pago de un titulo bancario
        logger.info(
            '#START de pago de un titulo bancario en especifico desde el Data Access Object')
        query = "UPDATE [Banco].[dbo].[tblTitulosBancarios] SET [PagoCuota] = 'y' WHERE [ID] =" + \
            str(ID)
        banco_db_resource = BancoRelationalDBResource()
        return banco_db_resource.db_connection_result(query, 'Pago de Titulo Bancario en especifico')

    def post_titulo_bancario(self, Titulo, Clasificacion, Valor, FechaCreacion, FechaVencimiento, PagoCuota):
        # Metodo para registrar un titulo bancario
        logger.info(
            '#START de nuevo titulo bancario desde el Data Access Object')
        query = "INSERT INTO [Banco].[dbo].[tblTitulosBancarios] ([Titulo],[Clasificacion],[Valor],[FechaCreacion],[FechaVencimiento],[PagoCuota]) VALUES ('" + \
            Titulo+"','"+Clasificacion+"','"+Valor+"','" + \
                FechaCreacion+"','"+FechaVencimiento+"','"+PagoCuota+"')"
        banco_db_resource = BancoRelationalDBResource()
        return banco_db_resource.db_connection_result(query, 'Nuevo Titulo Bancario')

    def delete_titulo_bancario(self, ID):
        # Metodo para eliminar un titulo bancario
        logger.info(
            '#START de eliminación de titulo bancario desde el Data Access Object')
        query = "DELETE FROM [Banco].[dbo].[tblTitulosBancarios] WHERE [ID] = " + \
            str(ID)
        banco_db_resource = BancoRelationalDBResource()
        return banco_db_resource.db_connection_result(query, 'Elimina Titulo Bancario en especifico')

    def patch_nueva_fecha_titulo_bancario(self, FechaCreacion, NuevaFecha):
        # Metodo para modificar la fecha de creacion de un titulo bancario
        logger.info(
            '#START edicion fecha creacion de titulos bancarios desde el Data Access Object')
        query = "UPDATE [Banco].[dbo].[tblTitulosBancarios] SET [FechaCreacion] = '" + \
            str(NuevaFecha) + \
            "' WHERE [FechaCreacion] = '" + str(FechaCreacion) + "'"
        banco_db_resource = BancoRelationalDBResource()
        return banco_db_resource.db_connection_result(query, 'Edita Fecha Creacion Titulos Bancarios')

    def validaTitulo(self, array1, array2):
        return [x for x in array1 if x in array2]

    def formatoTitulo(self, string):
        replacements = (
            ("á", "a"),
            ("é", "e"),
            ("í", "i"),
            ("ó", "o"),
            ("ú", "u"),
        )
        for a, b in replacements:
            string = string.replace(a, b).replace(a.upper(), b.upper())
            s = string.upper()
        return s

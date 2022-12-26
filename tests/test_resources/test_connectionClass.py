from src.resources.onPremiseResources.connectionClass import BancoRelationalDBResource
from tests.mocks import titulo_bancario_rows

def test_db_connection():
    query = "SELECT * FROM [Banco].[dbo].[tblTitulosBancarios] WHERE [ID] = 2"
    assert BancoRelationalDBResource().db_connection(query, "Consulta los titulos bancarios") == titulo_bancario_rows

def test_db_connection_result():
    query = "SELECT * FROM [Banco].[dbo].[tblTitulosBancarios] WHERE [ID] = 2"
    assert BancoRelationalDBResource().db_connection_result(query, "Consulta los titulos bancarios") == {"Message": "Se ha ejecutado de manera correcta el query"}
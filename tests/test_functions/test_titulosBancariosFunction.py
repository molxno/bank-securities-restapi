from src.main import app
from fastapi.testclient import TestClient


client = TestClient(app)

def test_status_code_titulos_bancarios():
    response = client.get("/titulosbancarios")
    assert response.status_code == 200

def test_status_code_titulo_bancario():
    response = client.get("/titulosbancarios/3")
    assert response.status_code == 200

def test_status_code_pago():
    response = client.patch("/titulosbancarios/paga/4")
    assert response.status_code == 200

def test_status_code_elimina():
    response = client.delete("/titulosbancarios/eliminar/99999")
    assert response.status_code == 200

def test_status_code_fecha():
    response = client.patch("/titulosbancarios/editafechacreacion/2022-01-01/2022-09-09")
    assert response.status_code == 200

#Falta metodo post
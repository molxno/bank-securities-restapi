import pandas as pd
import random

from tests.mocks import titulos_bancarios_mock
from src.services.tituloBancarioService import TituloBancario

def test_get_titulos_bancarios():

    expected_processed = [
        {
            "ID": 1,
            "Titulo": "USD",
            "Clasificacion": "DOLAR",
            "Valor": 500000000,
            "FechaCreacion": "2022-03-14",
            "FechaVencimiento": "2023-03-15",
            "PagoCuota": "y"
        },
        {
            "ID": 2,
            "Titulo": "TRPV",
            "Clasificacion": "TITULO DE PARTICIPACION RENTA VARIABLE",
            "Valor": 256000000,
            "FechaCreacion": "2022-08-25",
            "FechaVencimiento": "2023-08-26",
            "PagoCuota": "y"
        },
        {
            "ID": 3,
            "Titulo": "TP",
            "Clasificacion": "TITULO DE PARTICIPACION",
            "Valor": 360000000,
            "FechaCreacion": "2022-02-16",
            "FechaVencimiento": "2023-02-17",
            "PagoCuota": "y"
        }
    ]

    expected = pd.DataFrame(expected_processed).T
    response = titulos_bancarios_mock

    assert response.T.to_dict() == expected.T.to_dict()


def test_get_titulo_bancario():
    assert len(TituloBancario().get_titulo_bancario(
        1)) == 1 or TituloBancario().get_titulo_bancario(1) == []


def test_patch_paga_titulo_bancario():
    assert TituloBancario().patch_paga_titulo_bancario(
        2) == {"Message": "Se ha ejecutado de manera correcta el query"}


def test_post_titulo_bancario():
    valor = str(random.randint(1230050, 900000000))
    assert TituloBancario().post_titulo_bancario("THI", "BONOS DEL TESORO EEUU", valor,
                                                 "2022-04-24", "2023-04-26", "n") == {"Message": "Se ha ejecutado de manera correcta el query"}


def test_delete_titulo_bancario():
    assert TituloBancario().delete_titulo_bancario(
        9999) == {"Message": "Se ha ejecutado de manera correcta el query"}


def test_patch_nueva_fecha_titulo_bancario():
    assert TituloBancario().patch_nueva_fecha_titulo_bancario("2022-03-14",
                                                              "2022-03-15") == {"Message": "Se ha ejecutado de manera correcta el query"}


def test_validaTitulo():
    assert TituloBancario().validaTitulo(
        ["COP"], ["USD", "TRPV", "TP", "TID", "THI", "TESU", "TEST", "TESP", "TESOROS", "TESI"]) == []


def test_formatoTitulo():
    assert TituloBancario().formatoTitulo("TÍTuLo dE PaRTICíPACIÓn") == "TITULO DE PARTICIPACION"
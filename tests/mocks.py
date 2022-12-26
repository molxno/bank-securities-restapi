import pandas as pd

titulos_bancarios_rows = [
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

titulos_bancarios_mock = pd.DataFrame(titulos_bancarios_rows).T

titulo_bancario_rows = [
    {
        "ID": 2,
        "Titulo": "TRPV",
        "Clasificacion": "TITULO DE PARTICIPACION RENTA VARIABLE",
        "Valor": 256000000,
        "FechaCreacion": "2022-08-25",
        "FechaVencimiento": "2023-08-26",
        "PagoCuota": "y"
    }    
]
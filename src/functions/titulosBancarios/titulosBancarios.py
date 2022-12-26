# AQUI VA LA RUTA DE FASTAPI
import logging
from fastapi import APIRouter

from src.services.tituloBancarioService import TituloBancario
from src.utils.common import build_error_response

from pydantic import BaseModel
from pydantic import Field
from datetime import date

logger = logging.getLogger()
logger.setLevel(logging.INFO)

router = APIRouter()

# Validaciones
titulos = ["USD", "TRPV", "TP", "TID", "THI",
           "TESU", "TEST", "TESP", "TESOROS", "TESI"]
clasificaciones = ["DOLAR", "TITULO DE PARTICIPACION RENTA VARIABLE", "TITULO DE PARTICIPACION",
                   "TIDIS", "TITULOS HIPOTECARIOS", "TES UVR", "TES TRM", "TES PESOS", "BONOS DEL TESORO EEUU", "TES IPC"]
pagoCuota = ["y", "n"]

# Model


class TituloBancarioModel(BaseModel):
    Titulo: str = Field(
        ...,
        min_length=3,
        max_length=7,
        description="Tipo de titulo bancario",
        example="TESOROS"
    )
    Clasificacion: str = Field(
        ...,
        min_length=3,
        max_length=38,
        description="Clasificacion del titulo bancario",
        example="TITULO DE PARTICIPACIÓN RENTA VARIABLE"
    )
    Valor: int = Field(
        ...,
        gt=0,
        description="Valor del titulo bancario",
        example="360000000"
    )
    FechaCreacion: date = date.today()
    FechaVencimiento: date = Field(
        ...,
        description="Fecha de vencimiento del titulo bancario",
        example="2023-08-18"
    )
    PagoCuota = "n"


@router.get("/titulosbancarios")
async def titulos_bancarios():
    logger.info('#START get titulos bancarios')
    try:
        e = TituloBancario()
        titulos = e.get_titulos_bancarios()
        logger.info('#EXIT get titulos bancarios')
        return titulos
    except Exception as e:
        return build_error_response(e)


@router.get("/titulosbancarios/{ID}")
async def titulo_bancario(ID: int):
    logger.info('#START get titulo bancario')
    try:
        e = TituloBancario()
        titulo = e.get_titulo_bancario(ID)
        if len(titulo) == 0:
            logger.info('#EXIT get titulo bancario en especifico')
            return {"Message": "No existe el titulo bancario"}
        logger.info('#EXIT get titulo bancario en especifico')
        return titulo
    except Exception as e:
        return build_error_response(e)


@router.patch("/titulosbancarios/paga/{ID}")
async def paga_titulo_bancario(ID: int):
    logger.info('#START patch pago titulo bancario')
    try:
        e = TituloBancario()
        titulo = e.get_titulo_bancario(ID)
        if len(titulo) == 0:
            return {"Message": "No existe el titulo bancario"}
        for item in titulo:
            for dict in item.items():
                if dict[-1] == 'y':
                    return {"Message": "El titulo bancario ya se encuentra pagado"}
        pagaTitulo = e.patch_paga_titulo_bancario(ID)
        logger.info('#EXIT patch titulo bancario en especifico')
        return pagaTitulo
    except Exception as e:
        return build_error_response(e)


@router.post("/titulosbancarios/nuevo")
async def nuevo_titulo_bancario(post: TituloBancarioModel):
    logger.info('#START post titulos bancarios')
    try:
        e = TituloBancario()
        newTitulo = post.dict()
        arrTitulo = []
        Titulo = e.formatoTitulo(newTitulo.get('Titulo'))
        arrTitulo.append(Titulo)
        Clasificacion = e.formatoTitulo(newTitulo.get('Clasificacion'))
        arrTitulo.append(Clasificacion)
        Valor = str(newTitulo.get('Valor'))
        arrTitulo.append(Valor)
        FechaCreacion = str(newTitulo.get('FechaCreacion'))
        arrTitulo.append(FechaCreacion)
        FechaVencimiento = str(newTitulo.get('FechaVencimiento'))
        arrTitulo.append(FechaVencimiento)
        PagoCuota = newTitulo.get('PagoCuota')
        arrTitulo.append(PagoCuota)
        valuesTitulo = [str(x) for x in arrTitulo]
        if e.validaTitulo(valuesTitulo, titulos) and e.validaTitulo(valuesTitulo, clasificaciones) and e.validaTitulo(valuesTitulo, pagoCuota):
            titulo = e.post_titulo_bancario(
                Titulo, Clasificacion, Valor, FechaCreacion, FechaVencimiento, PagoCuota)
            logger.info('#EXIT post nuevo titulo bancario')
            return titulo
        logger.info('#EXIT post error titulo bancario')
        return {"Message": "El titulo o la clasificación no es válida."}
    except Exception as e:
        return build_error_response(e)


@router.delete("/titulosbancarios/eliminar/{ID}")
async def paga_titulo_bancario(ID: int):
    logger.info('#START delete pago titulo bancario')
    try:
        e = TituloBancario()
        titulo = e.get_titulo_bancario(ID)
        if len(titulo) == 0:
            logger.info('#EXIT delete titulo bancario en especifico')
            return {"Message": "No existe el titulo bancario"}
        logger.info('#EXIT delete titulo bancario en especifico')
        eliminaTitulo = e.delete_titulo_bancario(ID)
        return eliminaTitulo
    except Exception as e:
        return build_error_response(e)


@router.patch("/titulosbancarios/editafechacreacion/{FechaCreacion}/{NuevaFecha}")
async def edita_fecha_creacion_titulo_bancario(FechaCreacion: date, NuevaFecha: date):
    logger.info('#START patch fecha creacion titulos bancarios')
    try:
        e = TituloBancario()
        titulo = e.patch_nueva_fecha_titulo_bancario(FechaCreacion, NuevaFecha)
        logger.info('#EXIT patch fecha creacion titulos bancarios')
        return titulo
    except Exception as e:
        return build_error_response(e)

TRUNCATE TABLE tblTitulosBancarios

INSERT INTO tblTitulosBancarios(Titulo, Clasificacion, Valor, FechaCreacion, FechaVencimiento, PagoCuota)
VALUES ('USD','DOLAR',500000000,'2022-03-14','2023-03-15','y')

INSERT INTO tblTitulosBancarios(Titulo, Clasificacion, Valor, FechaCreacion, FechaVencimiento, PagoCuota)
VALUES ('TRPV','TITULO DE PARTICIPACION RENTA VARIABLE',256000000,'2022-08-25','2023-08-26','y')

INSERT INTO tblTitulosBancarios(Titulo, Clasificacion, Valor, FechaCreacion, FechaVencimiento, PagoCuota)
VALUES ('TP','TITULO DE PARTICIPACION',360000000,'2022-02-16','2023-02-17','y')


select * from tblTitulosBancarios
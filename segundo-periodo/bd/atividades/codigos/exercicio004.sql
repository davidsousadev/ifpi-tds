/*
DROP table demo;
DROP table notasFiscais;
*/

CREATE TABLE notasFiscais(
  id int,
  id_nf int,
  id_item int,
  cod_prod int,
  valor_unidade numeric(6, 2),
  quantidade int,
  desconto numeric(6, 2) NULL,
  PRIMARY KEY (id)
);

INSERT INTO notasFiscais (id, id_nf, id_item, cod_prod, valor_unidade, quantidade, desconto) VALUES
(1,1,1,1,25.00,10,5),
(2,1,2,2,13.50,3,NULL),
(3,1,3,3,15.00,2,NULL),
(4,1,4,4,10.00,1,NULL),
(5,1,5,5,30.00,1,NULL),
(6,2,1,3,15.00,4,NULL),
(7,2,2,4,10.00,5,NULL),
(8,2,3,5,30.00,7,NULL),
(9,3,1,1,25.00,5,NULL),
(10,3,2,4,10.00,4,NULL),
(11,3,3,5,30.00,5,NULL),
(12,3,4,2,13.50,7,NULL),
(13,4,1,5,30.00,10,15),
(14,4,2,4,10.00,12,5),
(15,4,3,1,25.00,13,5),
(16,4,4,2,13.50,15,5),
(17,5,1,3,15.00,3,NULL),
(18,5,2,5,30.00,6,NULL),
(19,6,1,1,25.00,22,15),
(20,6,2,3,15.00,25,10),
(21,7,1,1,25.00,10,3),
(22,7,2,2,13.50,10,4),
(23,7,3,3,15.00,10,4),
(24,7,4,5,30.00,10,1);

SELECT * from notasFiscais;

/*a) Pesquise os itens que foram vendidos sem desconto. As colunas presentes no resultado da consulta
são: ID_NF, ID_ITEM, COD_PROD E VALOR_UNIT. */
SELECT id_nf, id_item, cod_prod, valor_unidade FROM notasFiscais WHERE desconto IS NULL;

/*b) Pesquise os itens que foram vendidos com desconto. As colunas presentes no resultado da consulta
são: ID_NF, ID_ITEM, COD_PROD, VALOR_UNIT E O VALOR VENDIDO. OBS: O valor vendido é igual ao
VALOR_UNIT - (VALOR_UNIT*(DESCONTO/100)). */
SELECT id_nf, id_item, cod_prod, valor_unidade, valor_unidade - (valor_unidade *(desconto / 100.00)) AS "Valor Vendido" FROM notasFiscais WHERE desconto is not NULL;

/*c) Altere o valor do desconto (para zero) de todos os registros onde este campo é nulo. */
UPDATE notasFiscais SET desconto = 0 WHERE desconto IS NULL;

/*d) Pesquise os itens que foram vendidos. As colunas presentes no resultado da consulta são: ID_NF,
ID_ITEM, COD_PROD, VALOR_UNIT, VALOR_TOTAL, DESCONTO, VALOR_VENDIDO. OBS: O
VALOR_TOTAL é obtido pela fórmula: QUANTIDADE * VALOR_UNIT. O VALOR_VENDIDO é igual a
VALOR_UNIT - (VALOR_UNIT*(DESCONTO/100)). */
SELECT id_nf, id_item, cod_prod, valor_unidade, quantidade * valor_unidade AS valor_total, desconto, valor_unidade - (valor_unidade * (desconto / 100.00)) AS valor_vendido FROM notasFiscais;



-- Deletar a tabela demo
DROP table demo;

-- Criação da Tabela
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

-- Inserção dos dados
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

-- Consultas solicitadas
-- a) Itens vendidos sem desconto
SELECT id_nf, id_item, cod_prod, valor_unidade
FROM notasFiscais
WHERE desconto IS NULL;

-- b) Itens vendidos com desconto
SELECT id_nf, id_item, cod_prod, valor_unidade, valor_unidade - (valor_unidade * (desconto / 100.00)) AS "Valor Vendido" 
FROM notasFiscais 
WHERE desconto IS NOT NULL;

-- c) Alterar valor do desconto para zero onde este campo é nulo
UPDATE notasFiscais 
SET desconto = 0 
WHERE desconto IS NULL;

-- d) Itens vendidos com valor total e valor vendido calculados
SELECT id_nf, id_item, cod_prod, valor_unidade, quantidade * valor_unidade AS valor_total, desconto, valor_unidade - (valor_unidade * (desconto / 100.00)) AS valor_vendido 
FROM notasFiscais;

-- e) Valor total das NF, ordenado do maior para o menor
SELECT id_nf, SUM(quantidade * valor_unidade) AS valor_total
FROM notasFiscais
GROUP BY id_nf
ORDER BY valor_total DESC;

-- f) Valor vendido das NF, ordenado do maior para o menor
SELECT id_nf, SUM(quantidade * (valor_unidade - (valor_unidade * (desconto / 100)))) AS valor_vendido
FROM notasFiscais
GROUP BY id_nf
ORDER BY valor_vendido DESC;

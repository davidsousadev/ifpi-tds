/*08-07-2024*/

-- DROP table demo;
-- DROP table cliente;

CREATE table cliente(
  codC int not NULL PRIMARY key,
  nome varchar(50),
  cpf char(11) not NULL,
  data_nasc date,
  sexo char(1),
  salario numeric(9,2)
);

insert into cliente(codc, nome, cpf, data_nasc, sexo, salario) VALUES
(1, 'Ana Moura', 12345678901, 2020-10-10, 'f', 1500.00),
(2, 'Aline Maria', 12345748901, 2020-10-10, 'f', 1300.00),
(3, 'Andrey Mat', 12347538901, 2020-10-10, 'm', 1200.00),
(4, 'Bernardo Borges', 12315978901, 2020-10-10, 'm', 1700.00),
(5, 'Claudio Clemente', 11045678901, 2020-10-10, 'm', 1900.00),
(6, 'David Demetrius', 1220678901, 2020-10-10, 'm', 15000.00);

-- Selects
-- A) Selecionar todos os registros do cliente em ordem decrescente
SELECT * from cliente order by nome DESC;

-- B) Selecionar todos os registros cujo nome começe com a letra A
SELECT * from cliente WHERE nome LIKE '%A';-- a ou A ou %a ou A%

-- C) Selecionar nomes cujos salários > 1000.00
SELECT nome from cliente WHERE salario >= 1000;

-- D) Seleecionar clientes do sexo feminino
SELECT nome from cliente WHERE sexo = 'f';

-- E) Selecionar salarios abaixo de 2000.00
select nome, salario from cliente WHERE salario < 2000;

-- UPDATE
UPDATE cliente set salario = 77777.77 WHERE codc = 6;

-- DELETE 
DELETE from cliente where salario < 1500;

SELECT * from cliente;
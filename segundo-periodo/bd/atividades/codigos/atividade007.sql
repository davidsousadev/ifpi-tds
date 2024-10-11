-- DROP table demo;
DROP table tb_aluno;
DROP table tb_curso;
DROP table tb_matricula;

-- Criação do banco de dados bdescola
-- CREATE DATABASE bdescola;

-- Cricação das Tabelas

-- Tabela Aluno
CREATE TABLE tb_aluno(
cod_aluno integer(3),
nome_aluno varchar(60) not NULL,
ano_nascimento year,
e_mail varchar(60),
sexo varchar(1) not NULL,
PRIMARY key (cod_aluno)
);

-- Tabela Curso
CREATE table tb_curso(
codigo_curso integer(3),
nome_curso varchar(60) NOT NULL,
PRIMARY KEY (codigo_curso)
);

-- Tabela Matricula
CREATE table tb_matricula(
codigo_curso integer(3),
codigo_aluno integer(3),
PRIMARY KEY (codigo_curso, codigo_aluno),
FOREIGN KEY (codigo_curso) REFERENCES tb_curso(codigo_curso),
FOREIGN KEY (codigo_aluno) REFERENCES tb_aluno(codigo_aluno)
);

-- Inserção de Dados
-- Inserção de dados Tabela Aluno
insert into tb_aluno values
  (1, 'Josiel Jardim', 1974, 'josiel@provaSQL.com.br', 'M'),
  (2, 'Ana Maria', 1980, 'ana@provaSQL.com.br', 'F'),
  (3, 'João Pedro', 1979, 'joao@provaSQL.com.br', 'M');

-- Inserção de dados na Tabela Curso
INSERT into tb_curso VALUES
(1, 'Medicina'),
(2, 'Arquitetura'),
(3, 'Filosofia'),
(4, 'Informática'),
(5, 'Jornalismo');

-- Inserção de dados na Tabela Matricula
INSERT into tb_matricula VALUES
(4,1),
(1,2), 
(3,3);

-- 1) Faça um comando SQL para matricular o aluno “Pedro César” no curso de Informática. Os dados devem ser inseridos na tabela TB_MATRÍCULA.
insert into tb_aluno values
  (4, 'Pedro César', 1996, 'pedrocesar@provaSQL.com.br', 'M');

INSERT into tb_matricula VALUES
(4,4);

-- Seleções
-- 2) Escreva um comando SQL que retorne os nomes dos alunos e do(s) cursos em que estão matriculados. Os dados deverão estar ordenados pelo nome do curso.
SELECT aluno.nome_aluno AS "Aluno" , curso.nome_curso AS "Curso" FROM 
tb_matricula matricula JOIN 
tb_aluno aluno ON matricula.codigo_aluno = aluno.cod_aluno JOIN 
tb_curso curso ON matricula.codigo_curso = curso.codigo_curso
ORDER BY curso.nome_curso;

-- 3) Crie um comando SQL que retorne o e-mail de todos os alunos maiores de idade.
SELECT e_mail  AS "E-mail +18" FROM tb_aluno
WHERE ((2024 - ano_nascimento) >= 18);


-- Seleções
-- select * from tb_aluno;
-- SELECT * from tb_curso;
-- SELECT * FROM tb_matricula;
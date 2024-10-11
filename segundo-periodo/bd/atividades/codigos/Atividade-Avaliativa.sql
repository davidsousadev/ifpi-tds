/*

DROP TABLE categorias;
DROP TABLE perguntas;
DROP TABLE questionario;
DROP TABLE relatorios;
DROP TABLE usuarios;

*/

CREATE TABLE categorias (
    id_categoria INT AUTO_INCREMENT NOT NULL,
    nome VARCHAR(100),
    PRIMARY KEY(id_categoria)
);

CREATE TABLE perguntas (
    id_pergunta INT AUTO_INCREMENT NOT NULL,
    enunciado TEXT,
    alternativa_a TEXT,
    alternativa_b TEXT,
    alternativa_c TEXT,
    alternativa_d TEXT,
    alternativa_e TEXT,
    alternativa_correta CHAR(1),
    nivel INT,
    categoria_id INT,
    estado VARCHAR(50),
    PRIMARY KEY(id_pergunta),
    FOREIGN KEY (categoria_id) REFERENCES categorias(id_categoria)
);

CREATE TABLE usuarios (
    id_usuario INT AUTO_INCREMENT NOT NULL,
    nome VARCHAR(100),
    usuario VARCHAR(50) UNIQUE,
    CPF CHAR(11) UNIQUE,
    data_de_nascimento DATE,
    email VARCHAR(100) UNIQUE,
    PRIMARY KEY (id_usuario)
);

CREATE TABLE questionario (
    id_questionario INT AUTO_INCREMENT NOT NULL,
    id_usuario INT NOT NULL,
    nivel INT,
    quantidade_de_perguntas INT,
    PRIMARY KEY(id_questionario),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);


CREATE TABLE relatorios (
    id_relatorio INT AUTO_INCREMENT NOT NULL,
    id_questionario INT NOT NULL,
    id_usuario INT not NULL,
    id_pergunta INT not NULL,
    acertos INT,
    erros INT,
    PRIMARY KEY(id_relatorio),
    FOREIGN KEY (id_questionario) REFERENCES questionario(id_questionario),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (id_pergunta) REFERENCES perguntas(id_pergunta)
);

INSERT INTO categorias (id_categoria, nome) VALUES
(1, 'Matemática'),
(2, 'Ciências'),
(3, 'História'),
(4, 'Geografia');

INSERT INTO perguntas (id_pergunta, enunciado, alternativa_a, alternativa_b, alternativa_c, alternativa_d, alternativa_e, alternativa_correta, nivel, categoria_id, estado) VALUES
(1, 'Qual é o resultado de 2 + 2?', '3', '4', '5', '6', '7', 'b', 1, 1, 'Ativa'),
(2, 'Qual é a capital do Brasil?', 'São Paulo', 'Rio de Janeiro', 'Brasília', 'Salvador', 'Belo Horizonte', 'c', 1, 4, 'Ativa'),
(3, 'Quem foi o primeiro presidente dos Estados Unidos?', 'Abraham Lincoln', 'George Washington', 'Thomas Jefferson', 'John Adams', 'James Madison', 'b', 2, 3, 'Ativa');

INSERT INTO usuarios (id_usuario, nome, usuario, CPF, data_de_nascimento, email) VALUES
(1, 'João Silva', 'joaosilva', '12345678901', '1990-05-15', 'joao@email.com'),
(2, 'Maria Santos', 'mariasantos', '98765432109', '1985-10-20', 'maria@email.com');

INSERT INTO questionario (id_questionario, id_usuario, nivel, quantidade_de_perguntas) VALUES
(1, 1, 1, 3),
(2, 2, 2, 1);

INSERT INTO relatorios (id_relatorio, id_questionario, id_usuario, id_pergunta, acertos, erros) VALUES
(1, 1, 1, 1, 1, 0),
(2, 1, 1, 2, 0, 1),
(3, 2, 2, 3, 1, 0);

SELECT * FROM categorias;
SELECT * FROM perguntas;
SELECT * FROM usuarios;
SELECT * FROM questionario;
SELECT * FROM relatorios;

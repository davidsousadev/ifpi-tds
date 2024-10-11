create table pais(
  cod_pais int,
  nome varchar(20),
  populacao int,
  PRIMARY KEY (cod_pais)
);

CREATE table equipe(
  cod_equipe int,
  nome varchar(20),
  cod_pais int,
  PRIMARY key (cod_equipe),
  FOREIGN key (cod_pais) REFERENCES pais
);

CREATE TABLE piloto(
  cod_piloto int,
  nome varchar(20),
  cod_nascimento datetime,
  cod_equipe int,
  cod_pais int,
  PRIMARY key (cod_piloto),
  FOREIGN key (cod_equipe) REFERENCES equipe,
  FOREIGN key (cod_pais) REFERENCES pais
);

create table circuito (
	cod_circuito int,
  	nome varchar(20),
  	extensao int,
  	cod_pais int,
  	PRIMARY key (cod_circuito),
  	FOREIGN key (cod_pais) REFERENCES pais
);

create table prova(
  cod_prova int,
  data datetime,
  situacao varchar(20),
  cod_circuito int,
  PRIMARY key (cod_prova),
  FOREIGN key (cod_circuito) REFERENCES circuito
);

create table resultado(
  cod_prova int,
  cod_piloto int,
  tempo_prova int,
  colocacao_final int,
  posicao_grid int,
  melhor_volta int,
  FOREIGN key (cod_prova) REFERENCES prova,
  FOREIGN key (cod_piloto) REFERENCES piloto,
  PRIMARY KEY (cod_prova, cod_piloto)
);

INSERT into pais (cod_pais, nome, populacao) VALUES
(1,'Argentina',44500000),
(2,'Bolívia',11350000),
(3,'Brasil',210000000),
(4,'Chile',18730000),
(5,'Colômbia',49650000),
(6,'Equador',17080000),
(7,'Guiana',779000),
(8,'Paraguai',6956000),
(9,'Peru',31990000),
(10,'Suriname',575991),
(11,'Uruguai',3449000),
(12,'Venezuela',28870000);




SELECT * from pais;

/*
DROP table pais;
DROP table equipe;
DROP table piloto;
DROP table circuito;
DROP table prova;
DROP table resultado;
DROP table demo;
*/

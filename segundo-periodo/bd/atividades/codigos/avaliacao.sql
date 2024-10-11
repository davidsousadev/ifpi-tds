create table Funcionarios(
	Id int not NULL PRIMARY key,
	Nome varchar (50),
	Rua varchar (50),
	Numero varchar (10),	
	CEP char(8) not NULL,
	Bairro varchar (50),
	Cidade varchar (50),
	Estado varchar (50));
    
insert into Funcionarios (Id, Nome, Rua, Numero, CEP, Bairro, Cidade, Estado) values
    (1, 'Alana', 'Av. Nossa Senhora de Fátima', '980', 64044780, 'Fátima', 'Teresina','PI'),
    (2, 'Carlos', 'Rua Palmeias Novas', '750', 88078923, 'Leblon', 'Rio de Janeiro','RJ'),
    (3, 'Robson', 'Rua Antônio Nunes', '305', 64045963, 'São João', 'Teresina','PI'),
    (4, 'Alice', 'Av. 13 de Maio', '888', 60048917, 'Fátima', 'Fortaleza','CE');
    

select * from Funcionarios where Bairro='Fátima' order by Nome desc;

select * from Funcionarios where Nome Like 'A%';

select Nome, Cidade from Funcionarios where Cidade = 'Teresina';





-- drop table Funcionarios
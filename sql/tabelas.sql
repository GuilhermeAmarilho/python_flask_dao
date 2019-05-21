ALTER TABLE funcionario DROP coddepartamento;
DROP TABLE departamento;
DROP TABLE funcionario;
CREATE TABLE funcionario(
    codigo serial,
    nome varchar(100) NOT NULL,
    coddepartamento int,
    CONSTRAINT funcionarioPK PRIMARY KEY (codigo)
);
CREATE TABLE departamento(
    codigo serial,
    nome varchar(100) NOT NULL,
    codgerente int,
    CONSTRAINT departamentoPK PRIMARY KEY (codigo),
    CONSTRAINT departamentoFK FOREIGN KEY (codgerente)
	REFERENCES funcionario (codigo)
		ON UPDATE CASCADE
		ON DELETE SET NULL
);
ALTER TABLE  funcionario ADD CONSTRAINT funcionarioFK FOREIGN KEY  (coddepartamento) REFERENCES departamento (codigo)
		ON UPDATE CASCADE
		ON DELETE SET NULL;
INSERT INTO departamento ("nome") VALUES ('The grandious Amarilho'),('Amarilho company'),('Alan office'),('Mauricio company'),('loja da Thamyris'),('Lancheria do adrian'),('ABC informatica'),('tudo sobre info');
INSERT INTO "funcionario" ("nome", "coddepartamento") VALUES ('Guilherme', 1),('Alan', 2),('Adrian', 3),('Bernardo', 4),('Brenda', 5),('Cristian', 6),('Carolina', 7),('Davi', 8),('Douglas', 1),('Emanuel', 2),('Fabricio', 3),('GUGU', 4),('Helena', 5),('Isadora', 6),('Isaias', 7),('Joao P', 8),('Joao G', 1),('Ketelin', 2),('Katrina', 3),('Kerolyn', 4),('Leonardo', 5),('Lucas', 6),('Livia', 7),('Lorrana', 8),('Mauricio', 1),('Matheus', 2),('Mathias', 3),('Mouses', 4),('Nicoli', 5),('Nina', 6),('Otavio', 7),('Patrick', 8),('Patricia', 1),('Perola', 2),('Raissa', 3),('rayne', 4),('Silvio', 5);
INSERT INTO "funcionario" ("nome") VALUES ('Abgail'),('George');
UPDATE "departamento" SET codgerente = 1 WHERE codigo = 1;
UPDATE "departamento" SET codgerente = 5 WHERE codigo = 2;
UPDATE "departamento" SET codgerente = 4 WHERE codigo = 3;
UPDATE "departamento" SET codgerente = 3 WHERE codigo = 4;
UPDATE "departamento" SET codgerente = 8 WHERE codigo = 5;
UPDATE "departamento" SET codgerente = 7 WHERE codigo = 6;
UPDATE "departamento" SET codgerente = 6 WHERE codigo = 7;
UPDATE "departamento" SET codgerente = 2 WHERE codigo = 8;
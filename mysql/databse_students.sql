use db;

CREATE TABLE students(
    estudanteID int not null AUTO_INCREMENT,
    nome varchar(100) NOT NULL,
    sobre_nome varchar(100) NOT NULL,
    PRIMARY KEY (estudanteID)
);

INSERT INTO students(nome, sobre_nome)
VALUES("João", "Marcos"), ("Naruto", "Uzumaki");  
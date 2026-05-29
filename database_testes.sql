CREATE DATABASE IF NOT EXISTS testes;
USE testes;

CREATE TABLE IF NOT EXISTS Eleitores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Nome_Completo VARCHAR(150) NOT NULL,
    CPF VARCHAR(20) NOT NULL UNIQUE,
    Titulo_de_eleitor VARCHAR(12) NOT NULL UNIQUE,
    Chave_de_acesso VARCHAR(20) NOT NULL,
    Mesario CHAR(1) NOT NULL DEFAULT 'N',
    Ja_votou BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS candidatos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    numero INT NOT NULL UNIQUE,
    partido VARCHAR(80) NOT NULL
);

CREATE TABLE IF NOT EXISTS votos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    protocolo VARCHAR(36) NOT NULL UNIQUE,
    numero_candidato INT,
    data_hora DATETIME NOT NULL,
    FOREIGN KEY (numero_candidato) REFERENCES candidatos(numero)
);

CREATE TABLE IF NOT EXISTS status_votacao (
    id INT PRIMARY KEY,
    aberta BOOLEAN NOT NULL DEFAULT FALSE
);

INSERT INTO status_votacao (id, aberta)
VALUES (1, FALSE)
ON DUPLICATE KEY UPDATE id = id;



DROP TABLE Eleitores;
DROP TABLE candidatos;
DROP TABLE votos;
DROP TABLE status_votacao;

SELECT * FROM Eleitores;
SELECT * FROM candidatos;
SELECT * FROM votos;
SELECT * FROM status_votacao;

SHOW TABLES;

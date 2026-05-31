-- Cria e seleciona o banco usado nos testes do sistema de votacao.
CREATE DATABASE IF NOT EXISTS testes;
USE testes;

-- Guarda os eleitores, incluindo dados de acesso, perfil de mesario e controle de voto.
CREATE TABLE IF NOT EXISTS Eleitores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Nome_Completo VARCHAR(150) NOT NULL,
    CPF VARCHAR(20) NOT NULL UNIQUE,
    Titulo_de_eleitor VARCHAR(12) NOT NULL UNIQUE,
    Chave_de_acesso VARCHAR(20) NOT NULL,
    Mesario CHAR(1) NOT NULL DEFAULT 'N',
    Ja_votou BOOLEAN NOT NULL DEFAULT FALSE
);

-- Guarda os candidatos disponiveis para votacao.
CREATE TABLE IF NOT EXISTS candidatos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    numero INT NOT NULL UNIQUE,
    partido VARCHAR(80) NOT NULL
);

-- Registra cada voto com protocolo, candidato escolhido e data/hora.
CREATE TABLE IF NOT EXISTS votos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    protocolo VARCHAR(36) NOT NULL UNIQUE,
    numero_candidato INT,
    data_hora DATETIME NOT NULL,
    FOREIGN KEY (numero_candidato) REFERENCES candidatos(numero)
);

-- Controla se a votacao esta aberta ou fechada.
CREATE TABLE IF NOT EXISTS status_votacao (
    id INT PRIMARY KEY,
    aberta BOOLEAN NOT NULL DEFAULT FALSE
);

-- Garante o registro inicial usado para abrir e fechar a votacao.
INSERT INTO status_votacao (id, aberta)
VALUES (1, FALSE)
ON DUPLICATE KEY UPDATE id = id;



-- Comandos manuais de limpeza usados durante testes.
DROP TABLE Eleitores;
DROP TABLE candidatos;
DROP TABLE votos;
DROP TABLE status_votacao;

-- Consultas manuais para conferir os dados salvos nas tabelas.
SELECT * FROM Eleitores;
SELECT * FROM candidatos;
SELECT * FROM votos;
SELECT * FROM status_votacao;

-- Mostra as tabelas existentes no banco selecionado.
SHOW TABLES;

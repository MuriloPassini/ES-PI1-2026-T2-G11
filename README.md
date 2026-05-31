# LAD.Py - Sistema de Votação Digital

## Descrição do Projeto
O LAD.Py é um sistema de votação digital desenvolvido com finalidade didática para o Projeto Integrador I do curso de Engenharia de Software da PUC Campinas.

O sistema tem como objetivo simular um processo eleitoral completo, garantindo organização, segurança e confiabilidade dos dados. Ele foi desenvolvido para ser executado via terminal (linha de comando), com foco em lógica de programação, manipulação de banco de dados e aplicação de conceitos matemáticos, como criptografia.

O projeto é dividido em dois módulos principais:
- **Gerenciamento**: responsável pelo cadastro e controle de eleitores e candidatos.
- **Votação**: responsável pela execução do processo eleitoral, registro de votos e geração de resultados.

Além disso, o sistema implementa:
- Validação de dados (CPF e título de eleitor)
- Criptografia de informações sensíveis
- Registro de logs
- Auditoria e verificação de integridade dos dados

> Este projeto possui finalidade exclusivamente acadêmica e não representa sistemas reais de votação.

---

## Integrantes
- Murilo Passini
- Pietro Eduardo
- Cauã Zanluchi
- Filipe Pierri
- Bernardo Garcia
- Gabriel André

---

## Tecnologias Utilizadas
- Python 3.14
- MySQL
- Biblioteca `mysql.connector`
- Git e GitHub
- VSCode ou PyCharm

---

## Instruções para Execução

### 1. Instalar os requisitos
Antes de rodar o projeto, é necessário ter instalado:
- Python
- MySQL
- Git, caso queira clonar o repositório

Depois, instale a biblioteca de conexão com o MySQL:

```bash
pip install mysql-connector-python
```

### 2. Configurar o banco de dados
Abra o MySQL e execute o arquivo `database_testes.sql` para criar o banco `testes` e as tabelas do sistema.

Atenção: o arquivo também possui comandos de teste como `DROP TABLE` e `SELECT` no final. Para preparar o banco normalmente, execute apenas a parte de criação:

```sql
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
```

Não execute os comandos `DROP TABLE` se quiser manter as tabelas criadas.

### 3. Conferir a conexão com o banco
O arquivo `.Vote/banco.py` usa estas configurações por padrão:

```python
host = "localhost"
user = "root"
password = "198765432AbGF"
database = "testes"
```

Se o seu MySQL usar outro usuário ou senha, ajuste pelas variáveis de ambiente antes de rodar:

```powershell
$env:VOTE_DB_HOST="localhost"
$env:VOTE_DB_USER="root"
$env:VOTE_DB_PASSWORD="sua_senha"
$env:VOTE_DB_NAME="testes"
```

### 4. Rodar o sistema
Na pasta principal do projeto, execute:

```bash
python .Vote/menu_principal.py
```

O sistema será aberto no terminal com o menu principal.

### 5. Fluxo básico de uso
Uma ordem simples para testar o sistema é:

1. Entrar em **Gerenciamento**.
2. Cadastrar eleitores.
3. Cadastrar pelo menos um eleitor como mesário.
4. Cadastrar candidatos.
5. Entrar em **Votação**.
6. Abrir a votação usando os dados do mesário.
7. Realizar votos com os eleitores cadastrados.
8. Fechar a votação usando o mesário.
9. Consultar resultados e auditoria.

Durante o cadastro do eleitor, o sistema mostra uma chave de acesso. Guarde essa chave, pois ela será usada para votar ou para autenticar o mesário.

### 6. Logs e protocolos
Os registros de auditoria são salvos automaticamente na pasta `.Vote`:

- `logs_ocorrencias.txt`
- `protocolos.txt`

Esses arquivos podem ser consultados pelo menu de auditoria dentro do sistema.

# Relatorio de Manutencao do Sistema de Votacao

Data da revisao: 18/05/2026

## 1. Objetivo

Este relatorio descreve a manutencao realizada nos arquivos da pasta `.Vote`, com foco em:

- Conectar as funcoes ja existentes ao menu principal.
- Evitar execucoes automaticas indevidas ao importar modulos.
- Corrigir erros de integracao entre menus, banco e funcoes.

## 2. Escopo

As funcoes mantidas e conectadas foram:

- Cadastro de eleitor.
- Edicao de eleitor.
- Cadastro, listagem, busca e exclusao de candidatos.
- Abertura da votacao por mesario.
- Votacao do eleitor.
- Auditoria simples em memoria, com logs e protocolos.

Nao foram adicionadas funcionalidades novas fora do que ja existia nos arquivos.

## 3. Principais problemas encontrados antes da manutencao

- Alguns arquivos executavam menus ou funcoes automaticamente ao serem importados.
- `Management.py` chamava `iniciar_management()` no final do arquivo, abrindo o menu administrativo antes da escolha no hub.
- `cadastro_candidato.py` tinha um menu executando no topo do arquivo, entao importar o modulo ja entrava no sistema de candidatos.
- `LOGS_VOTACAO.py` tambem rodava um loop de menu direto no import.
- `Abertura_votacao.py` chamava `abrir_votacao()` automaticamente e ainda tinha uma segunda funcao de conexao duplicada.
- `voting_sys.py` usava `cursor` e `connect` sem cria-los nem importa-los corretamente.
- Os nomes de tabelas e colunas estavam inconsistentes entre os modulos.
- `validacoes.py` tinha `validacaocpf()` sem parametro, mas o cadastro chamava a funcao passando um CPF.
- `cadastro_candidato.py` tinha erro de fluxo: a opcao de deletar repetia a mesma condicao da opcao de buscar.
- O arquivo de cadastro de eleitor estava registrado no Git como `CADASTRO_ELEITOR.PY`, mas os imports usavam `cadastro_eleitor.py`.

## 4. Mudancas por arquivo

### `.Vote/banco.py`

- Mudei toda a conexao com MySQL em `conectar_bd()`.
- Adicionei `fechar_bd(conexao, cursor)` para padronizar fechamento de conexoes.
- Adicionei suporte a variaveis de mudança de credenciais (powershell):
  - `VOTE_DB_HOST`
  - `VOTE_DB_USER`
  - `VOTE_DB_PASSWORD`
  - `VOTE_DB_NAME`
- Os valores padrao continuam sendo `localhost`, `root`, `198765432AbGF` e `testes`.

### `.Vote/menu_principal.py`

- O menu principal passou a chamar:
  - `iniciar_management()`
  - `votacao()`
  - `menu_auditoria()`
- Foi adicionado o bloco:

```python
if __name__ == "__main__":
    iniciar_hub()
```

Assim, o hub so abre automaticamente quando o arquivo e executado diretamente.

### `.Vote/Management.py`

- Removi a chamada automatica de `iniciar_management()` no import.
- Transformei o gerenciamento em um menu com retorno ao hub.
- Conectei as opcoes:
  - Cadastrar eleitor.
  - Editar eleitor.
  - Gerenciar candidatos.
  - Abrir votacao como mesario.

### `.Vote/cadastro_eleitor.py`

- Corrigi o uso de `conectar_bd()`, que retorna `conexao, cursor`.
- Corrigi chamada de `validacaocpf(cpf)`.
- Adicionei validacao para impedir nome vazio.
- Padronizei fechamento da conexao com `fechar_bd()`.
- Mantive o cadastro usando as colunas:
  - `Nome_Completo`
  - `CPF`
  - `Titulo_de_eleitor`
  - `Chave_de_acesso`
  - `Mesario`
- O arquivo tambem foi registrado no Git como `cadastro_eleitor.py`, pra ficar igual ao import usado pelo menu.

### `.Vote/editar_eleitor.py`

- Corrigi a conexao com o banco.
- Padronizei os nomes de colunas usados com o cadastro de eleitor.
- Removi conversoes para `int` em CPF e titulo, preservando zeros a esquerda caso existam.
- Adicionei fechamento padronizado de conexao.

### `.Vote/cadastro_candidato.py`

- Removi conexao global e cursor global.
- Removi menu automatico no import.
- Adicionei `menu_candidatos()`.
- Corrigi fluxo das opcoes:
  - `1` cadastra.
  - `2` lista.
  - `3` busca.
  - `4` deleta.
  - `5` sai.
- Corrigi SQL de exclusao.
- Corrigi exibicao de resultados de busca.
- Padronizei fechamento de conexao em cada operacao.

### `.Vote/Abertura_votacao.py`

- Removei conexao duplicada dentro do arquivo.
- Removei chamada automatica de `abrir_votacao()`.
- Passoamos a usar `conectar_bd()` e `fechar_bd()`.
- Mantive autenticacao do mesario.
- Mantive a zeresima, apagando votos e resetando `Ja_votou`.
- Lista candidatos cadastrados ao final.

### `.Vote/voting_sys.py`

- Juntei a votacao dentro da funcao `votacao()`.
- Removi dependencias inexistentes de `cursor` e `connect` globais.
- Padronizei busca do eleitor usando:
  - `Titulo_de_eleitor`
  - primeiros 4 digitos do `CPF`
  - `Chave_de_acesso`
- Corrigi busca de candidato usando `nome`, `numero`, `partido`.
- Gera protocolo com `uuid`.
- Registra voto na tabela `votos`.
- Marca o eleitor como `Ja_votou = TRUE`.

### `.Vote/LOGS_VOTACAO.py`

- Removi loop automatico no import.
- Adicionei `menu_auditoria()`.
- Mantive as funcoes ja existentes:
  - `registrar_log`
  - `exibir_logs`
  - `gerar_protocolo`
  - `exibir_protocolos`

### `.Vote/validacoes.py` e `.Vote/validarcpf.py`

- Corrigi `validacaocpf()` para receber CPF por parametro.
- Corrigi a transformacao de string para lista de digitos.
- Preservou a validacao de titulo ja existente.

### `.Vote/busca_eleitores.py` e `.Vote/OLDVOTING.py`

- Foram ajustados para nao ficarem incoerentes com o restante do projeto.
- Passaram a usar a mesma conexao centralizada e os mesmos nomes de colunas.

## 5. Validacoes realizadas

### Sintaxe

Comando executado:

```powershell
python -m compileall .Vote
```

Resultado: todos os arquivos compilaram sem erro de sintaxe.

### Imports

Foi testado importar os principais modulos sem disparar menus automaticamente.

Resultado: imports passaram. No teste real, os dois modulos com acento no nome tambem foram importados com `importlib`.

### Navegacao do menu

Foram testados fluxos simulados:

- Entrar no hub e sair.
- Entrar em gerenciamento, abrir menu de candidatos, sair do menu de candidatos, voltar ao gerenciamento e voltar ao hub.
- Entrar em auditoria e encerrar auditoria.

Resultado: menus navegaram sem erro.

### Validacao de CPF

Foi testado:

- CPF valido conhecido: retornou `True`.
- CPF repetido: retornou `False`.
- CPF curto: retornou `False`.

## 6. Validacao bloqueada

A conexao real com o MySQL nao pode ser validada neste momento.

Erro encontrado:

```text
Access denied for user 'root'@'localhost'
```

Isso significa que o MySQL respondeu, mas recusou usuario/senha.

Para testar os fluxos reais de banco, e necessario configurar as credenciais corretas:

```powershell
$env:VOTE_DB_HOST="localhost"
$env:VOTE_DB_USER="root"
$env:VOTE_DB_PASSWORD="sua_senha"
$env:VOTE_DB_NAME="testes"
python .Vote\menu_principal.py
```

## 7. Requisitos esperados do banco

Pelo codigo atual, o banco precisa conter as seguintes estruturas.

Tabela `Eleitores`:

- `Nome_Completo`
- `CPF`
- `Titulo_de_eleitor`
- `Chave_de_acesso`
- `Mesario`
- `Ja_votou`

Tabela `candidatos`:

- `nome`
- `numero`
- `partido`

Tabela `votos`:

- `protocolo`
- `titulo_eleitor`
- `numero_candidato`
- `data_hora`

Se os nomes reais no MySQL forem diferentes, os comandos SQL ainda podem falhar.

## 8. Riscos restantes

- A conexao com banco ainda depende das credenciais corretas.
- Os nomes das colunas precisam bater exatamente com o banco criado pelo grupo.
- O sistema ainda usa arquivos com acentos no nome, como `Abertura_votacao` e `LOGS_VOTACAO` com acentos reais no nome do arquivo. Isso funciona no Windows testado, mas pode ser fragil em outro ambiente.
- A auditoria atual fica apenas em memoria; ao fechar o programa, logs e protocolos somem. Isso ja era o comportamento implementado.
- A abertura da votacao executa zeresima, apagando votos existentes. Isso parece ser parte da funcao prevista, mas deve ser usado com cuidado.

## 9. Como executar

No PowerShell, dentro da pasta do projeto:

```powershell
python .Vote\menu_principal.py
```

Se precisar informar credenciais do banco:

```powershell
$env:VOTE_DB_PASSWORD="sua_senha"
python .Vote\menu_principal.py
```

## 10. Conclusao

A manutencao deixou os modulos principais conectados pelo menu e removeu os comportamentos que executavam funcoes fora de hora. A parte sem banco foi validada com sintaxe, imports e navegacao de menus. O unico bloqueio para validar o ciclo completo e a autenticacao do MySQL local.

# Automação de Testes API - ServeRest

## Sobre o projeto

Projeto de automação de testes de API utilizando Python, Pytest e Requests para validar os endpoints da API ServeRest.

Os testes contemplam cenários positivos e negativos, incluindo:

* Consulta de usuários
* Cadastro de usuários
* Validação de e-mail duplicado
* Validação de campos obrigatórios
* Busca de usuário por ID
* Atualização de usuário

## Tecnologias utilizadas

* Python 3.12+
* Pytest
* Requests

## Pré-requisitos

Ter instalado:

* Python 3.12 ou superior
* Pip
* Git (opcional)

Verificar versões:

```bash
python --version
pip --version
```

## Clonando o projeto

```bash
git clone <https://github.com/Renanpacheco/week3_air.git>
cd nome-do-projeto
```

## Criando ambiente virtual

### Linux / Ubuntu

```bash
python3 -m venv venv
```

### Windows

```powershell
python -m venv venv
```

## Ativando ambiente virtual

### Linux / Ubuntu

```bash
source venv/bin/activate
```

### Windows (Prompt de Comando - CMD)

```cmd
venv\Scripts\activate.bat
```

### Windows (PowerShell)

```powershell
.\venv\Scripts\Activate.ps1
```

Após a ativação, o terminal deverá exibir algo semelhante a:

```text
(venv)
```

## Instalando dependências

```bash
pip install -r requirements.txt
```

Caso o arquivo `requirements.txt` não exista:

```bash
pip install pytest requests
```

## Executando os testes

### Executar todos os testes

```bash
pytest
```

### Executar com detalhes

```bash
pytest -v
```

### Executar exibindo mensagens do print()

```bash
pytest -v -s
```

### Executar um único teste

```bash
pytest tests/test_api_serverest.py::test_create_user -v
```

### Executar uma classe de testes

```bash
pytest tests/test_api_serverest.py -v
```

## API utilizada

ServeRest

Documentação oficial:

https://compassuol.serverest.dev

## Boas práticas adotadas

* Validação de status codes
* Validação dos campos retornados pela API
* Uso de e-mails dinâmicos para evitar conflitos de cadastro
* Testes independentes
* Estrutura preparada para utilização de fixtures do Pytest
* Automação de cenários positivos e negativos

## Gerando o arquivo requirements.txt

Caso adicione novas dependências ao projeto:

```bash
pip freeze > requirements.txt
```

## Autor

Renan Pacheco

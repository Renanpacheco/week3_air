# PLANO DE TESTES

## 1. Objetivo da Suíte

Garantir a qualidade, confiabilidade e estabilidade da API ServeRest através da execução automatizada de testes funcionais e de validação de contratos.

A suíte tem como objetivos:

* Validar o comportamento esperado dos endpoints.
* Verificar códigos de status HTTP.
* Validar estruturas de resposta (JSON Schema).
* Garantir o correto funcionamento das regras de negócio.
* Identificar regressões após alterações na API.
* Validar autenticação e autorização dos recursos protegidos.

---

## 2. Estratégia de Testes

### Tipo de Teste

Serão executados principalmente:

* Testes Funcionais
* Testes de Integração de API
* Testes de Contrato (Schema Validation)
* Testes Negativos
* Testes de Autorização e Autenticação

### Camada Testada

Camada de API (REST).

Não fazem parte deste escopo:

* Testes de Interface (UI)
* Testes Mobile
* Testes de Performance
* Testes de Segurança avançados

### Ferramentas

* Python 3.x
* Pytest
* Requests
* Faker
* JsonSchema (opcional)
* Allure Reports (opcional)

### Estratégia de Dados

* Utilização de dados dinâmicos para evitar dependência entre testes.
* Criação de massa de teste durante a execução.
* Limpeza dos dados quando aplicável.
* Cada teste deve ser independente e executável isoladamente.

---

## 3. Escopo

### Coberto

#### Login

* Autenticação de usuários
* Geração de token

#### Usuários

* Cadastro
* Consulta
* Atualização
* Exclusão
* Validações de campos obrigatórios

#### Produtos

* Cadastro
* Consulta
* Atualização
* Exclusão
* Validação de permissões administrativas

#### Carrinhos

* Criação de carrinho
* Consulta de carrinhos
* Cancelamento de compra
* Conclusão de compra

### Fora do Escopo

* Testes de carga
* Testes de estresse
* Testes de acessibilidade
* Testes de front-end
* Testes de banco de dados
* Testes de segurança avançados (OWASP)

---

## 4. Cenários a Implementar

### POST /login

#### Cenários Positivos

* Realizar login com credenciais válidas.
* Validar retorno do token.

#### Cenários Negativos

* Login com email inexistente.
* Login com senha inválida.
* Login sem informar email.
* Login sem informar senha.

---

### POST /usuarios

#### Cenários Positivos

* Cadastrar usuário comum.
* Cadastrar usuário administrador.

#### Cenários Negativos

* Cadastrar usuário com email já existente.
* Cadastrar usuário sem nome.
* Cadastrar usuário sem email.
* Cadastrar usuário sem senha.
* Cadastrar usuário com valor inválido para administrador.

---

### GET /usuarios

#### Cenários Positivos

* Listar usuários.
* Buscar usuário por ID.
* Filtrar usuários por nome.
* Filtrar usuários por email.

#### Cenários Negativos

* Buscar usuário inexistente.

---

### PUT /usuarios/{id}

#### Cenários Positivos

* Atualizar nome do usuário.
* Atualizar email do usuário.

#### Cenários Negativos

* Atualizar usuário inexistente.
* Atualizar com email já utilizado.

---

### DELETE /usuarios/{id}

#### Cenários Positivos

* Excluir usuário existente.

#### Cenários Negativos

* Excluir usuário inexistente.
* Excluir usuário vinculado a regras que impeçam a remoção.

---

### POST /produtos

#### Cenários Positivos

* Cadastrar produto com token de administrador.

#### Cenários Negativos

* Cadastrar sem autenticação.
* Cadastrar com token inválido.
* Cadastrar produto com nome duplicado.
* Cadastrar produto sem nome.
* Cadastrar produto sem preço.
* Cadastrar produto sem quantidade.

---

### GET /produtos

#### Cenários Positivos

* Listar produtos.
* Buscar produto por ID.
* Filtrar produto por nome.

#### Cenários Negativos

* Buscar produto inexistente.

---

### PUT /produtos/{id}

#### Cenários Positivos

* Atualizar produto existente.

#### Cenários Negativos

* Atualizar produto inexistente.
* Atualizar sem autenticação.
* Atualizar com token inválido.

---

### DELETE /produtos/{id}

#### Cenários Positivos

* Excluir produto existente.

#### Cenários Negativos

* Excluir produto inexistente.
* Excluir sem autenticação.

---

### POST /carrinhos

#### Cenários Positivos

* Adicionar produto ao carrinho.
* Adicionar múltiplos produtos ao carrinho.

#### Cenários Negativos

* Adicionar produto inexistente.
* Adicionar quantidade maior que o estoque.
* Criar carrinho sem autenticação.

---

### GET /carrinhos

#### Cenários Positivos

* Listar carrinhos cadastrados.
* Buscar carrinho por ID.

#### Cenários Negativos

* Buscar carrinho inexistente.

---

### DELETE /carrinhos/concluir-compra

#### Cenários Positivos

* Concluir compra com sucesso.
* Validar redução de estoque.

#### Cenários Negativos

* Concluir compra sem carrinho ativo.

---

### DELETE /carrinhos/cancelar-compra

#### Cenários Positivos

* Cancelar compra.
* Validar devolução do estoque.

#### Cenários Negativos

* Cancelar compra sem carrinho ativo.

---

## 5. Critérios de Qualidade

Um teste será considerado pronto quando:

* Possuir nome claro e objetivo.
* Executar de forma independente.
* Não depender da ordem de execução.
* Validar status code.
* Validar corpo da resposta.
* Validar regras de negócio relevantes.
* Possuir assertions suficientes para detectar falhas reais.
* Utilizar dados dinâmicos quando necessário.
* Estiver documentado e revisado.

### Critérios de Aprovação da Suíte

* 100% dos testes executados.
* 0 falhas críticas.
* 0 erros de execução.
* Cobertura dos fluxos principais da API.
* Evidências geradas em relatório de execução.

---

Versão: 1.0

Autor: Renan Pacheco

## 5. Critérios de Qualidade

Um teste será considerado pronto quando:

* Possuir nome claro e objetivo.
* Executar de forma independente.
* Não depender da ordem de execução.
* Validar o código de status HTTP.
* Validar o corpo da resposta.
* Validar regras de negócio relevantes.
* Possuir assertions suficientes para detectar falhas reais.
* Utilizar dados dinâmicos quando necessário.
* Estiver documentado e revisado.

### Critérios de Aprovação da Suíte

* 100% dos testes executados.
* 0 falhas críticas.
* 0 erros de execução.
* Cobertura dos principais fluxos da API.
* Evidências geradas por meio de relatório de execução.

---

## 6. Cobertura da Automação

### Fórmula

Cobertura (%) = (Casos Implementados / Casos Planejados) × 100

### Resultado Atual

* Casos de teste planejados: 61
* Casos de teste implementados: 33
* Casos de teste pendentes: 28

Cobertura atual da suíte:

**(33 / 61) × 100 = 54,10%**

### Observações

Os cenários relacionados à validação de campos obrigatórios e demais validações de entrada não foram totalmente implementados nesta etapa. A priorização foi direcionada para os fluxos principais da API, contemplando autenticação, operações CRUD, gerenciamento de carrinhos, regras de negócio e validação dos retornos dos endpoints.

Esses cenários poderão ser adicionados em futuras evoluções da suíte para ampliar a cobertura funcional.

---

**Versão:** 2.0

**Autor:** Renan Pacheco

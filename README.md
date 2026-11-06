# bvapp-atas — Cenários de teste do RF-25296 (Arquivamento/Exclusão de Atas)

Mini projeto individual do **Laboratório 06 — Engenharia de Testes**, que organiza os cenários de teste da
Feature **25296 — Arquivamento/Exclusão de Atas**, do Epic **25283 — Gestão de Atas de Assembleia** do BVapp.

| | |
|---|---|
| **Autoria** | Thalyson Felicio de Moura |
| **Feature sob responsabilidade** | 25296 — Arquivamento/Exclusão de Atas |
| **Fonte dos requisitos** | Backlog do OpenProject exportado em 06/11/2026 |
| **Modelo dos cenários** | Exemplo "UC001 — Manter produtos" (Aula 06) |
| **Estrutura de pastas** | Estrutura do projeto `bvapp-didatico` (Aula 06) |

> **Importante.** Este repositório contém **apenas a documentação** dos cenários e a organização dos arquivos.
> Nenhuma funcionalidade foi implementada e nenhum teste foi automatizado ou executado, como pede a atividade.
> Os arquivos `test_*.py` contêm só docstring e comentários: são arquivos Python válidos, prontos para receber o
> código dos testes em etapas futuras.

---

## 1. Estrutura do projeto

```
bvapp-atas/
├── pyproject.toml                # dependências (Django, Selenium)
├── manage.py                     # entrada dos comandos do Django
├── config/                       # configuração global do projeto Django
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py                   # nenhuma rota definida ainda
│   ├── asgi.py
│   └── wsgi.py
├── functional_tests/             # cenários de teste (observam o sistema pelo navegador)
│   ├── __init__.py
│   └── test_rf25296_ctNN_<descricao>.py   # um arquivo por cenário (CT-25296-01 a 12)
├── atas/                         # aplicação Django do módulo de Atas
│   ├── __init__.py
│   ├── apps.py
│   ├── views.py                  # sem implementação
│   ├── tests.py                  # reservado para os testes internos
│   └── templates/atas/
└── docs/
    └── requisitos/
        └── RF-25296-arquivamento-exclusao-atas.md   # análise e correção dos requisitos
```

**Convenção de nomes.** Seguindo a Aula 06, o nome de cada arquivo combina o identificador do requisito
(`rf25296`), o identificador do cenário (`ctNN`) e uma descrição. Os identificadores são os IDs do backlog,
sem numeração paralela.

**Formato de cada cenário** (baseado no UC001 da Aula 06 e nos campos pedidos no Laboratório 06):

- docstring de cabeçalho: identificador e título, objetivo, requisitos relacionados, ator, **autoria**,
  pré-condições, **dados de teste e resultados esperados**, dúvidas registradas;
- `🟢 [FP]` fluxo principal, `🟠 [A#]` fluxos alternativos, `🟣 [RN#]` regras de negócio;
- `❓ [Q#]` dúvidas: regras ausentes ou contraditórias, registradas para esclarecimento, **sem inventar regra**.

---

## 2. Requisitos: análise e correção

O professor pediu que os requisitos vagos ou errados fossem analisados e corrigidos. A análise da Feature 25296
está em [`docs/requisitos/RF-25296-arquivamento-exclusao-atas.md`](docs/requisitos/RF-25296-arquivamento-exclusao-atas.md),
com:

1. o texto original do backlog;
2. 16 problemas encontrados (clareza, completude, consistência, testabilidade);
3. a versão corrigida da Feature, dos critérios de aceitação e das histórias de usuário;
4. a rastreabilidade problema → correção;
5. 13 questões pendentes para os stakeholders;
6. o impacto em Features de outros integrantes (25294, 25295, 25310), sem alterar o texto delas;
7. o texto pronto para atualizar o OpenProject.

Cada correção está classificada como **R** (reescrita, sem mudança de significado), **D** (derivada de outro
item do backlog) ou **P** (proposta que ainda precisa de validação).

---

## 3. Cenários de teste

| ID | Cenário | Requisitos (versão corrigida) | Origem no backlog | Situação |
|---|---|---|---|---|
| CT-25296-01 | Manter ata: ciclo completo (**CRUD**: criar, consultar, atualizar, arquivar) | CA01–CA04; RN02–RN05 | 25361, 25362 + RF-25293/25294/25295 | Especificado |
| CT-25296-02 | Arquivar ata oficializada | CA02; RN01, RN02 | 25362, 25363 | Especificado |
| CT-25296-03 | Ocultar ata arquivada da listagem de atas | CA03; RN03 | 25362, 25363, 25349 | Especificado |
| CT-25296-04 | Ocultar ata arquivada dos filtros por período e por tipo | CA03; RN03 | 25362, 25350, 25353 | Especificado |
| CT-25296-05 | Consultar ata arquivada pelo filtro de status "Arquivada" | CA04; RN04 | 25362, 25363 | Especificado (depende de Q12) |
| CT-25296-06 | Preservar os dados da ata após o arquivamento | CA02; RN02 | 25362, 25349 | Especificado |
| CT-25296-07 | Impedir exclusão de ata oficializada pela interface | CA01, CA07 (P); RN05 | 25361, 25364 | Especificado |
| CT-25296-08 | Impedir exclusão de ata oficializada por requisição direta | CA01; RN05 | 25364 | Especificado |
| CT-25296-09 | Impedir arquivamento por usuário sem permissão para editar | CA05; RN01 | 25363, 25360 | Especificado |
| CT-25296-10 | Registrar o arquivamento no log de auditoria | CA06; RN07 | 25408–25411 | Especificado |
| CT-25296-11 | Impedir exclusão de ata arquivada | RN06 (P) | 25361, 25362, 25364 | **Pendente** (Q04) |
| CT-25296-12 | Excluir ata não oficializada | — | Título da Feature | **Pendente** (Q02) |

São **10 cenários especificados** e **2 pendentes**. Os pendentes registram lacunas do requisito, do mesmo modo
que a Aula 06 trata os cenários de herança de Usina e de auditoria: não substituem regras ausentes por valores
inventados.

### Rastreabilidade: itens do backlog → cenários

| Item do backlog | Cenários |
|---|---|
| CA 25361 — proibir exclusão de ata oficializada | CT-01, CT-07, CT-08, CT-11 |
| CA 25362 — arquivamento, ocultação e busca avançada | CT-01 a CT-06 |
| US 25363 — arquivar ata oficializada | CT-01, CT-02, CT-03, CT-05, CT-09 |
| US 25364 — impedir exclusão definitiva | CT-01, CT-07, CT-08 |
| CA 25408 / 25409 / 25410 / 25411 — auditoria (RF-25310) | CT-10 |

---

## 4. Principais dúvidas em aberto

A lista completa está na seção 5 do documento de requisitos. As que mais afetam os testes:

- **Q01**: como uma Ata passa ao status "Oficializada" (necessário para preparar quase todos os cenários).
- **Q02**: se Atas não oficializadas podem ser excluídas.
- **Q04**: se a proteção contra exclusão continua depois do arquivamento.
- **Q12**: o filtro de status "Arquivada" ainda não existe em RF-25294 (Consulta e Listagem de Atas).

---

## 5. Reaproveitamento em etapas futuras

Os arquivos de `functional_tests/` seguem o padrão de descoberta de testes do Django (`test_*.py` dentro de um
pacote). Na etapa de automação, cada cenário poderá receber uma classe de teste
(ex.: `StaticLiveServerTestCase` com Selenium, como `CenariosRF001Test` na Aula 06), mantendo os comentários
como narrativa e marcando com `@skip` os trechos que dependem de questões pendentes.

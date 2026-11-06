# RF-25296 — Arquivamento/Exclusão de Atas: análise e correção dos requisitos

| Campo | Valor |
|---|---|
| Epic | 25283 — Gestão de Atas de Assembleia |
| Feature | 25296 — Arquivamento/Exclusão de Atas |
| Itens do backlog analisados | CA 25361, CA 25362, US 25363, US 25364 |
| Fonte | `OpenProject_backlog_geral_2026-11-0620261106-772-hs3t9p.csv` (exportado em 06/11/2026) |
| Itens relacionados consultados (não alterados) | RF-25294 (CA 25349, 25350; US 25352, 25353), RF-25295 (CA 25355; US 25360), RF-25310 (CA 25408, 25409) |
| Responsável pela análise | Thalyson Felicio de Moura |

> **Observação sobre o vínculo dos itens.** O CSV exportado não possui coluna de item pai (Parent).
> A associação dos CAs 25361–25362 e das USs 25363–25364 à Feature 25296 foi deduzida pela
> sequência dos IDs e pelo conteúdo dos textos.

---

## 1. Versão original (transcrição literal do backlog)

**Feature 25296 — Arquivamento/Exclusão de Atas**
Descrição: *(vazia)*

**CA 25361** — CA01 - O sistema não deve permitir a exclusão (deleção definitiva do banco de dados) de atas já oficializadas

**CA 25362** — CA02 - O sistema deve permitir o "Arquivamento" da ata, mudando seu status para "Arquivada" e ocultando-a das listagens padrão do sistema, mantendo-a disponível apenas via filtros de busca avançada

**US 25363** — US - Arquivar ata oficializada
> **Dado** que o usuário tenha permissão para visualizar Atas e editar Atas **E** aperte em arquivar Ata **Então** o sistema deve atualizar o status da Ata para "Arquivada" **E** parar de exibir essa Ata na tela de visualização de Atas **E** voltar a exibi-la apenas quando o usuário especificar, por meio do filtro de busca avançada, que quer visualizar Atas com status de "Arquivada".

**US 25364** — US - Impedir exclusão definitiva de ata do sistema
> **Dado** que uma Ata foi marcada com "Oficializada" **Então** o sistema deve bloquear qualquer tentativa de excluir essa Ata do banco de dados.

---

## 2. Análise: problemas encontrados

Aspectos avaliados: **clareza** (o texto admite uma única interpretação?), **completude** (o comportamento
esperado está todo descrito?), **consistência** (o texto concorda com ele mesmo e com os demais requisitos?)
e **testabilidade** (é possível definir preparação, ação e resultado observável?).

| ID | Item | Aspecto | Problema | Evidência |
|---|---|---|---|---|
| PR01 | Feature 25296 | Completude | A Feature não tem descrição. As Features já reorganizadas pela equipe (ex.: 25292) seguem o formato *Descrição / Caminhos Alternativos / Regras de Negócio*. | Campo *Description* vazio no CSV |
| PR02 | CA 25361, US 25364 | Clareza / Consistência | O termo "oficializada" não é definido em nenhum requisito do módulo e aparece de formas diferentes: "atas já oficializadas" (CA) e "marcada com 'Oficializada'" (US). Não se sabe se é um status ou uma marcação à parte, nem como a ata chega a ele. | CA 25361; US 25364 |
| PR03 | CA 25361, US 25364 | Clareza / Testabilidade | "Deleção definitiva do banco de dados" e "excluir essa Ata do banco de dados" descrevem detalhe de implementação, não comportamento observável pela pessoa usuária. | CA 25361; US 25364 |
| PR04 | CA 25361, US 25364 | Testabilidade | Não está definido o que o sistema faz quando recusa a exclusão (o que a pessoa usuária observa). Sem isso não há resultado esperado verificável. | "não deve permitir" / "bloquear qualquer tentativa" |
| PR05 | CA 25362 | Testabilidade | Um único critério reúne três comportamentos diferentes: (a) mudar o status, (b) ocultar das listagens, (c) manter disponível pela busca avançada. Uma falha em um deles não fica localizável. | CA 25362 |
| PR06 | CA 25362 | Clareza | "Listagens padrão do sistema" não identifica quais listagens. No módulo, a listagem de Atas está em RF-25294, com listagem simples (CA 25349) e listagem filtrada por período e tipo (CA 25350). | CA 25362; CA 25349; CA 25350 |
| PR07 | CA 25362, US 25363 × RF-25294 | Consistência | A Feature manda consultar atas arquivadas "via filtros de busca avançada", mas RF-25294 só define filtro por intervalo de datas e por tipo de assembleia. Não existe, no backlog, filtro por status. | CA 25350; US 25353 |
| PR08 | US 25363 | Clareza / Forma | A ação ("aperte em arquivar Ata") está dentro do **Dado**, e não existe **Quando**. O verbo "apertar" amarra o requisito a um elemento visual (botão). A última cláusula mistura o arquivamento com a consulta de arquivadas, que é outro comportamento. | US 25363 |
| PR09 | US 25364 | Completude / Forma | Não há ator, não há evento (**Quando**) e não há resultado observável, só "bloquear". | US 25364 |
| PR10 | CA 25361 × CA 25362 | Consistência (lacuna lógica) | O arquivamento troca o status para "Arquivada". Se "Oficializada" for um status, a ata arquivada deixa de ser "Oficializada" e, pela redação atual, a proibição de exclusão deixa de valer para ela. Assim, arquivar uma ata oficializada a tornaria excluível, contrariando a intenção de preservar o documento. | CA 25361; CA 25362; título da US 25363 |
| PR11 | US 25363 | Completude | Só o caso com permissão é descrito. Não se diz o que acontece com quem tem permissão para visualizar, mas não para editar Atas. | US 25363 |
| PR12 | Feature 25296 | Completude | O título fala em "Exclusão", mas nenhum item diz se atas **não** oficializadas podem ser excluídas, por quem e como. | Título da Feature; CA 25361 |
| PR13 | CA 25362 × US 25363 | Consistência | O CA permite arquivar "a ata" (qualquer uma); o título da US fala em "Arquivar ata **oficializada**". Não se sabe quais atas podem ser arquivadas. | CA 25362; US 25363 |
| PR14 | US 25363 × RF-25295 | Consistência | Aqui a autorização é por **permissão** ("permissão para visualizar Atas e editar Atas"); em RF-25295 a edição é restrita por **perfil** ("Diretoria ou Administrador"). | US 25363; CA 25355 |
| PR15 | Feature 25296 × RF-25310 | Rastreabilidade | RF-25310 exige registrar em log toda ação de "arquivamento" no módulo de Atas, mas a Feature 25296 não referencia essa obrigação. | CA 25408; CA 25409 |
| PR16 | Feature 25296 | Completude | Não estão definidos: reversão do arquivamento (desarquivar), confirmação antes de arquivar, textos das mensagens e o que é possível fazer com uma ata arquivada (visualizar detalhes, exportar, editar). | Ausência nos itens analisados |

---

## 3. Versão corrigida

Cada correção tem um **tipo**:

- **R — Reescrita:** muda a forma, mas não o significado do requisito original.
- **D — Derivada:** completa o requisito com informação que já existe em outro item do backlog (fonte citada).
- **P — Proposta:** resolve uma lacuna ou contradição com uma decisão que **ainda precisa ser validada** pelos
  stakeholders (PO/professor). Fica marcada para não ser confundida com regra confirmada.

O que não pôde ser decidido nem com proposta fundamentada ficou na seção 5 (*Questões pendentes*).

### 3.1 Feature — texto corrigido

**RF-25296: Arquivamento/Exclusão de Atas**

**Descrição:** O sistema deve permitir que o usuário com permissão para visualizar e editar Atas arquive uma
Ata, alterando seu status para "Arquivada". Uma Ata arquivada deixa de ser exibida na listagem de Atas
(RF-25294) e permanece disponível para consulta quando o usuário seleciona explicitamente o status "Arquivada"
no filtro de busca avançada. O sistema deve impedir a exclusão definitiva de Atas com status "Oficializada",
de modo que elas permaneçam no sistema.

**Caminhos Alternativos:**

- **Tentativa de exclusão de Ata oficializada:** ao receber uma solicitação de exclusão definitiva de uma Ata
  com status "Oficializada", feita pela interface ou por requisição direta ao sistema, o sistema deve recusar
  a exclusão e manter a Ata inalterada. *(P)* O sistema deve informar ao usuário que Atas oficializadas não
  podem ser excluídas.
- **Arquivamento sem permissão:** ao receber uma solicitação de arquivamento feita por usuário que não tem
  permissão para editar Atas, o sistema não deve realizar o arquivamento, e o status da Ata deve permanecer
  inalterado.
- **Consulta de Atas arquivadas:** ao selecionar o status "Arquivada" no filtro de busca avançada, o sistema
  deve exibir as Atas arquivadas.

**Regras de Negócio e Validações:**

| RN | Regra | Tipo | Fonte |
|---|---|---|---|
| RN01 | Arquivar uma Ata exige permissão para visualizar Atas e para editar Atas. | R | US 25363 |
| RN02 | O arquivamento altera somente o status da Ata para "Arquivada"; título, data de criação, tipo de assembleia e conteúdo permanecem os mesmos. | R + D | CA 25362 ("mudando seu status"); CA 25349 (dados exibidos de uma ata) |
| RN03 | Uma Ata com status "Arquivada" não é exibida na listagem de Atas nem nos resultados dos filtros por intervalo de datas e por tipo de assembleia. | D | CA 25362; US 25363; CA 25349; CA 25350 |
| RN04 | Uma Ata com status "Arquivada" só é exibida quando o usuário seleciona explicitamente o status "Arquivada" no filtro de busca avançada. Para cada Ata, são exibidos título, data de criação, tipo de assembleia e status. | R + D | CA 25362; US 25363; CA 25349 |
| RN05 | Uma Ata com status "Oficializada" não pode ser excluída definitivamente por nenhum usuário, por nenhum meio (interface ou requisição direta ao sistema). | R | CA 25361; US 25364 ("qualquer tentativa") |
| RN06 | A proibição de RN05 continua valendo depois que uma Ata oficializada é arquivada. | **P** | Resolve PR10. Ver Q04 |
| RN07 | Todo arquivamento deve ser registrado no log de auditoria, com nome do usuário responsável, data/hora, ação realizada e Ata afetada. | D | CA 25408; CA 25409 (RF-25310) |

### 3.2 Critérios de aceitação corrigidos

| Novo | Origem | Tipo | Critério corrigido |
|---|---|---|---|
| CA01 | CA 25361 | R | Dada uma Ata com status "Oficializada", quando qualquer usuário solicitar sua exclusão definitiva, pela interface ou por requisição direta ao sistema, o sistema deve recusar a solicitação e a Ata deve continuar existindo, com o mesmo conteúdo e o mesmo status. |
| CA02 | CA 25362 (parte a) | R | Quando um usuário com permissão para visualizar e editar Atas arquivar uma Ata, o sistema deve alterar o status dessa Ata para "Arquivada", sem alterar título, data de criação, tipo de assembleia e conteúdo. |
| CA03 | CA 25362 (parte b) | R + D | Uma Ata com status "Arquivada" não deve ser exibida na listagem de Atas (CA 25349) nem nos resultados dos filtros por intervalo de datas e por tipo de assembleia (CA 25350). |
| CA04 | CA 25362 (parte c) + US 25363 | R + D | Quando o usuário selecionar o status "Arquivada" no filtro de busca avançada, o sistema deve exibir as Atas arquivadas, com título, data de criação, tipo de assembleia e status. |
| CA05 | US 25363 (pré-condição) | D | Quando um usuário que não tem permissão para editar Atas tentar arquivar uma Ata, o sistema não deve realizar o arquivamento e o status da Ata deve permanecer inalterado. |
| CA06 | CA 25408, CA 25409 | D | Após um arquivamento, o log de auditoria deve conter um registro com o nome do usuário responsável, a data/hora, a ação "arquivamento" e a identificação da Ata afetada. |
| CA07 | — | **P** | Ao recusar a exclusão de uma Ata oficializada, o sistema deve informar ao usuário que Atas oficializadas não podem ser excluídas. *(Texto exato da mensagem: Q09.)* |

### 3.3 Histórias de usuário corrigidas

Formato DADO / QUANDO / ENTÃO, o mesmo usado nas demais USs do backlog (ex.: 25318, 25324).

**US 25363 — Arquivar ata oficializada** *(R)*
> **DADO** que o usuário tem permissão para visualizar e editar Atas **E** existe uma Ata com status "Oficializada"
> exibida na listagem de Atas
> **QUANDO** ele acionar a opção de arquivar essa Ata
> **ENTÃO** o sistema deve alterar o status da Ata para "Arquivada" **E** deixar de exibi-la na listagem de Atas.

**US 25296-N1 — Consultar atas arquivadas** *(nova; D — separada da última cláusula da US 25363)*
> **DADO** que existe ao menos uma Ata com status "Arquivada" **E** o usuário tem permissão para visualizar Atas
> **QUANDO** ele selecionar o status "Arquivada" no filtro de busca avançada da listagem de Atas
> **ENTÃO** o sistema deve exibir as Atas arquivadas, com título, data de criação, tipo de assembleia e status.

**US 25364 — Impedir exclusão definitiva de ata oficializada** *(R)*
> **DADO** que existe uma Ata com status "Oficializada"
> **QUANDO** qualquer usuário tentar excluí-la definitivamente, pela interface ou por requisição direta ao sistema
> **ENTÃO** o sistema deve recusar a exclusão **E** a Ata deve continuar existindo, com o mesmo conteúdo e o mesmo status.

**US 25296-N2 — Impedir arquivamento por usuário sem permissão** *(nova; D — caso negativo da pré-condição da US 25363)*
> **DADO** que o usuário tem permissão para visualizar Atas **E** não tem permissão para editar Atas
> **QUANDO** ele tentar arquivar uma Ata
> **ENTÃO** o sistema não deve realizar o arquivamento **E** o status da Ata deve permanecer inalterado.

---

## 4. Rastreabilidade das correções

| Problema | Correção aplicada | Tipo |
|---|---|---|
| PR01 | Descrição da Feature escrita no formato da equipe (3.1) | R + D |
| PR02 | Termo padronizado como **status "Oficializada"** em todos os itens; definição pendente em Q01 | R (definição: Q01) |
| PR03 | "Deleção do banco de dados" substituída por "exclusão definitiva" com resultado observável ("a Ata deve continuar existindo") | R |
| PR04 | Resultado observável definido em CA01 e US 25364; mensagem ao usuário como proposta CA07 | R + P |
| PR05 | CA 25362 dividido em CA02, CA03 e CA04 | R |
| PR06 | "Listagens padrão" substituído pelas listagens identificadas em RF-25294 (CA 25349, CA 25350) | D |
| PR07 | Busca avançada definida como seleção do status "Arquivada" (texto já presente na US 25363); **impacto em RF-25294** registrado na seção 6 | D (Q12) |
| PR08 | US 25363 reescrita com DADO/QUANDO/ENTÃO; consulta separada na US 25296-N1; "apertar" substituído por "acionar a opção" | R |
| PR09 | US 25364 reescrita com evento e resultado observável | R |
| PR10 | RN06 proposta | **P** (Q04) |
| PR11 | CA05 e US 25296-N2 criados | D |
| PR12 | Não corrigido: depende de decisão (Q02) | — |
| PR13 | Mantido o escopo da US original (ata oficializada); dúvida registrada | — (Q03) |
| PR14 | Mantida a autorização por permissão, como na US 25363; divergência registrada | — (Q11) |
| PR15 | RN07 e CA06 referenciam RF-25310 | D |
| PR16 | Não corrigido: depende de decisão | — (Q05, Q06, Q09, Q10) |

---

## 5. Questões pendentes (para esclarecimento com os stakeholders)

Não foram inventadas respostas para estas questões. Os cenários de teste que dependem delas indicam a questão
correspondente.

| ID | Questão | Por que é necessária | Itens afetados |
|---|---|---|---|
| Q01 | Como uma Ata passa a ter o status "Oficializada"? Quais são todos os status possíveis de uma Ata e quais transições são permitidas? | Sem isso não é possível preparar, de forma repetível, uma Ata oficializada para os testes. | RN05, CA01, US 25363, US 25364 |
| Q02 | Atas que **não** estão oficializadas podem ser excluídas definitivamente? Se sim, em quais status, por quem e com qual confirmação? | O título da Feature fala em "Exclusão", mas nenhuma regra a descreve. | Feature 25296; CT-25296-12 |
| Q03 | Quais Atas podem ser arquivadas: somente as oficializadas (título da US 25363) ou qualquer Ata (CA 25362)? | Define as pré-condições do arquivamento. | CA02, US 25363 |
| Q04 | A proibição de exclusão continua valendo depois que uma Ata oficializada é arquivada? (RN06 proposta) | Resolve a lacuna lógica PR10. | RN06; CT-25296-11 |
| Q05 | O arquivamento pode ser desfeito (desarquivar)? Se sim, para qual status a Ata volta e quem pode fazer isso? | Não há regra; não foi criado cenário para isso. | Feature 25296 |
| Q06 | O sistema deve pedir confirmação antes de arquivar? | Define um passo do fluxo principal. | US 25363; CT-25296-02 |
| Q07 | Para o usuário sem permissão de editar Atas, a opção de arquivar deve ficar oculta (como faz a US 25360 para edição) ou ser exibida e recusada? | Define o resultado observável de CA05. | CA05; CT-25296-09 |
| Q08 | Para uma Ata oficializada, a opção de excluir deve ficar oculta na interface ou ser exibida e recusada? | Define o resultado observável de CA01 na interface. | CA01; CT-25296-07 |
| Q09 | Quais são os textos das mensagens de sucesso do arquivamento e de recusa da exclusão? | Mensagens não podem ser inventadas nos resultados esperados. | CA07; CT-25296-02, 07 |
| Q10 | Uma Ata arquivada pode ter seus detalhes visualizados, ser exportada em PDF (CA 25351) ou editada (RF-25295)? | Define o que é possível fazer com a Ata depois de arquivada. | CT-25296-06 |
| Q11 | A autorização é por perfil (Diretoria/Administrador, CA 25355) ou por permissão ("visualizar e editar Atas", US 25363)? Consultar arquivadas exige só permissão de visualizar? | Define os atores dos cenários. | RN01, CA05, US 25296-N1 |
| Q12 | O filtro de status "Arquivada" será incluído em RF-25294? Ele pode ser combinado com os filtros de período e de tipo? | A busca avançada não existe em RF-25294 (PR07). | CA04; RF-25294 |
| Q13 | Com o filtro "Arquivada" selecionado, a listagem mostra somente as Atas arquivadas ou também as demais? | Define o resultado esperado da consulta. | CA04; CT-25296-05 |

---

## 6. Impacto em requisitos de outras Features (não alterados aqui)

Estes itens são de responsabilidade de outros integrantes. As observações abaixo devem ser comunicadas a eles;
**nenhum texto dessas Features foi alterado neste documento.**

| Feature | Item | Impacto |
|---|---|---|
| RF-25294 Consulta e Listagem de Atas | CA 25350, US 25353 | Precisa incluir um filtro por status (ao menos "Arquivada") para que a busca avançada exigida por RF-25296 exista (Q12). |
| RF-25295 Atualizações e Versionamento | CA 25355, US 25360 | Precisa alinhar o modelo de autorização (perfil × permissão) com RF-25296 (Q11). |
| RF-25310 Visualização de Logs | CA 25408, CA 25409 | Já exige o registro do arquivamento; está coerente com RN07/CA06. |

---

## 7. Texto pronto para atualizar o OpenProject

Para colar no campo *Description* da Feature 25296. O conteúdo é o mesmo da seção 3.1; as marcações *(P)*
indicam propostas pendentes de validação.

```
**RF-25296: Arquivamento/Exclusão de Atas** **Descrição:** O sistema deve permitir que o usuário com permissão para visualizar e editar Atas arquive uma Ata, alterando seu status para "Arquivada". Uma Ata arquivada deixa de ser exibida na listagem de Atas (RF-25294) e permanece disponível para consulta quando o usuário seleciona explicitamente o status "Arquivada" no filtro de busca avançada. O sistema deve impedir a exclusão definitiva de Atas com status "Oficializada", de modo que elas permaneçam no sistema. **Caminhos Alternativos:** **• Tentativa de exclusão de Ata oficializada:** ao receber uma solicitação de exclusão definitiva de uma Ata com status "Oficializada", feita pela interface ou por requisição direta ao sistema, o sistema deve recusar a exclusão e manter a Ata inalterada. (P) O sistema deve informar ao usuário que Atas oficializadas não podem ser excluídas. **• Arquivamento sem permissão:** ao receber uma solicitação de arquivamento feita por usuário que não tem permissão para editar Atas, o sistema não deve realizar o arquivamento, e o status da Ata deve permanecer inalterado. **• Consulta de Atas arquivadas:** ao selecionar o status "Arquivada" no filtro de busca avançada, o sistema deve exibir as Atas arquivadas. **Regras de Negócio e Validações:** **• RN01 -** Arquivar uma Ata exige permissão para visualizar Atas e para editar Atas. **• RN02 -** O arquivamento altera somente o status da Ata para "Arquivada"; título, data de criação, tipo de assembleia e conteúdo permanecem os mesmos. **• RN03 -** Uma Ata com status "Arquivada" não é exibida na listagem de Atas nem nos resultados dos filtros por intervalo de datas e por tipo de assembleia. **• RN04 -** Uma Ata com status "Arquivada" só é exibida quando o usuário seleciona explicitamente o status "Arquivada" no filtro de busca avançada, com título, data de criação, tipo de assembleia e status. **• RN05 -** Uma Ata com status "Oficializada" não pode ser excluída definitivamente por nenhum usuário, por nenhum meio (interface ou requisição direta ao sistema). **• RN06 (P) -** A proibição de RN05 continua valendo depois que uma Ata oficializada é arquivada. **• RN07 -** Todo arquivamento deve ser registrado no log de auditoria (RF-25310), com nome do usuário responsável, data/hora, ação realizada e Ata afetada.
```

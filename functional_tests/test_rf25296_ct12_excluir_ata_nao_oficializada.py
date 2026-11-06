'''
CT-25296-12 - Excluir ata não oficializada  [CENÁRIO PENDENTE]

Situação: PENDENTE. O backlog não define se Atas não oficializadas podem ser
excluídas (questão Q02). Este cenário registra a lacuna e não define fluxo
nem resultado esperado, para não inventar uma regra.

Objetivo: Verificar o comportamento do sistema ao excluir uma Ata que não
está com o status "Oficializada", como sugere o título da Feature
"Arquivamento/Exclusão de Atas".

Requisitos:
- RF-25296: título da Feature (menciona "Exclusão")
- Origem no backlog: CA 25361 (só trata das Atas oficializadas)

Ator:
- A definir (Q02, Q11)

Autoria:
- Thalyson Felicio de Moura

Pré-condições:
- A definir: os status possíveis de uma Ata não estão definidos (Q01).

Dados de teste:
- A definir.

Resultado esperado:
- A definir (Q02).

Dúvidas registradas (docs/requisitos/RF-25296-arquivamento-exclusao-atas.md):
- Q01 - Quais são os status possíveis de uma Ata.
- Q02 - Se Atas não oficializadas podem ser excluídas, em quais status, por
  quem e com qual confirmação.
'''

# ❓ [Q02] DÚVIDA - EXCLUSÃO DE ATAS NÃO OFICIALIZADAS
# ---------------------------------------------------------------

# O título da Feature 25296 fala em "Exclusão", mas o único requisito sobre
# exclusão (CA 25361 / US 25364) proíbe a exclusão de Atas oficializadas.
# Não há regra para as demais Atas.
#
# Possibilidades que só os stakeholders podem decidir (não são regras):
# - a exclusão de Atas não oficializadas é permitida;
# - nenhuma Ata pode ser excluída, e o arquivamento é a única forma de
#   retirar uma Ata de circulação.
#
# Quando a Q02 for respondida, este cenário deverá receber fluxo principal,
# fluxos alternativos e resultados esperados, e o título da Feature poderá
# precisar de ajuste.

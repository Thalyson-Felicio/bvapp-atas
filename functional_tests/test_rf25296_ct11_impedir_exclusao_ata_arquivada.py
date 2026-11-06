'''
CT-25296-11 - Impedir exclusão definitiva de ata arquivada  [CENÁRIO PENDENTE]

Situação: PENDENTE. Depende da validação da proposta RN06 (questão Q04).
Enquanto a Q04 não for respondida, este cenário não tem resultado esperado
confirmado e não deve ser considerado na verificação do requisito.

Objetivo: Verificar que uma Ata oficializada continua protegida contra
exclusão definitiva depois de arquivada.

Requisitos:
- RF-25296 (versão corrigida): RN06 (proposta), RN05
- Origem no backlog: CA 25361, US 25364 (proibição), CA 25362 (arquivamento)

Ator:
- Usuário com permissão para visualizar e editar Atas

Autoria:
- Thalyson Felicio de Moura

Pré-condições:
- Existe a Ata "Ata CT-25296-11", que foi oficializada e depois arquivada
  (status "Arquivada").

Dados de teste (fictícios):
- "Ata CT-25296-11", tipo "Ordinária", status "Arquivada".

Resultado esperado (se a RN06 for confirmada):
- A exclusão é recusada e a Ata continua disponível pelo filtro de status
  "Arquivada", com os mesmos dados.

Dúvidas registradas (docs/requisitos/RF-25296-arquivamento-exclusao-atas.md):
- Q04 - Se a proibição de exclusão continua depois do arquivamento.
'''

# 🟢 [FP] - FLUXO PRINCIPAL (válido somente se a RN06 for confirmada)
# ---------------------------------------------------------------

# O ator seleciona o status "Arquivada" no filtro de busca avançada.

# O sistema exibe "Ata CT-25296-11".

# O ator tenta excluir "Ata CT-25296-11" definitivamente, pela interface
# ou por requisição direta (como em CT-25296-07 e CT-25296-08).

# O sistema recusa a exclusão. [RN06]

# O ator seleciona novamente o status "Arquivada" no filtro.

# O sistema continua exibindo "Ata CT-25296-11" com os mesmos dados.


# ❓ [Q04] DÚVIDA - LACUNA ENTRE ARQUIVAMENTO E PROIBIÇÃO DE EXCLUSÃO
# ---------------------------------------------------------------

# A proibição de exclusão (CA 25361, US 25364) vale para Atas com status
# "Oficializada". O arquivamento (CA 25362) troca o status para "Arquivada".
# Pela redação original, uma Ata oficializada, depois de arquivada, deixaria
# de estar protegida. A proposta RN06 fecha essa lacuna, mas precisa ser
# validada pelos stakeholders antes de virar resultado esperado.

'''
CT-25296-03 - Ocultar ata arquivada da listagem de atas

Objetivo: Verificar que, depois de arquivada, a Ata deixa de ser exibida na
listagem de Atas, enquanto as Atas não arquivadas continuam sendo exibidas.

Requisitos:
- RF-25296 (versão corrigida): CA03; RN03
- Origem no backlog: CA 25362, US 25363
- Relacionado: RF-25294 (CA 25349, US 25352)

Ator:
- Usuário com permissão para visualizar e editar Atas

Autoria:
- Thalyson Felicio de Moura

Pré-condições:
- O ator está autenticado e tem permissão para visualizar e editar Atas.
- Existem duas Atas com status "Oficializada": "Ata CT-25296-03-A" e
  "Ata CT-25296-03-B". [Q01]

Dados de teste (fictícios):
- "Ata CT-25296-03-A": será arquivada.
- "Ata CT-25296-03-B": permanece com status "Oficializada" (controle).

Resultados esperados:
- Antes do arquivamento, as duas Atas aparecem na listagem.
- Depois do arquivamento, só "Ata CT-25296-03-B" aparece na listagem.

Dúvidas registradas (docs/requisitos/RF-25296-arquivamento-exclusao-atas.md):
- Q01 - Como preparar Atas com status "Oficializada".
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator acessa a listagem de Atas.

# O sistema exibe "Ata CT-25296-03-A" e "Ata CT-25296-03-B".

# O ator arquiva "Ata CT-25296-03-A" (conforme CT-25296-02).

# O ator acessa novamente a listagem de Atas, sem aplicar filtros.

# O sistema não exibe "Ata CT-25296-03-A". [CA03] [RN03]

# O sistema continua exibindo "Ata CT-25296-03-B", com título, data de
# criação, tipo de assembleia e status. (CA 25349)


# 🟠 [A1] - RECARREGAR A LISTAGEM
# ---------------------------------------------------------------

# O ator sai da listagem e volta a ela por outro caminho do menu.

# O sistema continua sem exibir "Ata CT-25296-03-A".
# A ocultação não pode depender de a página ter sido recarregada.


# 🟣 [RN03] OCULTAÇÃO DA ATA ARQUIVADA
# ---------------------------------------------------------------

# Uma Ata com status "Arquivada" não é exibida na listagem de Atas nem nos
# resultados dos filtros por intervalo de datas e por tipo de assembleia.
# A parte dos filtros é verificada em CT-25296-04.

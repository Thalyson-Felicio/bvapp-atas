'''
CT-25296-05 - Consultar ata arquivada pelo filtro de status "Arquivada"

Objetivo: Verificar que uma Ata arquivada volta a ser exibida quando o
usuário seleciona explicitamente o status "Arquivada" no filtro de busca
avançada, com os dados previstos para a listagem.

Requisitos:
- RF-25296 (versão corrigida): CA04; RN04; US 25296-N1
- Origem no backlog: CA 25362, US 25363
- Relacionado: RF-25294 (CA 25349: dados exibidos de cada Ata)

Ator:
- Usuário com permissão para visualizar Atas (Q11)

Autoria:
- Thalyson Felicio de Moura

Pré-condições:
- O ator está autenticado e tem permissão para visualizar Atas.
- Existe a Ata "Ata CT-25296-05", com status "Arquivada".

Dados de teste (fictícios):
- "Ata CT-25296-05", tipo "Ordinária", status "Arquivada".

Resultados esperados:
- Sem o filtro de status: "Ata CT-25296-05" não aparece.
- Com o status "Arquivada" selecionado: "Ata CT-25296-05" aparece com
  título, data de criação, tipo de assembleia "Ordinária" e status
  "Arquivada".

Dúvidas registradas (docs/requisitos/RF-25296-arquivamento-exclusao-atas.md):
- Q11 - Se consultar Atas arquivadas exige apenas permissão de visualizar.
- Q12 - O filtro de status ainda não existe em RF-25294.
- Q13 - Se o filtro "Arquivada" mostra só as arquivadas ou também as demais.
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator acessa a listagem de Atas.

# O sistema não exibe "Ata CT-25296-05". [RN03]

# O ator abre o filtro de busca avançada e seleciona o status
# "Arquivada". [Q12]

# O ator aplica o filtro.

# O sistema exibe "Ata CT-25296-05". [CA04] [RN04]

# O ator verifica que a Ata é exibida com título, data de criação, tipo
# de assembleia "Ordinária" e status "Arquivada". (CA 25349)


# 🟠 [A1] - REMOVER O FILTRO DE STATUS
# ---------------------------------------------------------------

# O ator remove a seleção do status "Arquivada" e aplica o filtro.

# O sistema volta a não exibir "Ata CT-25296-05". [RN03]


# 🟣 [RN04] CONSULTA DA ATA ARQUIVADA
# ---------------------------------------------------------------

# Uma Ata com status "Arquivada" só é exibida quando o usuário seleciona
# explicitamente o status "Arquivada" no filtro de busca avançada.


# ❓ [Q13] DÚVIDA - CONTEÚDO DA LISTAGEM FILTRADA
# ---------------------------------------------------------------

# O requisito não define se, com o filtro "Arquivada", a listagem mostra
# somente as Atas arquivadas ou também as demais. Por isso, este cenário
# verifica apenas que a Ata arquivada aparece, sem afirmar nada sobre as
# outras Atas.

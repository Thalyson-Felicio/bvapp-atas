'''
CT-25296-09 - Impedir arquivamento por usuário sem permissão para editar atas

Objetivo: Verificar que um usuário com permissão apenas para visualizar
Atas não consegue arquivar uma Ata e que o status da Ata permanece
inalterado.

Requisitos:
- RF-25296 (versão corrigida): CA05; RN01; US 25296-N2
- Origem no backlog: US 25363 (exige permissão para visualizar e editar)
- Relacionado: US 25360 (oculta a edição para quem não tem permissão)

Ator:
- Usuário com permissão para visualizar Atas e sem permissão para editar
  Atas

Autoria:
- Thalyson Felicio de Moura

Pré-condições:
- O ator está autenticado com permissão apenas para visualizar Atas.
- Existe a Ata "Ata CT-25296-09", com status "Oficializada". [Q01]

Dados de teste (fictícios):
- "Ata CT-25296-09", tipo "Ordinária", status "Oficializada".

Resultados esperados:
- O arquivamento não é realizado.
- "Ata CT-25296-09" continua na listagem com status "Oficializada".

Dúvidas registradas (docs/requisitos/RF-25296-arquivamento-exclusao-atas.md):
- Q01 - Como preparar uma Ata com status "Oficializada".
- Q07 - Se a opção de arquivar fica oculta ou é exibida e recusada.
- Q11 - Perfil x permissão.
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator acessa a listagem de Atas.

# O sistema exibe "Ata CT-25296-09" com status "Oficializada".

# O ator seleciona "Ata CT-25296-09" e procura a opção de arquivar. [Q07]
# - Se a opção não for exibida, segue para [A1].
# - Se a opção for exibida, o ator a aciona.

# O sistema não realiza o arquivamento. [CA05] [RN01]

# O ator acessa novamente a listagem de Atas.

# O sistema exibe "Ata CT-25296-09" com status "Oficializada". [CA05]


# 🟠 [A1] - OPÇÃO DE ARQUIVAR NÃO EXIBIDA
# ---------------------------------------------------------------

# O sistema não exibe a opção de arquivar para o ator.

# O ator verifica que "Ata CT-25296-09" continua na listagem com status
# "Oficializada". [CA05]


# 🟠 [A2] - SOLICITAÇÃO DIRETA DE ARQUIVAMENTO
# ---------------------------------------------------------------

# Sem usar as telas, o ator envia diretamente ao sistema uma solicitação de
# arquivamento de "Ata CT-25296-09", com sua sessão autenticada.

# O sistema não realiza o arquivamento.

# "Ata CT-25296-09" continua com status "Oficializada". [RN01]


# 🟣 [RN01] PERMISSÃO PARA ARQUIVAR
# ---------------------------------------------------------------

# Arquivar uma Ata exige permissão para visualizar Atas e para editar Atas.


# ❓ [Q07] DÚVIDA - COMPORTAMENTO DA OPÇÃO DE ARQUIVAR
# ---------------------------------------------------------------

# A US 25360 oculta a opção de editar para quem não tem permissão, mas o
# backlog não diz se o mesmo vale para arquivar. Os dois caminhos estão
# descritos ([FP] e [A1]); o resultado obrigatório é o mesmo: o status
# não muda.

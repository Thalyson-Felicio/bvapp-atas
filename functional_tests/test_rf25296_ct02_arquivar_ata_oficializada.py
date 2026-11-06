'''
CT-25296-02 - Arquivar ata oficializada

Objetivo: Verificar que um usuário com permissão para visualizar e editar
Atas consegue arquivar uma Ata oficializada e que o arquivamento altera o
status da Ata para "Arquivada".

Requisitos:
- RF-25296 (versão corrigida): CA02; RN01, RN02
- Origem no backlog: CA 25362, US 25363

Ator:
- Usuário com permissão para visualizar e editar Atas

Autoria:
- Thalyson Felicio de Moura

Pré-condições:
- O ator está autenticado e tem permissão para visualizar e editar Atas.
- Existe uma Ata com status "Oficializada" exibida na listagem de Atas. [Q01]

Dados de teste (fictícios):
- Ata: "Ata CT-25296-02", tipo "Extraordinária", status "Oficializada".

Resultados esperados:
- O status da Ata "Ata CT-25296-02" passa a "Arquivada".
- O título, a data de criação e o tipo de assembleia não mudam.

Dúvidas registradas (docs/requisitos/RF-25296-arquivamento-exclusao-atas.md):
- Q01 - Como preparar uma Ata com status "Oficializada".
- Q03 - Se Atas em outros status também podem ser arquivadas.
- Q06 - Se há confirmação antes de arquivar.
- Q09 - Texto da mensagem de sucesso.
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator acessa a listagem de Atas.

# O sistema exibe a Ata "Ata CT-25296-02" com status "Oficializada".

# O ator anota o título, a data de criação e o tipo de assembleia
# exibidos para essa Ata.

# O ator aciona a opção de arquivar a Ata "Ata CT-25296-02". [RN01] [A1]

# O sistema altera o status da Ata para "Arquivada". [CA02]

# O ator seleciona o status "Arquivada" no filtro de busca avançada.

# O sistema exibe a Ata "Ata CT-25296-02" com status "Arquivada" e com o
# mesmo título, a mesma data de criação e o mesmo tipo anotados. [RN02]


# 🟠 [A1] - CONFIRMAÇÃO DO ARQUIVAMENTO
# ---------------------------------------------------------------

# [Q06] O requisito não define se o sistema pede confirmação antes de
# arquivar. Se a confirmação for definida, o ator a confirma e o fluxo
# continua no passo seguinte do [FP]. Nenhum passo de confirmação é
# presumido neste cenário.


# 🟣 [RN01] PERMISSÃO PARA ARQUIVAR
# ---------------------------------------------------------------

# Arquivar uma Ata exige permissão para visualizar Atas e para editar Atas.

# 🟣 [RN02] O ARQUIVAMENTO ALTERA SOMENTE O STATUS
# ---------------------------------------------------------------

# Título, data de criação, tipo de assembleia e conteúdo permanecem os
# mesmos após o arquivamento.


# ❓ [Q09] DÚVIDA - MENSAGEM DE SUCESSO
# ---------------------------------------------------------------

# O requisito não define se o sistema exibe uma mensagem após o
# arquivamento nem o seu texto. O resultado esperado se limita à mudança
# de status.

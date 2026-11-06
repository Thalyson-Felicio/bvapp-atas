'''
CT-25296-06 - Preservar os dados da ata após o arquivamento

Objetivo: Verificar que o arquivamento altera somente o status da Ata e que
título, data de criação e tipo de assembleia permanecem iguais aos de antes
do arquivamento.

Requisitos:
- RF-25296 (versão corrigida): CA02; RN02
- Origem no backlog: CA 25362 ("mudando seu status para Arquivada")
- Relacionado: RF-25294 (CA 25349)

Ator:
- Usuário com permissão para visualizar e editar Atas

Autoria:
- Thalyson Felicio de Moura

Pré-condições:
- O ator está autenticado e tem permissão para visualizar e editar Atas.
- Existe a Ata "Ata CT-25296-06", com status "Oficializada". [Q01]

Dados de teste (fictícios):
- "Ata CT-25296-06", tipo "Extraordinária", status "Oficializada".

Resultados esperados:
| Dado               | Antes do arquivamento | Depois do arquivamento |
|--------------------|-----------------------|------------------------|
| Título             | "Ata CT-25296-06"     | "Ata CT-25296-06"      |
| Data de criação    | valor anotado (D)     | o mesmo valor D        |
| Tipo de assembleia | "Extraordinária"      | "Extraordinária"       |
| Status             | "Oficializada"        | "Arquivada"            |

Dúvidas registradas (docs/requisitos/RF-25296-arquivamento-exclusao-atas.md):
- Q01 - Como preparar uma Ata com status "Oficializada".
- Q10 - Se uma Ata arquivada pode ter seus detalhes visualizados ou ser
  exportada. Sem essa resposta, o conteúdo integral da Ata não pode ser
  comparado; o cenário compara somente os dados exibidos na listagem.
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator acessa a listagem de Atas.

# O ator anota o título, a data de criação (D), o tipo de assembleia e o
# status exibidos para "Ata CT-25296-06".

# O ator arquiva "Ata CT-25296-06" (conforme CT-25296-02).

# O ator seleciona o status "Arquivada" no filtro de busca avançada.

# O sistema exibe "Ata CT-25296-06".

# O ator compara os dados exibidos com os dados anotados.

# O título, a data de criação e o tipo de assembleia são iguais aos
# anotados. Somente o status mudou, de "Oficializada" para
# "Arquivada". [CA02] [RN02]


# 🟣 [RN02] O ARQUIVAMENTO ALTERA SOMENTE O STATUS
# ---------------------------------------------------------------

# Título, data de criação, tipo de assembleia e conteúdo permanecem os
# mesmos após o arquivamento.


# ❓ [Q10] DÚVIDA - CONTEÚDO INTEGRAL DA ATA ARQUIVADA
# ---------------------------------------------------------------

# RN02 também exige que o conteúdo não mude, mas o backlog não define se é
# possível visualizar os detalhes ou exportar (CA 25351) uma Ata arquivada.
# Quando a Q10 for respondida, este cenário deverá incluir a comparação do
# conteúdo da Ata antes e depois do arquivamento.

'''
CT-25296-04 - Ocultar ata arquivada dos filtros por período e por tipo

Objetivo: Verificar que uma Ata arquivada não aparece nos resultados dos
filtros por intervalo de datas e por tipo de assembleia, mesmo quando ela
atende aos critérios desses filtros.

Requisitos:
- RF-25296 (versão corrigida): CA03; RN03
- Origem no backlog: CA 25362
- Relacionado: RF-25294 (CA 25350, US 25353: "mantendo a exclusão das atas
  marcadas como Arquivadas")

Ator:
- Usuário com permissão para visualizar e editar Atas

Autoria:
- Thalyson Felicio de Moura

Pré-condições:
- O ator está autenticado e tem permissão para visualizar e editar Atas.
- Existem duas Atas do tipo "Ordinária", criadas na mesma data:
  - "Ata CT-25296-04-A", com status "Arquivada";
  - "Ata CT-25296-04-B", com status "Oficializada". [Q01]

Dados de teste (fictícios):
- Filtro de tipo: "Ordinária".
- Filtro de período: intervalo que contém a data de criação das duas Atas.

Resultados esperados:
- Filtro por tipo "Ordinária": exibe "Ata CT-25296-04-B" e não exibe
  "Ata CT-25296-04-A".
- Filtro por período: exibe "Ata CT-25296-04-B" e não exibe
  "Ata CT-25296-04-A".

Dúvidas registradas:
- RF-25294 não define qual data o filtro de período usa, se os limites são
  inclusivos, nem se os dois filtros podem ser combinados. Essas dúvidas
  pertencem à Feature 25294. O intervalo dos dados de teste deve conter a
  data com folga para não depender dessas respostas.
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator acessa a listagem de Atas.

# O ator seleciona o tipo de assembleia "Ordinária" no filtro e aplica.

# O sistema exibe "Ata CT-25296-04-B". (CA 25350)

# O sistema não exibe "Ata CT-25296-04-A", embora ela seja do tipo
# "Ordinária". [CA03] [RN03]

# O ator remove o filtro de tipo.

# O ator informa no filtro de período um intervalo que contém a data de
# criação das duas Atas e aplica.

# O sistema exibe "Ata CT-25296-04-B". (CA 25350)

# O sistema não exibe "Ata CT-25296-04-A", embora sua data de criação
# esteja no intervalo. [CA03] [RN03]


# 🟣 [RN03] OCULTAÇÃO DA ATA ARQUIVADA
# ---------------------------------------------------------------

# Uma Ata com status "Arquivada" não é exibida na listagem de Atas nem nos
# resultados dos filtros por intervalo de datas e por tipo de assembleia.

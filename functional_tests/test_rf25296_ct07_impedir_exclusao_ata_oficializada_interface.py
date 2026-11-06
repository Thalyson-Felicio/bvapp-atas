'''
CT-25296-07 - Impedir exclusão definitiva de ata oficializada pela interface

Objetivo: Verificar que um usuário, mesmo com permissão para visualizar e
editar Atas, não consegue excluir definitivamente uma Ata oficializada pela
interface do sistema, e que a Ata continua existindo sem alterações.

Requisitos:
- RF-25296 (versão corrigida): CA01, CA07 (proposta); RN05
- Origem no backlog: CA 25361, US 25364

Ator:
- Usuário com permissão para visualizar e editar Atas (o maior nível de
  acesso descrito para Atas no backlog)

Autoria:
- Thalyson Felicio de Moura

Pré-condições:
- O ator está autenticado e tem permissão para visualizar e editar Atas.
- Existe a Ata "Ata CT-25296-07", com status "Oficializada". [Q01]

Dados de teste (fictícios):
- "Ata CT-25296-07", tipo "Ordinária", status "Oficializada".

Resultados esperados:
- A Ata não é excluída: continua na listagem, com os mesmos título, data de
  criação, tipo de assembleia e status "Oficializada".
- (Proposta CA07) O sistema informa que Atas oficializadas não podem ser
  excluídas. O texto da mensagem não é definido (Q09).

Dúvidas registradas (docs/requisitos/RF-25296-arquivamento-exclusao-atas.md):
- Q01 - Como preparar uma Ata com status "Oficializada".
- Q08 - Se a opção de excluir fica oculta ou é exibida e recusada.
- Q09 - Texto da mensagem de recusa.
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator acessa a listagem de Atas.

# O sistema exibe "Ata CT-25296-07" com status "Oficializada".

# O ator anota o título, a data de criação, o tipo de assembleia e o
# status exibidos.

# O ator seleciona "Ata CT-25296-07" e procura a opção de excluir. [Q08]
# - Se a opção não for exibida, segue para [A1].
# - Se a opção for exibida, o ator a aciona.

# O sistema recusa a exclusão. [CA01] [RN05]

# (Proposta CA07) O sistema informa ao ator que Atas oficializadas não
# podem ser excluídas. [Q09]

# O ator acessa novamente a listagem de Atas.

# O sistema exibe "Ata CT-25296-07" com os mesmos dados anotados e status
# "Oficializada". [CA01]


# 🟠 [A1] - OPÇÃO DE EXCLUIR NÃO EXIBIDA
# ---------------------------------------------------------------

# O sistema não exibe a opção de excluir para "Ata CT-25296-07".

# O ator acessa novamente a listagem de Atas.

# O sistema exibe "Ata CT-25296-07" com os mesmos dados anotados e status
# "Oficializada". [CA01]

# Ocultar a opção não prova que a exclusão é recusada por outros meios;
# isso é verificado em CT-25296-08.


# 🟣 [RN05] PROIBIÇÃO DE EXCLUSÃO DE ATA OFICIALIZADA
# ---------------------------------------------------------------

# Uma Ata com status "Oficializada" não pode ser excluída definitivamente
# por nenhum usuário, por nenhum meio (interface ou requisição direta).


# ❓ [Q08] DÚVIDA - COMPORTAMENTO DA OPÇÃO DE EXCLUIR
# ---------------------------------------------------------------

# O backlog não define se a opção de excluir fica oculta ou se é exibida e
# recusada. Os dois caminhos estão descritos ([FP] e [A1]); o resultado
# obrigatório nos dois é o mesmo: a Ata continua existindo, sem alterações.

'''
CT-25296-08 - Impedir exclusão definitiva de ata oficializada por requisição direta

Objetivo: Verificar que a proibição de exclusão de uma Ata oficializada não
depende apenas da interface: uma solicitação de exclusão enviada diretamente
ao sistema, sem usar as telas, também deve ser recusada.

Requisitos:
- RF-25296 (versão corrigida): CA01; RN05
- Origem no backlog: US 25364 ("bloquear qualquer tentativa de excluir")

Ator:
- Usuário autenticado com permissão para visualizar e editar Atas

Autoria:
- Thalyson Felicio de Moura

Pré-condições:
- O ator está autenticado e tem permissão para visualizar e editar Atas.
- Existe a Ata "Ata CT-25296-08", com status "Oficializada". [Q01]
- A forma de enviar uma solicitação de exclusão diretamente ao sistema
  (endereço e método) foi definida na implementação.

Dados de teste (fictícios):
- "Ata CT-25296-08", tipo "Extraordinária", status "Oficializada".
- Identificador da Ata no sistema: obtido na preparação do teste.

Resultados esperados:
- O sistema recusa a solicitação de exclusão.
- A Ata continua existindo, com os mesmos dados e status "Oficializada".

Dúvidas registradas:
- Q01 - Como preparar uma Ata com status "Oficializada".
- O backlog não define a rota nem o formato da resposta de recusa. O
  resultado esperado se limita a: a Ata continua existindo. O código de
  resposta exato não deve ser presumido.
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator acessa a listagem de Atas e confirma que "Ata CT-25296-08" é
# exibida com status "Oficializada".

# Sem usar as telas do sistema, o ator envia diretamente ao sistema uma
# solicitação de exclusão da Ata "Ata CT-25296-08", usando a sessão
# autenticada.

# O sistema recusa a solicitação. [CA01] [RN05]

# O ator acessa novamente a listagem de Atas.

# O sistema exibe "Ata CT-25296-08" com os mesmos dados e status
# "Oficializada". [CA01]


# 🟠 [A1] - SOLICITAÇÃO SEM AUTENTICAÇÃO
# ---------------------------------------------------------------

# A mesma solicitação de exclusão é enviada sem sessão autenticada.

# O sistema recusa a solicitação.

# A Ata continua existindo, com os mesmos dados. [RN05]


# 🟣 [RN05] PROIBIÇÃO DE EXCLUSÃO DE ATA OFICIALIZADA
# ---------------------------------------------------------------

# Uma Ata com status "Oficializada" não pode ser excluída definitivamente
# por nenhum usuário, por nenhum meio (interface ou requisição direta).

'''
CT-25296-10 - Registrar o arquivamento no log de auditoria

Objetivo: Verificar que o arquivamento de uma Ata gera um registro no log de
auditoria com o usuário responsável, a data/hora, a ação realizada e a Ata
afetada.

Requisitos:
- RF-25296 (versão corrigida): CA06; RN07
- Origem no backlog: RF-25310 (CA 25408, CA 25409, CA 25411)

Ator:
- Usuário A: permissão para visualizar e editar Atas (realiza o
  arquivamento).
- Usuário B: perfil de nível Administrativo/Diretoria (consulta o log,
  conforme CA 25411).

Autoria:
- Thalyson Felicio de Moura

Pré-condições:
- Existe a Ata "Ata CT-25296-10", com status "Oficializada". [Q01]
- A tela de visualização de logs (RF-25310) está disponível.

Dados de teste (fictícios):
- "Ata CT-25296-10", tipo "Ordinária", status "Oficializada".
- Nome do Usuário A: conhecido na preparação.
- Horário do arquivamento: anotado pelo ator no momento da ação.

Resultados esperados:
- O log contém um registro com:
  - nome do usuário responsável: Usuário A;
  - data/hora: compatível com o horário anotado;
  - ação: arquivamento;
  - documento afetado: "Ata CT-25296-10".

Dúvidas registradas:
- Q01 - Como preparar uma Ata com status "Oficializada".
- RF-25310 não define o formato da data/hora, o fuso horário nem a
  tolerância de comparação. O teste não deve presumir esses valores
  (mesmo cuidado indicado na Aula 06 para a auditoria de RF001).
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O Usuário A acessa a listagem de Atas.

# O Usuário A arquiva "Ata CT-25296-10" (conforme CT-25296-02) e anota o
# horário da ação.

# O Usuário B acessa a tela de visualização de logs. (CA 25411)

# O sistema exibe um registro referente ao arquivamento de
# "Ata CT-25296-10". [CA06] [RN07]

# O Usuário B verifica que o registro contém o nome do Usuário A, a data e
# hora da ação, a ação "arquivamento" e a identificação de
# "Ata CT-25296-10". (CA 25409)


# 🟠 [A1] - REGISTRO SOMENTE LEITURA
# ---------------------------------------------------------------

# O Usuário B procura uma opção para editar ou excluir o registro.

# O sistema não permite editar nem excluir o registro. (CA 25410)


# 🟣 [RN07] AUDITORIA DO ARQUIVAMENTO
# ---------------------------------------------------------------

# Todo arquivamento deve ser registrado no log de auditoria, com nome do
# usuário responsável, data/hora, ação realizada e Ata afetada.

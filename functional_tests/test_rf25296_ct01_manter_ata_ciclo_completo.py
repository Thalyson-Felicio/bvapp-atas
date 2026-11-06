'''
CT-25296-01 - Manter ata: ciclo completo (criar, consultar, atualizar e arquivar)

Objetivo: Verificar o ciclo completo de manutenção de uma Ata, com as quatro
operações no mesmo fluxo: criar a Ata, consultá-la na listagem, atualizá-la
e retirá-la de circulação. Neste módulo a "exclusão" de uma Ata oficializada
é proibida (RN05), por isso a retirada é feita pelo arquivamento, e a
tentativa de exclusão definitiva é verificada como fluxo alternativo.

Requisitos:
- RF-25296 (versão corrigida): CA01, CA02, CA03, CA04; RN02, RN03, RN04, RN05
- Contexto das demais operações do CRUD (Features de outros integrantes):
  - Criar:     RF-25293 (CA 25341, CA 25342, CA 25343)
  - Consultar: RF-25294 (CA 25349)
  - Atualizar: RF-25295 (CA 25355, CA 25356, CA 25357)

Ator:
- Usuário com permissão para escrever, visualizar e editar Atas (Q11)

Autoria:
- Thalyson Felicio de Moura

Pré-condições:
- Existe um modelo de Ata cadastrado com status "Ativo" (RF-25292).
- O ator está autenticado no sistema.

Dados de teste (fictícios):
- Modelo de Ata: um modelo com status "Ativo" e suas variáveis obrigatórias.
- Título da Ata: "Ata CT-25296-01"
- Tipo de assembleia: "Ordinária"

Resultados esperados:
- Criar: a Ata é salva e aparece na listagem com título, data de criação,
  tipo de assembleia e status.
- Atualizar: a versão anterior é preservada e o número da versão atual é
  exibido.
- Arquivar: o status passa a "Arquivada" e a Ata some da listagem.
- Consultar arquivada: a Ata aparece ao selecionar o status "Arquivada" no
  filtro de busca avançada, com os mesmos título, data e tipo.
- Excluir: a exclusão definitiva da Ata oficializada é recusada e a Ata
  continua existindo.

Dúvidas registradas (docs/requisitos/RF-25296-arquivamento-exclusao-atas.md):
- Q01 - Como a Ata passa ao status "Oficializada".
- Q03 - Quais Atas podem ser arquivadas.
- Q04 - Se a proibição de exclusão continua depois do arquivamento.
- Q11 - Perfil x permissão para escrever, editar e arquivar.
- Q12 - Existência do filtro de status em RF-25294.
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# --- CRIAR (RF-25293) ---

# O ator acessa a página de Atas e escolhe criar uma nova Ata.

# O ator seleciona um modelo de Ata com status "Ativo".

# O sistema exibe um formulário com os campos correspondentes às
# variáveis do modelo selecionado. (CA 25342)

# O ator preenche todas as variáveis obrigatórias e o conteúdo da Ata,
# usando os dados de teste, e confirma o salvamento.

# O sistema salva a Ata. (CA 25343)
# [Obs.] RF-25293 não define como o título e o tipo de assembleia da Ata
# são informados. Essa dúvida pertence à Feature 25293.

# --- CONSULTAR (RF-25294) ---

# O ator acessa a listagem de Atas.

# O sistema exibe a Ata "Ata CT-25296-01" com título, data de criação,
# tipo de assembleia "Ordinária" e status. (CA 25349)

# --- ATUALIZAR (RF-25295) ---

# O ator seleciona a Ata "Ata CT-25296-01" e aciona a opção de editar.

# O sistema exibe a Ata para edição.

# O ator altera o conteúdo da Ata e confirma o salvamento.

# O sistema preserva a versão anterior, gera uma nova versão e exibe o
# número da versão atual. (CA 25356, CA 25357)
# [Obs.] CA 25357 apenas exemplifica a numeração (v1.0, v1.1); a regra de
# incremento não é definida. O teste deve verificar que o número exibido
# mudou, sem presumir um valor.

# --- OFICIALIZAR (pré-condição do arquivamento) ---

# A Ata passa ao status "Oficializada". [Q01]
# O backlog não define como isso acontece. Na execução, a preparação
# deverá usar o procedimento definido como resposta à Q01.

# --- ARQUIVAR (RF-25296) ---

# O ator localiza a Ata "Ata CT-25296-01" na listagem de Atas e aciona a
# opção de arquivar. [RN01] [Q03]

# O sistema altera o status da Ata para "Arquivada". [CA02] [RN02]

# O ator acessa novamente a listagem de Atas.

# O sistema não exibe a Ata "Ata CT-25296-01". [CA03] [RN03]

# O ator seleciona o status "Arquivada" no filtro de busca avançada. [Q12]

# O sistema exibe a Ata "Ata CT-25296-01" com o mesmo título, a mesma data
# de criação, o tipo "Ordinária" e o status "Arquivada". [CA04] [RN04]

# O ator verifica que o ciclo terminou: a Ata saiu da listagem, mas
# continua disponível para consulta. [A1]


# 🟠 [A1] - TENTAR EXCLUIR DEFINITIVAMENTE A ATA OFICIALIZADA
# ---------------------------------------------------------------

# Antes de arquivar, com a Ata no status "Oficializada", o ator tenta
# excluí-la definitivamente.

# O sistema recusa a exclusão. [CA01] [RN05]

# O ator acessa a listagem de Atas.

# O sistema continua exibindo a Ata "Ata CT-25296-01" com o mesmo status
# e os mesmos dados.

# O detalhamento deste fluxo está em CT-25296-07 (interface) e
# CT-25296-08 (requisição direta).


# 🟣 [RN05] PROIBIÇÃO DE EXCLUSÃO DE ATA OFICIALIZADA
# ---------------------------------------------------------------

# Uma Ata com status "Oficializada" não pode ser excluída definitivamente
# por nenhum usuário, por nenhum meio.

# 🟣 [RN02] O ARQUIVAMENTO ALTERA SOMENTE O STATUS
# ---------------------------------------------------------------

# Título, data de criação, tipo de assembleia e conteúdo permanecem os
# mesmos após o arquivamento.


# ❓ [Q04] DÚVIDA - EXCLUSÃO APÓS O ARQUIVAMENTO
# ---------------------------------------------------------------

# Após o arquivamento, o status deixa de ser "Oficializada". A proposta
# RN06 mantém a proibição de exclusão, mas ainda não foi validada.
# Por isso, este cenário não verifica a exclusão depois do arquivamento
# (ver CT-25296-11).

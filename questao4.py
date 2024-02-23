"""4. Atualização e Remoção
a) Atualize a idade de um aluno específico na tabela.
b) Remova um aluno pelo seu ID.
"""

import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

#A

#B

conexao.commit()
conexao.close
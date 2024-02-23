"""4. Atualização e Remoção
a) Atualize a idade de um aluno específico na tabela.
b) Remova um aluno pelo seu ID.
"""
import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

#A
cursor.execute('UPDATE alunos SET idade=28 WHERE id=1')

#B
cursor.execute('DELETE FROM alunos WHERE id=1')

conexao.commit()
conexao.close
"""
3. Consultas Básicas
Escreva consultas SQL para realizar as seguintes tarefas:
a) Selecionar todos os registros da tabela "alunos".
b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
c) Selecionar os alunos do curso de "Engenharia" em ordem
alfabética.
d) Contar o número total de alunos na tabela
"""

import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

#A
dados = cursor.execute('SELECT * FROM alunos')
for alunos in dados:
	print(alunos)

#B
maior20 = cursor.execute('SELECT nome,idade FROM alunos WHERE idade>20')
for alunos in maior20:
	print(alunos)

#C
engenhariaASC = cursor.execute('SELECT * FROM alunos WHERE curso="Engenharia" ORDER BY nome ASC')
for alunos in engenhariaASC:
	print(alunos)

#D
totalAlunos = cursor.execute('SELECT COUNT(*) FROM alunos')
for alunos in totalAlunos:
	print(alunos)

conexao.commit()
conexao.close
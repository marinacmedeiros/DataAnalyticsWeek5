"""
6. Consultas e Funções Agregadas
Escreva consultas SQL para realizar as seguintes tarefas:
a) Selecione o nome e a idade dos clientes com idade superior a
30 anos.
b) Calcule o saldo médio dos clientes.
c) Encontre o cliente com o saldo máximo.
d) Conte quantos clientes têm saldo acima de 1000.
"""

import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

#A
maior30 = cursor.execute('SELECT nome,idade FROM clientes GROUP BY idade HAVING idade>30')
for clientes in maior30:
	print(clientes)

#B
saldoMedio = cursor.execute('SELECT AVG(saldo) FROM clientes')
for clientes in saldoMedio:
	print(clientes)

#C
saldoMax = cursor.execute('SELECT nome,MAX(saldo) FROM clientes')
for clientes in saldoMax:
	print(clientes)

#D
saldoAcima1000 = cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo>1000')
for clientes in saldoAcima1000:
	print(clientes)

conexao.commit()
conexao.close
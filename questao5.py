"""
5. Criar uma Tabela e Inserir Dados
Crie uma tabela chamada "clientes" com os campos: id (chave
primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns registros de clientes na tabela.
"""

import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

cursor.execute('CREATE TABLE clientes(id INT PRIMARY KEY, nome VARCHAR(100), idade INT, saldo FLOAT);')

add_clientes = [
	('1', 'João', 25, 1000.0),
	('2', 'Maria', 30, 1500.0),
	('3', 'Pedro', 35, 2000.0),
	('4', 'Ana', 28, 1800.0),
	('5', 'Carlos', 40, 2200.0),
	('6', 'Mariana', 33, 1900.0),
	('7', 'Lucas', 27, 1600.0),
	('8', 'Julia', 22, 1300.0),
	('9', 'Fernando', 45, 2500.0),
	('10', 'Camila', 31, 1700.0),
	('11', 'Rafael', 29, 2000.0),
	('12', 'Patricia', 36, 2100.0)
]

cursor.executemany('INSERT INTO clientes VALUES(?,?,?,?)', add_clientes)

conexao.commit()
conexao.close
"""
7. Atualização e Remoção com Condições
a) Atualize o saldo de um cliente específico.
b) Remova um cliente pelo seu ID.
"""

import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

#A
cursor.execute('UPDATE clientes SET saldo=2000 WHERE id=1')

#B
cursor.execute('DELETE FROM clientes WHERE id=1')


conexao.commit()
conexao.close
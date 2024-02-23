"""
8. Junção de Tabelas
Crie uma segunda tabela chamada "compras" com os campos: id
(chave primária), cliente_id (chave estrangeira referenciando o id da tabela "clientes"), produto (texto) e valor (real).

Insira algumas compras associadas a clientes existentes na tabela "clientes".

Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.
"""

import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

cursor.execute('CREATE TABLE compras(id INT PRIMARY KEY, cliente_id INT, produto VARCHAR(100), valor FLOAT, FOREIGN KEY(cliente_id) REFERENCES clientes(id));')

add_compras = [
	(1, 2, 'Laptops', 1500.0),
	(2, 3, 'Camisetas', 20.0),
	(3, 4, 'Livros', 30.0),
	(4, 5, 'Tênis', 100.0)
]

insert_query = "INSERT INTO compras (id, cliente_id, produto, valor) VALUES (?, ?, ?, ?)"

cursor.executemany(insert_query, add_compras)

cursor.execute('SELECT clientes.nome, compras.produto, compras.valor FROM clientes INNER JOIN compras ON clientes.id = compras.cliente_id')

conexao.commit()
conexao.close()
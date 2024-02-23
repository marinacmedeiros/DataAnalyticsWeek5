#Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.

import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(1, "MARIA", 22, "Arquitetura")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(2, "CARLA", 25, "Matemática")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(3, "JOANA", 45, "ADS")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(4, "ISADORA", 65, "Medicina")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(5, "MOANA", 33, "Direito")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(6, "CÁTIA", 18, "Engenharia")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(7, "ISABELA", 19, "Engenharia")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(8, "MÁRCIA", 34, "Engenharia")')

conexao.commit()
conexao.close
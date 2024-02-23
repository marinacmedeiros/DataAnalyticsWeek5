#

import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()


conexao.commit()
conexao.close
import sqlite3

#cria banco de dados
conn = sqlite3.connect('aulaDB.db')
print(type(conn))

#Cria tabela no banco, pois está dentro da mesma conexão

ddl_create = """

CREATE TABLE fornecedor (
    id_fornecedor INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome_fornecedor TEXT NOT NULL
    cnpj VARCHAR(18) NOT NULL,
    cidade TEXT,
    estado VARCHAR(2) NOT NULL,
    cep VARCHAR(9) NOT NULL,
    data_cadastro DATE NOT NULL,
"""
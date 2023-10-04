import sqlite3
#Criação da função para conectar ao banco de dados
def conectar():
    try:
        global conn
        conn = sqlite3.connect("cadastro.db")
        print("Conexão realizada com sucesso!")
    except sqlite3.Error as erro:
        print("Erro de Conexão")
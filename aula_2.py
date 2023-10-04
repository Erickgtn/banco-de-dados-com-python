import sqlite3

conn = sqlite3.connect("aula2.db")

""" conn.execute('''
CREATE table aluno(
  nome string,
  sobrenome string,
  idade integer
)
''') """

nome = input("Informe seu nome: ")
sobrenome = input("Informe seu sobrenome: ")
idade = int(input("Informe sua idade: "))

conn.execute("INSERT INTO aluno VALUES ('"+nome+"','"+sobrenome+"','"+str(idade)+"')")

conn.commit()
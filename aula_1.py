import sqlite3

conn = sqlite3.connect("aula.db")

""" conn.execute('''
CREATE table aluno(
  id integer PRIMARY KEY AUTOINCREMENT,
  nome string,
  sobrenome string,
  idade integer
)
''') """



conn.execute('''insert INTO aluno values(1, "Euler", "Sampaio", 33)''')
conn.commit()

cursor = conn.execute('''select * from aluno''')

print(cursor.fetchall())
""" for row in cursor:
  print(row) """
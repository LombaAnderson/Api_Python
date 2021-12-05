import sqlite3

# empregados = [

#   {'nome': 'Anderson', 'cargo': 'Desenvolvedor', 'salario': 6000},
#   {'nome': 'Filipe', 'cargo': 'Analista', 'salario': 5000},
#   {'nome': 'Liciane', 'cargo': 'Analista', 'salario': 5000}
#  ]

conn = sqlite3.connect('entreprise.db')

cursor = conn.cursor()

cursor.execute("""
            CREATE TABLE empregados(
               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               cargo TEXT,
               salario REAL
             );
""")

print("Tabela criada com sucesso!")

# Desconecção do banco de dados
conn.close()

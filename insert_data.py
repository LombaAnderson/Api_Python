import sqlite3

empregados = [

    {'nome': 'Anderson', 'cargo': 'Desenvolvedor', 'salario': 6000},
    {'nome': 'Filipe', 'cargo': 'Analista', 'salario': 5000},
    {'nome': 'Liciane', 'cargo': 'Analista', 'salario': 5000}
]

conn = sqlite3.connect('entreprise.db')

cursor = conn.cursor()

for empregado in empregados:
 cursor.execute(""" 
            INSERT INTO empregados (nome, cargo, salario)
            VALUES (?, ?, ?)
       """, (empregado['nome'], empregado['cargo'], empregado['salario']))

print("Dados inseridos com sucesso!")

conn.commit()
conn.close()

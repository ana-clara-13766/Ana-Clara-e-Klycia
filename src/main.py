import mysql.connector

banco = mysql.connector.connect(
    host="10.30.29.183",
    port=3309,
    user="root",
    password="root123",
    database="Ana_Clara"
)

cursor = banco.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS anaclara_klycia")

# cursor.execute("CREATE TABLE USUARIO(id INT, username VARCHAR(255), email VARCHAR(50), senha VARCHAR(100), idade INT)")
id_INT = int(input("id"))
username = input("username")
email = input("email")
senha = input("senha")
idade = int(input("idade"))
cursor.execute(f"INSERT INTO USUARIO VALUES ({id_INT}, '{username}', '{email}', '{senha}', {idade})")
banco.commit()
cursor.execute("SELECT * FROM USUARIO")

dados = cursor.fetchall()

# 5. Mostrar os dados
for linha in dados:
    print(linha)
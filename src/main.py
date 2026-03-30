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

cursor.execute("CREATE TABLE USUARIO(id INT, username VARCHAR(255), email VARCHAR(50), senha VARCHAR(100), idade INT.)")
id_INT = int(input("id"))
username = int(input("username"))
email = int(input("email"))
senha = int(input("senha"))
idade = int(input("idade"))
cursor.execute(f"INSERT INTO USUARIO VALUES ({id}, {username}, {email}, {senha}, {idade})")
banco.commit()
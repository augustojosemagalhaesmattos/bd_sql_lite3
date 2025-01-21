from operacoes_passagens.funcoes import adicionar_passagem, listar_passagens, atualizar_passagem, excluir_passagens, adicionar_passageiro
import sqlite3

# conn: variavel para conexão com o banco de dados
conn = sqlite3.connect("C:/python_sql/bd_sql_lite3/passagens_02/passagens.db")
# Ele é um objeto, uma ferramenta, permitindo vc executar comandos sql
cursor = conn.cursor()



cursor.execute('''
    CREATE TABLE IF NOT EXISTS passageiros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
    )
''')
cursor.execute('DROP TABLE IF EXISTS passagens')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS passagens (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        numero_voo TEXT NOT NULL,
        destino TEXT NOT NULL,
        data_hora TEXT NOT NULL,
        preco REAL NOT NULL,
        assento TEXT,
        passageiro_id INTEGER,
        FOREIGN KEY (passageiro_id) REFERENCES passageiros(id)
    )
''')


while True:
    print('-'*70)
    print("Menu de opções: ")
    print('-'*70)

    print("1. Adicionar Passageiro")
    print("2. Adicionar Passagem")
    print("3. Listar Passagens")
    print("4. Atualizar Passagens")
    print("5. Excluir Passagem ")
    print("6. Sair")
    print('-'*70)
    
    opcao = input("Escolha uma opção (1-6): ")
    
    if opcao == "1":
        adicionar_passageiro()  
    elif opcao == "2":
        adicionar_passagem()  
    elif opcao == "3":
        listar_passagens() 
    elif opcao == "4":
        atualizar_passagem()  
    elif opcao == "5":
        excluir_passagens()  
    elif opcao == "6":
        print("Saída feita com sucesso!") 
        break

conn.commit()
conn.close()

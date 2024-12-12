from operacoes_passagens.funcoes import adicionar_passagem, listar_passagens, atualizar_passagem, excluir_passagens
import sqlite3


conn = sqlite3.connect("C:/python/passagens/novo_reposi_sql/atividade_01/passagens.db")
cursor = conn.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS passagens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_passageiro TEXT NOT NULL,
            numero_voo TEXT NOT NULL,
            destino TEXT NOT NULL,
            data_hora TEXT NOT NULL,
            preco REAL NOT NULL,
            assento TEXT   
    )
''')

while True:
    print('-'*70)
    print("Menu de opções: ")
    print('-'*70)

    print("1. Adicionar Passagem")
    print("2. Listar Passagens")
    print("3. Atualizar Passagens")
    print("4. Excluir Passagem ")
    print("5. Sair")
    print('-'*70)
    
    opcao = input("Escolha uma opção (1-5): ")
    if opcao == "1":
        adicionar_passagem()
        
    elif opcao == "2":
        listar_passagens()
        
    elif opcao == "3":
        
        atualizar_passagem()
        
    elif opcao == "4":
        
        excluir_passagens()
        
    elif opcao == "5":
        print("Saida feita com sucesso!") 
        
        break

conn.commit()
conn.close()
        
        
        

    

        
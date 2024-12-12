import sqlite3
from prettytable import PrettyTable

conn = sqlite3.connect("C:/python/passagens/novo_reposi_sql/atividade_01/passagens.db")
cursor = conn.cursor()

def adicionar_passagem():

    nome = input("Nome do Passageiro: ").capitalize()
    numero_voo = input("Número do Voo: ")
    destino = input("Destino: ").capitalize()
    data_hora = input("Data e Hora da Viagem: ")
    preco = float(input("Preço do Bilhete: "))
    assento = input("Assento: ")
   
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO passagens (nome_passageiro, numero_voo, destino, data_hora, preco, assento)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (nome, numero_voo, destino, data_hora, preco, assento) )
    conn.commit()

def listar_passagens():

    conn = sqlite3.connect("C:/python/passagens/novo_reposi_sql/atividade_01/passagens.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM passagens")
    passagens = cursor.fetchall()
    

    # Cria a tabela Prettytable e define os nomes das colunas
    tabela = PrettyTable()
    # Obtém os nomes das colunas a partir de cursor.description
    colunas = [descricao[0] for descricao in cursor.description]
    # Define os nomes das colunas na tabela PrettyTable
    tabela.field_names = colunas

    # Adiciona as linhas à tabela
    for row in passagens:
        tabela.add_row(row)

    print(tabela)
    conn.commit()
    conn.close()

def atualizar_passagem():
    
    id_passagem = int(input("ID da Passagem: "))
    novo_destino = input("Novo Destino: ").capitalize()
    nova_data_hora = input("Nova Data e Hora: ")
    novo_nome = input("Novo Nome: ").capitalize()
    novo_numero_voo = input("Novo Numero do Voo: ")
    novo_assento = input("Novo Assento: ")
    
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE passagens
        SET destino = ?, data_hora = ?, nome_passageiro = ?, numero_voo = ?, assento = ?
        WHERE id = ?
    ''', (novo_destino, nova_data_hora, novo_nome, novo_numero_voo, novo_assento, id_passagem))

    print("✈️Atualizado com sucesso!✈️")

    conn.commit()

def excluir_passagens():

    exclusao = int(input("Digite o ID da passagens para excluir: "))

    cursor = conn.cursor()
    cursor.execute('DELETE FROM passagens WHERE id = ?',(exclusao,))
    conn.commit()
    print(f"Passagem com ID '{exclusao}' excluída com sucesso!")
    
      


   

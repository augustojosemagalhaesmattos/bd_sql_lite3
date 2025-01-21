import sqlite3
from prettytable import PrettyTable

# Conexão global com o banco de dados
conn = sqlite3.connect("C:/python_sql/bd_sql_lite3/passagens_02/passagens.db")
cursor = conn.cursor()

# Função para adicionar um passageiro
def adicionar_passageiro():
    nome = input("Nome do Passageiro: ").capitalize()
    cursor.execute('''
        INSERT INTO passageiros (nome)
        VALUES (?)
    ''', (nome,))
    conn.commit()
    print("🛫 Passageiro adicionado com sucesso!")

# Função para adicionar uma passagem
def adicionar_passagem():
    cursor.execute("SELECT * FROM passageiros")
    passageiros = cursor.fetchall()

    # Listar passageiros disponíveis
    print("Passageiros cadastrados:")
    for passageiro in passageiros:
        print(f"{passageiro[0]} - {passageiro[1]}")

    passageiro_id = int(input("ID do Passageiro: "))
    numero_voo = input("Número do Voo: ")
    destino = input("Destino: ").capitalize()
    data_hora = input("Data e Hora da Viagem: ")
    preco = float(input("Preço do Bilhete: "))
    assento = input("Assento: ")

    cursor.execute('''
        INSERT INTO passagens (numero_voo, destino, data_hora, preco, assento, passageiro_id)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (numero_voo, destino, data_hora, preco, assento, passageiro_id))
    conn.commit()
    print("🛫 Passagem adicionada com sucesso!")

# Função para listar todas as passagens
def listar_passagens():
    cursor.execute('''
        SELECT passagens.id, passageiros.nome, passagens.numero_voo, passagens.destino, passagens.data_hora, passagens.preco, passagens.assento
        FROM passagens
        INNER JOIN passageiros ON passagens.passageiro_id = passageiros.id
    ''')
    passagens = cursor.fetchall()

    # Cria a tabela PrettyTable e define os nomes das colunas
    tabela = PrettyTable()
    tabela.field_names = ["ID", "Passageiro", "Número do Voo", "Destino", "Data e Hora", "Preço", "Assento"]

    # Adiciona as linhas à tabela
    for row in passagens:
        tabela.add_row(row)

    print(tabela)

# Função para atualizar uma passagem
def atualizar_passagem():
    id_passagem = int(input("ID da Passagem: "))
    novo_destino = input("Novo Destino: ").capitalize()
    nova_data_hora = input("Nova Data e Hora: ")
    novo_numero_voo = input("Novo Número do Voo: ")
    novo_assento = input("Novo Assento: ")

    cursor.execute('''
        UPDATE passagens
        SET destino = ?, data_hora = ?, numero_voo = ?, assento = ?
        WHERE id = ?
    ''', (novo_destino, nova_data_hora, novo_numero_voo, novo_assento, id_passagem))

    print("✈️ Passagem atualizada com sucesso!")
    conn.commit()

# Função para excluir uma passagem
def excluir_passagens():
    exclusao = int(input("Digite o ID da passagem para excluir: "))
    cursor.execute('DELETE FROM passagens WHERE id = ?', (exclusao,))
    conn.commit()

    print(f"✈️ Passagem com ID '{exclusao}' excluída com sucesso!")

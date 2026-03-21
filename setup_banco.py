import sqlite3

def criar_banco():
    # 1. Cria a conexão e o arquivo do banco de dados na sua pasta
    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()

    # 2. Tabela de Café (Estoque, Entradas e Vendas)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cafe (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT,
            tipo_movimento TEXT, 
            variedade TEXT,
            quantidade REAL,
            preco_total REAL,
            conta_depositada TEXT,
            dia_deposito TEXT
        )
    ''')

    # 3. Tabela de Colheita
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS colheita (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data_inicio TEXT,
            quantidade_colhida REAL,
            tipo_colheita TEXT, 
            custo_operacao REAL
        )
    ''')

    # 4. Tabela de Despesas Gerais (Insumos, Manutenção, Fixas, Benfeitorias)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS despesas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT,
            categoria TEXT, 
            descricao TEXT,
            valor_total REAL,
            status_obra TEXT 
        )
    ''')

    # 5. Tabela de Pessoal (RH - Fixos e Temporários)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pessoal (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT,
            nome_funcionario TEXT,
            tipo_contrato TEXT, 
            atividade_realizada TEXT,
            valor_pago REAL
        )
    ''')

    # 6. Tabela de Pecuária
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pecuaria (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT,
            tipo_movimento TEXT, 
            quantidade_cabecas INTEGER,
            arroba_dia REAL,
            arroba_negociada REAL,
            valor_total REAL,
            destino_motivo TEXT
        )
    ''')

    # 7. Tabela de Usuários (Para o login do seu primo)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT UNIQUE,
            senha TEXT
        )
    ''')

    # 8. Salva tudo e fecha a porta do banco
    conexao.commit()
    conexao.close()
    print("Sucesso! O arquivo 'banco.db' e todas as tabelas foram criados.")

if __name__ == '__main__':
    criar_banco()
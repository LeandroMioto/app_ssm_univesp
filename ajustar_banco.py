import sqlite3

def atualizar_tabela_usuarios():
    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()
    
    # Adicionamos a coluna 'nivel' na tabela que já existe
    try:
        cursor.execute('ALTER TABLE usuarios ADD COLUMN nivel TEXT DEFAULT "operador"')
        print("Coluna 'nivel' adicionada com sucesso!")
    except sqlite3.OperationalError:
        print("A coluna já existe ou o banco está travado.")

    # Agora vamos dar o poder de 'admin' para você e para o seu primo
    cursor.execute('UPDATE usuarios SET nivel = "admin" WHERE usuario IN ("leandro", "primo")')
    
    conexao.commit()
    conexao.close()
    print("Permissões de Administrador configuradas!")

if __name__ == '__main__':
    atualizar_tabela_usuarios()
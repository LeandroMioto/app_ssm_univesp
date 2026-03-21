import sqlite3

def criar_usuarios_iniciais():
    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()
    
    # Vamos cadastrar dois usuários de teste
    # Em um sistema real, usaríamos senhas criptografadas, mas vamos simplificar agora
    usuarios = [
        ('leandro', '1234'),
        ('primo', 'sitio2026')
    ]
    
    cursor.executemany('INSERT INTO usuarios (usuario, senha) VALUES (?, ?)', usuarios)
    
    conexao.commit()
    conexao.close()
    print("Usuários criados com sucesso! Agora você já pode logar.")

if __name__ == '__main__':
    criar_usuarios_iniciais()
from flask import Flask, render_template, request, redirect, url_for, session, abort
import sqlite3

app = Flask(__name__)
app.secret_key = 'sitio_sao_marcos_2026_segredo' 

def conectar_banco():
    conexao = sqlite3.connect('banco.db')
    conexao.row_factory = sqlite3.Row
    return conexao

def verificar_admin():
    if session.get('nivel') != 'admin':
        abort(403)

# --- ACESSO ---
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        db = conectar_banco()
        user = db.execute('SELECT * FROM usuarios WHERE usuario = ? AND senha = ?', 
                         (request.form['usuario'], request.form['senha'])).fetchone()
        db.close()
        if user:
            session['usuario'] = user['usuario']
            session['nivel'] = user['nivel']
            return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/')
def index():
    if 'usuario' not in session: return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/relatorios')
def relatorios_hub():
    verificar_admin()
    return render_template('central_relatorios.html')

# --- LANÇAMENTOS (TODOS) ---
@app.route('/vendas', methods=['GET', 'POST'])
def vendas():
    if 'usuario' not in session: return redirect(url_for('login'))
    mensagem = ""
    if request.method == 'POST':
        db = conectar_banco()
        db.execute('INSERT INTO cafe (data, tipo_movimento, variedade, quantidade, preco_total) VALUES (?, ?, ?, ?, ?)',
                   (request.form['data_venda'], 'Venda', request.form['variedade'], request.form['quantidade'], request.form['valor_total']))
        db.commit()
        db.close()
        mensagem = "Venda salva!"
    return render_template('vendas.html', mensagem=mensagem)

@app.route('/despesas', methods=['GET', 'POST'])
def despesas():
    if 'usuario' not in session: return redirect(url_for('login'))
    mensagem = ""
    if request.method == 'POST':
        db = conectar_banco()
        db.execute('INSERT INTO despesas (data, categoria, descricao, valor_total) VALUES (?, ?, ?, ?)',
                   (request.form['data'], request.form['categoria'], request.form['descricao'], request.form['valor_total']))
        db.commit()
        db.close()
        mensagem = "Despesa registrada!"
    return render_template('despesas.html', mensagem=mensagem)

@app.route('/pecuaria', methods=['GET', 'POST'])
def pecuaria():
    if 'usuario' not in session: return redirect(url_for('login'))
    mensagem = ""
    if request.method == 'POST':
        db = conectar_banco()
        db.execute('INSERT INTO pecuaria (data, tipo_movimento, quantidade_cabecas, arroba_dia, valor_total, destino_motivo) VALUES (?, ?, ?, ?, ?, ?)',
                   (request.form['data'], request.form['tipo_movimento'], request.form['quantidade_cabecas'], request.form.get('arroba_dia', 0), request.form.get('valor_total', 0), request.form.get('destino_motivo', '')))
        db.commit()
        db.close()
        mensagem = "Gado registrado!"
    return render_template('pecuaria.html', mensagem=mensagem)

@app.route('/pessoal', methods=['GET', 'POST'])
def pessoal():
    if 'usuario' not in session: return redirect(url_for('login'))
    mensagem = ""
    if request.method == 'POST':
        db = conectar_banco()
        db.execute('INSERT INTO pessoal (data, nome_funcionario, tipo_contrato, atividade_realizada, valor_pago) VALUES (?, ?, ?, ?, ?)',
                   (request.form['data'], request.form['nome_funcionario'], request.form['tipo_contrato'], request.form['atividade_realizada'], request.form['valor_pago']))
        db.commit()
        db.close()
        mensagem = "Pagamento salvo!"
    return render_template('pessoal.html', mensagem=mensagem)

# --- RELATÓRIOS (ADMIN) ---
@app.route('/relatorio_vendas')
def relatorio_vendas():
    verificar_admin()
    vendas = conectar_banco().execute('SELECT * FROM cafe ORDER BY data DESC').fetchall()
    return render_template('relatorio_vendas.html', vendas=vendas)

@app.route('/relatorio_despesas')
def relatorio_despesas():
    verificar_admin()
    despesas = conectar_banco().execute('SELECT * FROM despesas ORDER BY data DESC').fetchall()
    return render_template('relatorio_despesas.html', despesas=despesas)

@app.route('/relatorio_pecuaria')
def relatorio_pecuaria():
    verificar_admin()
    pecuaria = conectar_banco().execute('SELECT * FROM pecuaria ORDER BY data DESC').fetchall()
    return render_template('relatorio_pecuaria.html', pecuaria=pecuaria)

@app.route('/relatorio_pessoal')
def relatorio_pessoal():
    verificar_admin()
    pessoal = conectar_banco().execute('SELECT rowid as id, * FROM pessoal ORDER BY data DESC').fetchall()
    return render_template('relatorio_pessoal.html', pessoal=pessoal)

@app.route('/gerar_recibo/<int:id>')
def gerar_recibo(id):
    verificar_admin()
    dado = conectar_banco().execute('SELECT * FROM pessoal WHERE rowid = ?', (id,)).fetchone()
    return render_template('recibo.html', dado=dado)

@app.route('/usuarios', methods=['GET', 'POST'])
def gerenciar_usuarios():
    verificar_admin()
    db = conectar_banco()
    if request.method == 'POST':
        db.execute('INSERT INTO usuarios (usuario, senha, nivel) VALUES (?, ?, ?)',
                   (request.form['novo_user'], request.form['nova_senha'], request.form['novo_nivel']))
        db.commit()
    lista = db.execute('SELECT * FROM usuarios').fetchall()
    db.close()
    return render_template('usuarios.html', usuarios=lista)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
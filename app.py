from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def conectar_banco():
    conexao = sqlite3.connect('banco.db')
    conexao.row_factory = sqlite3.Row 
    return conexao

def iniciar_banco():
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM leads ORDER BY id DESC')
    todos_leads = cursor.fetchall()
    conn.close()
    return render_template('index.html', leads=todos_leads)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    nome = request.form.get('nome')
    email = request.form.get('email')
    telefone = request.form.get('telefone')
    
    if nome and email:
        conn = conectar_banco()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO leads (nome, email, telefone) VALUES (?, ?, ?)', (nome, email, telefone))
        conn.commit()
        conn.close()
        
    return redirect(url_for('index'))

@app.route('/deletar/<int:id>')
def deletar(id):
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM leads WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    iniciar_banco()
    app.run(debug=True)
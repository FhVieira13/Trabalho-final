from flask import Flask, render_template, redirect, request, session, url_for
from data import times, jogos, classificacao, elencos

app = Flask(__name__)
app.secret_key = 'chave_secreta'

@app.route('/')
def home():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    return redirect(url_for('ver_classificacao'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['usuario'] == 'admin' and request.form['senha'] == 'admin':
            session['usuario'] = request.form['usuario']
            return redirect(url_for('home'))
        else:
            return render_template('login.html', erro='Usuário ou senha inválido')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('login'))

@app.route('/classificacao')
def ver_classificacao():
    return render_template('classificacao.html', classificacao=classificacao)

@app.route('/jogos')
def ver_jogos():
    return render_template('jogos.html', jogos=jogos)

@app.route('/times')
def ver_times():
    return render_template('times.html', times=times)

@app.route('/elenco/<nome_time>')
def ver_elenco(nome_time):
    elenco = elencos.get(nome_time, [])
    return render_template('elenco.html', time=nome_time, elenco=elenco)

if __name__ == '__main__':
    app.run()
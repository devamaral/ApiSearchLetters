from flask import Flask, render_template, request
from vsearch import script

app = Flask(__name__)  # ?


@app.route('/')  # ?
def hello() -> str:
    return 'Olá mundo de Flask!'


@app.route('/search4', methods=['POST'])
def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    return str(script.search4letters(phrase, letters))


@app.route('/entry')
def entry_page() -> str:
    return render_template('entry.html', the_title='Bem-vindo a função search4letters na web!')


@app.route('/result')
def result() -> str:
    return render_template('results.html', the_title='Bem-vindo ao resultado')


app.run(debug=True)
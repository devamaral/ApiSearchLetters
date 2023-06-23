from flask import Flask, render_template, request
from vsearch import script

app = Flask(__name__)  # ?


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Aqui estão os resultados'
    results = str(script.search4letters(phrase, letters))
    return render_template('results.html', the_phrase=phrase, the_letters=letters, the_title=title, the_results=results)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Bem-vindo a função search4letters na web!')


@app.route('/result')
def result() -> str:
    return render_template('results.html', the_title='Bem-vindo ao resultado')


app.run(debug=True)
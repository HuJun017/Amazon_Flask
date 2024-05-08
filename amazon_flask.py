import pandas as pd
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/elenco')
def elenco_prodotti():
    df = pd.read_csv('/workspace/Amazon_Flask/data/prodotti.csv')
    return render_template('tabella.html', tabella = df.to_html())



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
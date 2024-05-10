import pandas as pd
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    df = pd.read_csv('/workspace/Amazon_Flask/data/prodotti.csv')
    return render_template('index.html', prodotti=df.to_dict('records'))

@app.route('/elenco', methods=['POST'])
def elenco():
    #caricamento del dataframe con le informazioni
    df = pd.read_csv('/workspace/Amazon_Flask/data/prodotti.csv')
    if request.methods == 'POST'
        data = request.get_json()
    return ()






if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
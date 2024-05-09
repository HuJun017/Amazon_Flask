import pandas as pd
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

df = pd.read_csv('/workspace/Amazon_Flask/data/prodotti.csv')

@app.route('/')
def homepage():
    return render_template('index.html', prodotti=df.to_dict('records'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
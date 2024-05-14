from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load data globally
df = pd.read_csv('/workspace/Amazon_Flask/data/prodotti.csv')

@app.route('/')
def homepage():
    return render_template('index.html', prodotti=df.to_dict('records'))

@app.route('/elenco', methods=['POST'])
def elenco():
    if request.method == 'POST':
        json_data = request.get_json()
        NomeProdotto = json_data.get('NomeProdotto')
        data = df[df['Nome'] == NomeProdotto]
        data = data.to_dict(orient = 'records')
        return jsonify(data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)

from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/')
def homepage():
  df = pd.read_csv('/workspace/Amazon_Flask/data/prodotti.csv')
  return render_template('index.html', prodotti = df.to_dict('records'))

@app.route('/elenco', methods = ['POST'])
def elenco():
    if request.methods == 'POST':
        json = request.get_json()
        NomeProdotto = json.get('NomeProdotto')

        data = df[df['Nome'] == NomeProdotto]
        return { "code": 200, "data": getData.to_json() }
        print(getData)
        if len(getData) == 0:
            print('errore')
            return { "code": 302 }
        print('corretto')
        return { "code": 200, "data": getData.to_json(orient='records') }
# Rest of your code (unchanged)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
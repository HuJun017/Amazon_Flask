from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/')
def homepage():
  df = pd.read_csv('/workspace/Amazon_Flask/data/prodotti.csv')
  return render_template('index.html', prodotti = df.to_dict('records'))

# Rest of your code (unchanged)
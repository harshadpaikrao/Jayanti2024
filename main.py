from flask import Flask
from flask import render_template
from flask import request
import pandas as pd


df_collect = pd.read_csv(r'https://docs.google.com/spreadsheets/d/e/2PACX-1vQ4aPGN0M0ZCk5fxAxnqMKoSDZM9esRy5JU5wTZE9nTy0NdF9WbcTxRbOMUVmIwfRTx0uS0UIygg2rD/pub?gid=0&single=true&output=csv')



total_sheet = pd.read_csv(r'https://docs.google.com/spreadsheets/d/e/2PACX-1vQ4aPGN0M0ZCk5fxAxnqMKoSDZM9esRy5JU5wTZE9nTy0NdF9WbcTxRbOMUVmIwfRTx0uS0UIygg2rD/pub?gid=541885403&single=true&output=csv')



app = Flask(__name__)

@app.route('/collect')
def collect():
  record = df_collect.loc[df_collect['Receipt number']==20]
  return render_template("collect.html", name=record['Name'].values[0], date=record['Date'].values[0],amount=record['Amount'].values[0])
  

@app.route('/', methods=['GET','POST'])
def index():
  if request.method == 'GET':
    return render_template('home.html', total=total_sheet['Amount'].values[0], lb=total_sheet['Amount'].values[1], exp=total_sheet['Amount'].values[2], bal=total_sheet['Amount'].values[3])
  elif request.method == 'POST':
    n = request.form['number']
    record = df_collect.loc[df_collect['Receipt number']==int(n)]
    if not record.empty:
      return render_template("collect.html", name=record['Name'].values[0], date=record['Date'].values[0],amount=record['Amount'].values[0])
    else:
      return render_template('error.html')
@app.route('/full_details')
def full():
  return render_template('full_details.html')

app.run(host='0.0.0.0', port=81)

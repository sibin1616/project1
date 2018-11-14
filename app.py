from flask import Flask,render_template,request
from edata import employ
app=Flask(__name__) 
empd=employ()
@app.route('/')
def index():
    return render_template('home.html')
@app.route('/data')
def data():
    return render_template('edetails.html',edata=empd)
if(__name__=='__main__'):
    app.run(debug=True)
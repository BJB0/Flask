## Flask Application
from flask import Flask, request, render_template, redirect, url_for, jsonify


## Creating the flask application
app=Flask(__name__)

@app.route("/",methods=["GET"])
def welcome():
  return "<h1>Welcome to BJB world!</h1>"

@app.route("/index",methods=["GET"])
def index():
  return "<h2>Welcome to the Index page</h2>"

## Variable rule
@app.route('/success/<int:score>')
def success(score):
  return "The person has passed the exam and the score is: "+ str(score)

@app.route('/fail/<int:score>')
def fail(score):
  return "The person has Failed the exam and the score is: "+ str(score)

@app.route('/form',methods=["GET","POST"])
def form():
  if request.method=="GET":
    return render_template('form.html')
  else:
    maths=float(request.form['maths'])
    science=float(request.form['science'])
    history=float(request.form['history'])
    
    average_marks = (maths+science+history)/3
    res=""
    if average_marks>=50:
      res="success"
      return redirect(url_for(res,score=average_marks))
    else:
      res="fail"
      return redirect(url_for(res,score=average_marks))
    
    #return render_template('form.html',score=average_marks)
    
@app.route('/api',methods=["POST"])
def calculate_sum():
  data=request.get_json()
  a_val=float(dict(data)['a'])
  b_val=float(dict(data)['b'])
  return jsonify(a_val+b_val)
  

if __name__=="__main__":
  app.run(debug=True)
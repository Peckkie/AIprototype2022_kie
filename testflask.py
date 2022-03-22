from flask import Flask, render_template , request
import requests 
import json
import pandas as pd
#อะไรที่จะ import ในไฟล์ย่อย ให้ import ในไฟล์นี้ด้วย
app = Flask(__name__)

@app.route('/')
def hello():
  return "Hello, World!" 

@app.route('/name')
def hellokie():
  return "Hello, KIE!"  

#api
@app.route('/request',methods=['POST'])
def request_detail():

  payload = request.data.decode("utf-8")
  inmessage = json.loads(payload)

  print(inmessage)
    
  json_data = json.dumps({'y': 'received!'})
  return  json_data

##webapp 
@app.route("/home", methods =['POST','GET']) #ยิ่งใส่เยอะยิ่งอันตราย คนจะเข้ามาใช้งาน App เราได้ง่าย  #'GET'รับมาอย่างเดียวไม่ได้ส่งมาด้วย 
def home():
  
  if request.method =='POST':
    dbtb = pd.read_csv('db.csv')
    first_name = request.form.get("fname")
    last_name = request.form.get("lname")
    language_name = request.form.get("fav_language")
    dbtb = dbtb.append({'name':first_name,'lastname':last_name}, ignore_index=True)
    dbtb.to_csv('db.csv', index=False)
    return render_template("home.html", name = f"{first_name} {last_name}", language = f"{language_name}")
  # #new
  # if request.method =='POST':
  #   HTML_name = request.form.get("fav_language")

  #   return render_template("home.html", language = f"{HTML_name}")

  return render_template("home.html", name = 'Kie')

@app.route("/home2", methods =['POST','GET'])
def home2():
  #new
  if request.method =='POST':
    language_name = request.form.get("fav_language")

    return render_template("home.html", language = f"{language_name}")
  return render_template("home.html", language = 'Language')

if __name__ == "__main__":
  app.run() #host = '0.0.0.0'
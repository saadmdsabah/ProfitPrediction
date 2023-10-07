from flask import Flask,render_template,request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("startup.pkl","rb"))

@app.route("/")
def start():
    return render_template("index.html")

@app.route("/login",methods =['POST'])
def login():
   p = request.form["rd"]
   q = request.form["ad"]
   r = request.form["ms"]
   s = request.form["s"]
   if (s=="cal"):
       s=0
   elif(s=="flo"):
       s=1
   else:
       s=2 

   t =  [[float(p),float(q),float(r),float(s)]] 
   output = model.predict(t)

   return render_template("index.html", y = "The predicted profit is  "+str(np.round(output[0])))

if __name__ == "__main__" :
    app.run(debug=False,host="0.0.0.0")
    

from flask import Flask, render_template, request
from surgery import clpred
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def getvalue():
    hospital_id = int(request.form['hospital_id'])
    age=int(request.form['age'])
    gender=int(request.form['gender'])
    aids = int(request.form['aids'])
    cirrhosis = int(request.form['cirrhosis'])
    diabetes_mellitus = int(request.form['diabetes_mellitus'])
    hepatic_failure = int(request.form['hepatic_failure'])
    immunosuppression = int(request.form['immunosuppression'])
    leukemia = int(request.form['leukemia'])
    lymphoma = int(request.form['lymphoma'])
    solid_tumor_with_metastasis = int(request.form['solid_tumor_with_metastasis'])
    n=clpred(hospital_id,age,gender,aids,cirrhosis,diabetes_mellitus,hepatic_failure,immunosuppression,leukemia,lymphoma,solid_tumor_with_metastasis)
    if n:return render_template('pass.html',hid=hospital_id,age=age,gender="Male" if gender==1 else "Female",ans="Success")
    return render_template('pass.html',hid=hospital_id,age=age,gender="Male" if gender==1 else "Female",ans="Fail")


if __name__ == '__main__':
    app.run(debug=True)

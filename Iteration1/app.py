from flask import Flask, request
import model

app = Flask(__name__, template_folder="templates", static_folder='static')


@app.route('/Iteration1')
@app.route('/home/Iteration1')
def index():
    return model.home_page()


@app.route('/StatisticalData/Iteration1')
def dataVisualization():
    return model.data_page()


@app.route('/BackgroundCollection/Iteration1', methods=['POST', 'GET'])
def informationCollect():
    if request.method == 'GET':
        return model.information_page()
    elif request.method == 'POST':
        age = request.form['age']
        gender = request.form['gender']
        major = request.form['major']
        skills = request.form['skills']
        industry = request.form['industry']
        experience = request.form['experience']
        return model.fill_information(age, gender, major, skills, industry, experience)




if __name__ == '__main__':
    app.run(debug=True)

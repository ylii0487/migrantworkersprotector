from flask import Flask, request
import model

app = Flask(__name__, template_folder="templates", static_folder='static')


@app.route('/')
@app.route('/home')
def index():
    return model.home_page()


@app.route('/StatisticalData')
def dataVisualization():
    return model.data_page()


@app.route('/BackgroundCollection', methods=['POST', 'GET'])
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


@app.route('/Game')
def game():
    return model.game_page()


@app.route('/Game_Answers')
def game_farm_answers():
    return model.game_answers_page()


@app.route('/Guideline')
def game_faq():
    return model.general_page()


#
# @app.route('/Game_Answers_Factory')
# def game_factory_answers():
#     return model.game_answers_factory_page()
#
#
# @app.route('/Game_Answers_Hospital')
# def game_hospital_answers():
#     return model.game_answers_hospital_page()
#
#
# @app.route('/Game_Answers_Office')
# def game_office_answers():
#     return model.game_answers_office_page()
#
#
# @app.route('/Game_Answers_Truck')
# def game_truck_answers():
#     return model.game_answers_truck_page()


if __name__ == '__main__':
    app.run(debug=True)

import time

from flask import Flask, request, Response,jsonify
import model

app = Flask(__name__, template_folder="templates", static_folder='static')


@app.before_request
def before_request():
    auth = request.authorization
    if not auth or not (auth.username == 'FIT5120' and auth.password == 'ICECDG'):
        return Response('Could not verify your access level for that URL.\n'
                        'You have to login with proper credentials', 401,
                        {'WWW-Authenticate': 'Basic realm="Login Required"'})


@app.route('/')
@app.route('/home')
def index():
    return model.home_page()


@app.route('/StatisticalData')
def dataVisualization():
    return model.data_page()


@app.route('/SalaryCalculator', methods=['GET', 'POST'])
def salary_calculator():
    if request.method == 'GET':
        return model.salary_calculator_page()
    elif request.method == 'POST':

        industry = request.form['industry']
        employment_type = request.form['employment-type']
        holiday_pay = request.form['holiday-pay']

        # Call the method in model.py and get the result
        print(industry)
        print(employment_type)
        print(holiday_pay)
        return model.salary_calculator_result_page(industry, employment_type, holiday_pay)
        # Return the result as a JSON response
        # return jsonify({'averageWage': average_wage})
        # industry = request.form['industry']
        # work_type = request.form['employment-type']
        # return model.salary_calculator_result_page(industry, work_type)


@app.route('/AskForHelp')
def help_quiz():
    return model.help_page()


@app.route('/AskForHelp_Result/<help_type>/<help_topic>/<help_fix>')
def help_quiz_result(help_type, help_topic, help_fix):
    return model.help_page_result(help_type, help_topic, help_fix)

@app.route('/Game')
def game():
    return model.game_page()


@app.route('/Game_Answers')
def game_farm_answers():
    return model.game_answers_page()


@app.route('/Guideline', methods=['GET', 'POST'])
def guideline():
    if request.method == 'GET':
        return model.guideline_page()
    elif request.method == 'POST':
        search_keywords = request.form['search_keywords']
        return model.guideline_resultpage(search_keywords)


@app.route('/Guideline/<guideline_cat>')
def guideline_type(guideline_cat):
    return model.guideline_type_page(guideline_cat)


@app.route('/AboutUs')
def about():
    return model.about_page()


@app.route('/Privacy')
def privacy():
    return model.privacy_page()


@app.route('/Reference')
def site_map():
    return model.reference_page()


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

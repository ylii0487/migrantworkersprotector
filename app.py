from flask import Flask, request, Response
from flask_mail import Mail
import model

app = Flask(__name__, template_folder="templates", static_folder='static')

app.config['SECRET_KEY'] ='top-secret!'
app.config['MAIL_SERVER'] = 'smtp.sendgrid.net'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'apikey'
app.config['MAIL_PASSWORD'] = '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'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_DEFAULT_SENDER'] = 'liyongyi.elle@gmail.com'


mail = Mail(app)

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

        return model.salary_calculator_result_page(industry, employment_type, holiday_pay)


@app.route('/SendEmail/<subject>', methods=['GET'])
def send_email(subject):
    return model.send_email_page(subject)


@app.route('/SendEmail', methods=['POST'])
def send_email_post():

    to = request.form['to']
    new_subject = request.form['subject']

    return model.send_email_page_result(mail, to, new_subject)


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


if __name__ == '__main__':
    app.run(debug=True)

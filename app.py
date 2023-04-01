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


@app.route('/BackgroundCollection')
def informationCollect():
    return model.information_page()


if __name__ == '__main__':
    app.run(debug=True)

import view
import database
import security
import os
import pandas as pd
import json

page_view = view.View()
database = database.MySQLDatabase()
database.connect()
# database.tables_setup()

page_security = security.Security()


def home_page():
    return page_view("index")


def data_page():
    return page_view("data")


def information_page():
    return page_view("information")


def fill_information(age, gender, major, skills, industry, experience):
    if len(major.split(" ")) == 0 or len(skills.split(" ")) == 0 or len(experience.split(" ")) == 0:

        err_str = "major or skills or experience cannot be null"

        return page_view("invalid_add", reason=err_str)

    else:
        if page_security.is_xss(age) or page_security.is_sql_injection(age) or page_security.is_xss(
                major) or page_security.is_sql_injection(major) or page_security.is_xss(
            skills) or page_security.is_sql_injection(skills) or page_security.is_xss(
            industry) or page_security.is_sql_injection(industry) or page_security.is_xss(
            experience) or page_security.is_sql_injection(experience):
            err_str = "String formate is incorrect"
            return page_view("invalid_add", reason=err_str)
        else:
            fill_info = database.add_info(age, gender, major, skills, industry, experience)
            database.get_allInfos()
            if fill_info:
                return page_view("information_successful")
            else:
                err_str = "The information is invalid"
                return page_view("invalid_add", reason=err_str)


def game_page():
    path = os.path.join(os.path.dirname(__file__), "data/game/safty_work.csv")
    df = pd.read_csv(path)
    df = df.fillna("")
    points = json.dumps(df.to_dict("records"))

    return page_view("game", points=points)


def game_answers_page():
    return page_view("game_answers")


# def game_answers_farm_page():
#     return page_view("game_answers_Farm")
#
#
# def game_answers_hospital_page():
#     return page_view("game_answers_Hospital")
#
#
# def game_answers_office_page():
#     return page_view("game_answers_Office")
#
#
# def game_answers_truck_page():
#     return page_view("game_answers_Truck")
def general_page():
    return page_view("guidline")
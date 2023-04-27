import view
import database
import security
import os
import pandas as pd
import json

page_view = view.View()
database = database.MySQLDatabase()
database.connect()
database.tables_setup()

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


def guideline_page():
    guidelines = database.get_allInfos_WorkingRights()
    guideline_type = database.get_allInfos_WorkingRights_Type()
    # guideline_title = database.get_allInfos_WorkingRights_Title()
    titles = {}
    subtitles = {}

    for guideline in guidelines:

        if guideline[4] in titles:
            if guideline[5] in subtitles:
                subtitles[guideline[5]] = guideline[6]
            else:
                subtitles.update({guideline[5]: guideline[6]})
            titles[guideline[4]] = subtitles
        else:
            subtitles = {}
            if guideline[5] in subtitles:
                subtitles[guideline[5]] = guideline[6]
            else:
                subtitles.update({guideline[5]: guideline[6]})
            titles.update({guideline[4]: subtitles})


    return page_view("guideline", types=guideline_type, titles=titles)
    # return page_view("guideline")


def guideline_resultpage(search_keywords):
    if len(search_keywords.split(" ")) == 0:

        err_str = "search_keywords cannot be null"

        return page_view("invalid_add", reason=err_str)

    else:
        if page_security.is_xss(search_keywords) or page_security.is_sql_injection(search_keywords):
            err_str = "String formate is incorrect"
            return page_view("invalid_add", reason=err_str)
        else:
            search_guidelines = database.get_searchGuideline(search_keywords)

            search_guideline_type = database.get_allInfos_WorkingRights_Type()
            search_titles = {}
            subtitles = {}

            for guideline in search_guidelines:

                if guideline[4] in search_titles:
                    if guideline[5] in subtitles:
                        subtitles[guideline[5]] = guideline[6]
                    else:
                        subtitles.update({guideline[5]: guideline[6]})
                    search_titles[guideline[4]] = subtitles
                else:
                    subtitles = {}
                    if guideline[5] in subtitles:
                        subtitles[guideline[5]] = guideline[6]
                    else:
                        subtitles.update({guideline[5]: guideline[6]})
                    search_titles.update({guideline[4]: subtitles})

            return page_view("guideline", types=search_guideline_type, titles=search_titles)


def guideline_type_page(search_types):
    search_guidelines = database.get_searchGuideline_type(search_types)
    search_titles = {}
    subtitles = {}

    print(search_types)
    for guideline in search_guidelines:

        if guideline[4] in search_titles:
            if guideline[5] in subtitles:
                subtitles[guideline[5]] = guideline[6]
            else:
                subtitles.update({guideline[5]: guideline[6]})
            search_titles[guideline[4]] = subtitles
        else:
            subtitles = {}
            if guideline[5] in subtitles:
                subtitles[guideline[5]] = guideline[6]
            else:
                subtitles.update({guideline[5]: guideline[6]})
            search_titles.update({guideline[4]: subtitles})

    return page_view("guideline_type", types=search_types, titles=search_titles)

def about_page():
    return page_view("about")
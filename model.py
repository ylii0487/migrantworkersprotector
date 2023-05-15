import json
import os

import pandas as pd
from flask_mail import Message

import database
import security
import view

page_view = view.View()
database = database.MySQLDatabase()

page_security = security.Security()

calculator_result = {}
help_result = {}


def home_page():
    return page_view("index")


def data_page():
    return page_view("data")


def salary_calculator_page():
    database.connect()
    classifications = database.get_allInfos_Calculator_Classification()
    calculator_types = database.get_allInfos_Calculator_Type()
    database.close()
    result = 0
    industry = "Not Selected"
    employment_type = "Not Selected"
    holiday_pay = "Not Selected"
    return page_view("calculator", classifications=classifications, calculator_types=calculator_types,
                     industry=industry, employment_type=employment_type, holiday_pay=holiday_pay, result=result)


def salary_calculator_result_page(industry, work_type, holiday_pay):
    database.connect()
    if industry == "" or work_type is None or holiday_pay is None:
        database.connect()
        classifications = database.get_allInfos_Calculator_Classification()
        calculator_types = database.get_allInfos_Calculator_Type()
        database.close()
        result = 0
        industry = "Not Selected"
        employment_type = "Not Selected"
        holiday_pay = "Not Selected"
        return page_view("calculator", classifications=classifications, calculator_types=calculator_types,
                         industry=industry, employment_type=employment_type, holiday_pay=holiday_pay, result=result)

    else:
        if holiday_pay == 'Yes':

            result = database.get_allInfos_Calculator_Result_Holiday(industry, work_type)
            classifications = database.get_allInfos_Calculator_Classification()
            calculator_types = database.get_allInfos_Calculator_Type()
        else:
            result = database.get_allInfos_Calculator_Result(industry, work_type)
            classifications = database.get_allInfos_Calculator_Classification()
            calculator_types = database.get_allInfos_Calculator_Type()

        database.close()
        calculator_result.update({"industry": industry})
        calculator_result.update({"employment_type": work_type})
        calculator_result.update({"holiday_pay": holiday_pay})
        calculator_result.update({"result": result})

        print(calculator_result)
        return page_view("calculator", classifications=classifications, calculator_types=calculator_types,
                         industry=industry, employment_type=work_type, holiday_pay=holiday_pay,
                         result=result)


def help_page():
    database.connect()
    help_types = database.get_allInfos_AskForHelp_Type()
    topics = {}
    for help_type in help_types:
        help_topics = database.get_allInfos_AskForHelp_Topic(help_type[0])

        if help_type in topics:
            topics[help_type] = help_topics
        else:
            topics.update({help_type: help_topics})

    database.close()

    return page_view("ask_for_help", types=help_types, topics=topics)


def help_page_result(quiz_type, quiz_topic, quiz_fix):
    if page_security.is_xss(quiz_type) or page_security.is_sql_injection(quiz_type) or page_security.is_xss(
            quiz_topic) or page_security.is_sql_injection(quiz_topic) or page_security.is_xss(
        quiz_fix) or page_security.is_sql_injection(quiz_fix):
        err_str = "String formate is incorrect"
        return page_view("invalid_add", reason=err_str)
    else:
        database.connect()
        results = database.get_allInfos_AskForHelp_Result(quiz_type, quiz_topic)
        database.close()
        descriptions = {}

        if quiz_fix == 'yes':
            message = 'You can have a good chat about your problem with your boss or colleagues who may be able to ' \
                      'give you some help. '
            descriptions.update({message: 'If you think your colleagues and supervisors can help you, you can muster '
                                          'up the courage to establish a consultation with them and have a proper '
                                          'conversation with them.'})
        else:
            for result in results:
                if result[0] in descriptions:
                    descriptions[result[0]] = result[1]
                else:
                    descriptions.update({result[0]: result[1]})

        help_result = descriptions.copy()

        print(help_result)
        return page_view("ask_for_help_result", descriptions=descriptions)


def game_page():
    path = os.path.join(os.path.dirname(__file__), "data/game/safty_work.csv")
    df = pd.read_csv(path)
    df = df.fillna("")
    points = json.dumps(df.to_dict("records"))

    return page_view("game", points=points)


def game_answers_page():
    return page_view("game_answers")


def guideline_page():
    database.connect()
    guidelines = database.get_allInfos_WorkingRights()
    guideline_type = database.get_allInfos_WorkingRights_Type()
    database.close()
    # guideline_title = database.get_allInfos_WorkingRights_Title()
    titles = {}
    subtitles = {}

    for guideline in guidelines:

        if guideline[5] in titles:
            if guideline[6] in subtitles:
                subtitles[guideline[6]] = guideline[7]
            else:
                subtitles.update({guideline[6]: guideline[7]})
            titles[guideline[5]] = subtitles
        else:
            subtitles = {}
            if guideline[6] in subtitles:
                subtitles[guideline[6]] = guideline[7]
            else:
                subtitles.update({guideline[6]: guideline[7]})
            titles.update({guideline[5]: subtitles})

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
            database.connect()
            search_guidelines = database.get_searchGuideline(search_keywords)

            search_guideline_type = database.get_allInfos_WorkingRights_Type()
            database.close()
            search_titles = {}
            subtitles = {}

            for guideline in search_guidelines:

                if guideline[5] in search_titles:
                    if guideline[6] in subtitles:
                        subtitles[guideline[6]] = guideline[7]
                    else:
                        subtitles.update({guideline[6]: guideline[7]})
                    search_titles[guideline[5]] = subtitles
                else:
                    subtitles = {}
                    if guideline[6] in subtitles:
                        subtitles[guideline[6]] = guideline[7]
                    else:
                        subtitles.update({guideline[6]: guideline[7]})
                    search_titles.update({guideline[5]: subtitles})

            return page_view("guideline_result", types=search_guideline_type, titles=search_titles,
                             keywords=search_keywords)


def guideline_type_page(search_types):
    database.connect()
    search_guidelines = database.get_searchGuideline_type(search_types)
    database.close()
    search_titles = {}
    subtitles = {}
    # print(search_types)
    print(search_guidelines)
    for guideline in search_guidelines:

        if guideline[5] in search_titles:
            if guideline[6] in subtitles:
                subtitles[guideline[6]] = guideline[7]
            else:
                subtitles.update({guideline[6]: guideline[7]})
            search_titles[guideline[5]] = subtitles
        else:
            subtitles = {}
            if guideline[6] in subtitles:
                subtitles[guideline[6]] = guideline[7]
            else:
                subtitles.update({guideline[6]: guideline[7]})
            search_titles.update({guideline[5]: subtitles})

    return page_view("guideline_type", types=search_types, titles=search_titles)


def about_page():
    return page_view("about")


def privacy_page():
    return page_view("privacy")


def reference_page():
    return page_view("reference")


def send_email_page(subject):
    return page_view("email", subject=subject)


def send_email_page_result(mail, to, subject):
    # template= render_template('email.html')
    # msg = Message(subject, recipients=[to])
    # msg.html = template
    # mail.send(msg)
    # print(to)

    # if subject == 'Salary_Calculator_Result':
    industry = calculator_result["industry"]
    employment_type = calculator_result["employment_type"]
    holiday_pay = calculator_result["holiday_pay"]
    result = calculator_result["result"]

    msg = Message(subject, recipients=[to])
    msg.body = 'Congratulations! You have sent a email to your email address'
    msg.html = ('<h2>Salary Calculator Result</h2>'
                '<p>Dear ' + to + ':</p>'
                                  '<p>Here is your salary calculator result:</p>'
                                  '<p>You Selected Industry: ' + industry + '</p>'
                                                                            '<p>Your Selected Employment Type is: ' + employment_type + '</p>'
                                                                                                                                        '<p>Is This Holiday Pay?: ' + holiday_pay + '</p>'
                                                                                                                                                                                    '<p>Result: ' +
                result[0][0] + '</p>'
                               '<p>Thank you for using our salary calculator.</p>')
    # msg.html = template
    mail.send(msg)
    return page_view("email_successful")


# else:
#     # template = render_template('email_help.html', username=to, description=ask_for_help_result)
#     msg = Message(subject, recipients=[to])
#     msg.body = 'Congratulations! You have sent a email to your email address'
#     msg.html = ('<h2>Ask For Help Result </h2>'
#                 '<p>Dear ' + to + ':</p>'
#
#                 '<p>Thank you for using our "Ask For Help" service. We have processed your request and here is the result:</p>'
#                 '<p>Result: </p>'
#
#                 '<p>Thank you for using our help services.</p>')
#     # msg.html = template
#     mail.send(msg)



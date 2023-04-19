import view
import database
import security

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


def recommendation_page():
    return page_view("recommendation")


def support_page():
    return page_view("support")


def about_page():
    return page_view("about")

import view
import database

page_view = view.View()


def home_page():
    return page_view("index")


def data_page():
    return page_view("data")


def information_page():
    return page_view("information")

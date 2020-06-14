from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper


class Application:

    def __init__(self):
        self.dw = webdriver.Firefox()
        self.dw.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)


    def open_home_page(self):
        dw = self.dw
        dw.get("http://localhost/addressbook")


    def destroy(self):
        self.dw.quit()

###
    def create_contact(self, contact):
        dw = self.dw
        # init contact creation
        dw.find_element_by_link_text("add new").click()
        # fill out contact form
        dw.find_element_by_name("firstname").send_keys(contact.firstname)
        dw.find_element_by_name("lastname").send_keys(contact.lastname)
        dw.find_element_by_name("address").send_keys(contact.address)
        dw.find_element_by_name("mobile").send_keys(contact.mobile)
        dw.find_element_by_name("email").send_keys(contact.email)
        dw.find_element_by_name("bday").send_keys(contact.bday)
        dw.find_element_by_name("bmonth").send_keys(contact.bmonth)
        # submit contact form
        dw.find_element_by_name("submit").click()
        self.return_to_homepage()


    def return_to_homepage(self):
        dw = self.dw
        dw.find_element_by_link_text("home").click()
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:

    def __init__(self):
        self.dw = webdriver.Firefox()
        #self.dw.implicitly_wait(1)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)


    def is_valid(self):
        try:
            self.dw.current_url
            return True
        except:
            return False


    def open_home_page(self):
        dw = self.dw
        dw.get("http://localhost/addressbook")


    def destroy(self):
        self.dw.quit()

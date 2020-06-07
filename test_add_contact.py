# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from contact import Contact

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.dw = webdriver.Firefox()
        self.dw.implicitly_wait(30)

    def open_homepage(self, dw):
        dw.get("http://localhost/addressbook/")

    def login(self, dw, username, password):
        dw.find_element_by_name("user").send_keys(username)
        dw.find_element_by_name("pass").send_keys(password)
        dw.find_element_by_css_selector("input[type=\"submit\"]").click()

    def create_contact(self, dw, contact):
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

    def return_to_homepage(self, dw):
        dw.find_element_by_link_text("home").click()

    def logout(self, dw):
        dw.find_element_by_link_text("Logout").click()

 #######

    def test_add_contact(self):
        dw = self.dw
        self.open_homepage(dw)
        self.login(dw, username="admin", password="secret")
        self.create_contact(dw, Contact(firstname="sgsgsggs", lastname="dhdhdh", address="dhdhd", mobile="512-111-1111", email="ssgsgsg@gmail.com", bday="18", bmonth="September"))
        self.return_to_homepage(dw)
        self.logout(dw)

    def test_add_empty_contact(self):
        dw = self.dw
        self.open_homepage(dw)
        self.login(dw, username="admin", password="secret")
        self.create_contact(dw, Contact(firstname="", lastname="", address="", mobile="", email="", bday="", bmonth=""))
        self.return_to_homepage(dw)
        self.logout(dw)

    def tearDown(self):
        self.dw.quit()

if __name__ == "__main__":
    unittest.main()

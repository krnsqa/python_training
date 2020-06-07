# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from group import Group

class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.dw = webdriver.Firefox()
        self.dw.implicitly_wait(60)

    def open_home_page(self, dw):
        dw.get("http://localhost/addressbook")

    def login(self, dw, username, password):
        dw.find_element_by_name("user").send_keys(username)
        dw.find_element_by_name("pass").send_keys(password)
        dw.find_element_by_css_selector("input[type=\"Submit\"]").click()

    def open_groups_page(self, dw):
        dw.find_element_by_link_text("groups").click()

    def create_group(self, dw, group):
        # init group creation
        dw.find_element_by_name("new").click()
        # fill out group form
        dw.find_element_by_name("group_name").send_keys(group.name)
        dw.find_element_by_name("group_header").send_keys(group.header)
        dw.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group form creation
        dw.find_element_by_name("submit").click()

    def return_to_groups_page(self, dw):
        dw.find_element_by_link_text("group page").click()

    def logout(self, dw):
        dw.find_element_by_link_text("Logout").click()

########

    def test_add_group(self):
        dw = self.dw
        self.open_home_page(dw)
        self.login(dw, username="admin", password="secret")
        self.open_groups_page(dw)
        self.create_group(dw, Group(name="dfdhdh", header="dsgshs", footer="sfsgsg"))
        self.return_to_groups_page(dw)
        self.logout(dw)

    def test_add_empty_group(self):
        dw = self.dw
        self.open_home_page(dw)
        self.login(dw, username="admin", password="secret")
        self.open_groups_page(dw)
        self.create_group(dw, Group(name="", header="", footer=""))
        self.return_to_groups_page(dw)
        self.logout(dw)

    def tearDown(self):
        self.dw.quit()

if __name__ == "__main__":
    unittest.main()

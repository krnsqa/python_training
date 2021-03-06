from model.contact import Contact
import re
from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app


    def change_field_value(self, field_name, text):
        dw = self.app.dw
        if text is not None:
            dw.find_element_by_name(field_name).clear()
            dw.find_element_by_name(field_name).send_keys(text)


    def fill_contact_form(self, contact):
        dw = self.app.dw
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("email", contact.email)
        self.change_field_value("phone2", contact.secondaryphone)



    def open_homepage(self):
        dw = self.app.dw
        if not (dw.current_url.endswith("/addressbook/")):
            dw.find_element_by_link_text("home").click()


    def create(self, contact):
        dw = self.app.dw
        self.open_homepage()
        # init contact creation
        dw.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit contact form
        dw.find_element_by_name("submit").click()
        self.return_to_homepage()
        self.contact_cache = None


    def return_to_homepage(self):
        dw = self.app.dw
        dw.find_element_by_link_text("home").click()


    def select_first_contact(self):
        dw = self.app.dw
        dw.find_element_by_name("selected[]").click()


    def select_contact_by_index(self, index):
        dw = self.app.dw
        dw.find_elements_by_name("selected[]")[index].click()


    def select_contact_by_id(self, id):
        dw = self.app.dw
        dw.find_element_by_css_selector("input[value='%s']" % id).click()


    def select_contact_to_edit_by_index(self, index):
        dw = self.app.dw
        # open modification form
        dw.find_elements_by_css_selector("#maintable a[href^='edit']")[index].click()


    def select_contact_to_edit_by_id(self, id):
        dw = self.app.dw
        # open modification form
        dw.find_element_by_css_selector("#maintable a[href='edit.php?id=%s']" % id).click()


    def delete_first_contact(self):
        dw = self.app.dw
        self.delete_contact_by_index(0)


    def delete_contact_by_index(self, index):
        dw = self.app.dw
        self.open_homepage()
        self.select_contact_by_index(index)
        # submit deletion
        dw.find_element_by_css_selector("input[value='Delete']").click()
        # confirm deletion
        dw.switch_to_alert().accept()
        self.return_to_homepage()
        self.contact_cache = None


    def delete_contact_by_id(self, id):
        dw = self.app.dw
        self.open_homepage()
        self.select_contact_by_id(id)
        # submit deletion
        dw.find_element_by_css_selector("input[value='Delete']").click()
        # confirm deletion
        dw.switch_to_alert().accept()
        self.return_to_homepage()
        self.contact_cache = None


    def modify_first_contact(self):
        dw = self.app.dw
        self.modify_contact_by_index(0)


    def modify_contact_by_index(self, index, new_contact_data):
        dw = self.app.dw
        self.open_homepage()
        self.select_contact_by_index(index)
        self.select_contact_to_edit_by_index(index)
        self.fill_contact_form(new_contact_data)
        # submit modification
        dw.find_element_by_name("update").click()
        self.return_to_homepage()
        self.contact_cache = None


    def modify_contact_by_id(self, id, new_contact_data):
        dw = self.app.dw
        self.open_homepage()
        self.select_contact_by_id(id)
        self.select_contact_to_edit_by_id(id)
        self.fill_contact_form(new_contact_data)
        # submit modification
        dw.find_element_by_name("update").click()
        self.return_to_homepage()
        self.contact_cache = None


    def count(self):
        dw = self.app.dw
        self.open_homepage()
        return len(dw.find_elements_by_name("selected[]"))


    contact_cache = None


    def get_contact_list(self):
        if self.contact_cache is None:
            dw = self.app.dw
            self.open_homepage()
            self.contact_cache = []
            rows = dw.find_elements_by_css_selector("tr[name='entry']")
            for row in rows:
                cells = row.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_name("selected[]").get_attribute("value")
                firstname = cells[2].text
                lastname = cells[1].text
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(id=id, firstname=firstname, lastname=lastname, address=address,
                                                  all_emails_from_homepage=all_emails, all_phones_from_homepage=all_phones))
        return list(self.contact_cache)


    def get_contact_from_contact_list_by_index(self, index, contact_cache):
        self.contact_cache_by_index = contact_cache[index]
        return (self.contact_cache_by_index)


    def open_contacts_to_edit_by_index(self, index):
        dw = self.app.dw
        self.open_homepage()
        row = dw.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()


    def open_contact_view_by_index(self, index):
        dw = self.app.dw
        self.open_homepage()
        row = dw.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()


    def get_contact_info_from_edit_page(self, index):
        dw = self.app.dw
        self.open_contacts_to_edit_by_index(index)
        firstname = dw.find_element_by_name("firstname").get_attribute("value")
        lastname = dw.find_element_by_name("lastname").get_attribute("value")
        id = dw.find_element_by_name("id").get_attribute("value")
        email = dw.find_element_by_name("email").get_attribute("value")
        email2 = dw.find_element_by_name("email2").get_attribute("value")
        email3 = dw.find_element_by_name("email3").get_attribute("value")
        homephone = dw.find_element_by_name("home").get_attribute("value")
        mobile = dw.find_element_by_name("mobile").get_attribute("value")
        workphone = dw.find_element_by_name("work").get_attribute("value")
        secondaryphone = dw.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       email=email, email2=email2, email3=email3,
                       homephone=homephone, mobile=mobile, workphone=workphone, secondaryphone=secondaryphone)


    def get_contact_from_view_page(self, index):
        dw = self.app.dw
        self.open_contact_view_by_index(index)
        text = dw.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, mobile=mobile,
                       workphone=workphone, secondaryphone=secondaryphone)


    def add_contact_to_group(self, contact, group):
        dw = self.app.dw
        self.open_homepage()
        # select contact
        self.select_contact_by_id(contact.id)
        # add contact to group
        dw.find_element_by_name("to_group").click
        Select(dw.find_element_by_name("to_group")).select_by_value('%s' % group.id)
        dw.find_element_by_name("add").click()
        # return to homepage
        dw.find_element_by_id("logo").click()


    def delete_contact_from_group(self, group, contact):
        dw = self.app.dw
        self.open_homepage()
        # select group
        dw.find_element_by_name("group").click
        Select(dw.find_element_by_name("group")).select_by_value('%s' % group.id)
        # select and delete contact in group
        self.select_contact_by_id(contact.id)
        dw.find_element_by_css_selector(".left [name='remove']").click()
        # return to homepage
        dw.find_element_by_id("logo").click()
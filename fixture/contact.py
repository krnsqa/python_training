from model.contact import Contact


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
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("email", contact.email)


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


    def delete_first_contact(self):
        dw = self.app.dw
        self.delete_contact_by_index(0)


    def delete_contact_by_index(self, index):
        dw = self.app.dw
        self.open_homepage()
        self.select_contact_by_index(index)
        # submit deletion
        dw.find_element_by_css_selector("input[value=\"Delete\"]").click()
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
        # open modification form
        dw.find_element_by_css_selector("#maintable a[href^='edit']").click()
        # fill out group form
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
            for element in rows:
                id = element.find_element_by_name("selected[]").get_attribute("value")
                cells = element.find_elements_by_tag_name("td")
                self.contact_cache.append(Contact(id=id, firstname=cells[2].text, lastname=cells[1].text))
        return list(self.contact_cache)
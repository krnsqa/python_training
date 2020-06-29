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


    def return_to_homepage(self):
        dw = self.app.dw
        dw.find_element_by_link_text("home").click()


    def select_first_contact(self):
        dw = self.app.dw
        dw.find_element_by_name("selected[]").click()


    def delete_first_contact(self):
        dw = self.app.dw
        self.open_homepage()
        self.select_first_contact()
        # submit deletion
        dw.find_element_by_css_selector("input[value=\"Delete\"]").click()
        # confirm deletion
        dw.switch_to_alert().accept()
        self.return_to_homepage()


    def modify_first_contact(self, new_contact_data):
        dw = self.app.dw
        self.open_homepage()
        self.select_first_contact()
        # open modification form
        dw.find_element_by_css_selector("#maintable a[href^='edit']").click()
        # fill out group form
        self.fill_contact_form(new_contact_data)
        # submit modification
        dw.find_element_by_name("update").click()
        self.return_to_homepage()


    def count(self):
        dw = self.app.dw
        self.open_homepage()
        return len(dw.find_elements_by_name("selected[]"))


    def get_contact_list(self):
        dw = self.app.dw
        self.open_homepage()
        contacts = []
        for element in dw.find_elements_by_css_selector("tr[name='entry']"):
            text = element.text.split(" ")
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contacts.append(Contact(id=id, firstname=text[1], lastname=text[0]))
        return contacts
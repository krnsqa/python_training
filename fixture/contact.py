

class ContactHelper:

    def __init__(self, app):
        self.app = app


    def fill_contact_form(self, contact):
        dw = self.app.dw
        dw.find_element_by_name("firstname").send_keys(contact.firstname)
        dw.find_element_by_name("lastname").send_keys(contact.lastname)
        dw.find_element_by_name("address").send_keys(contact.address)
        dw.find_element_by_name("mobile").send_keys(contact.mobile)
        dw.find_element_by_name("email").send_keys(contact.email)
        dw.find_element_by_name("bday").send_keys(contact.bday)
        dw.find_element_by_name("bmonth").send_keys(contact.bmonth)


    def create(self, contact):
        dw = self.app.dw
        # init contact creation
        dw.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit contact form
        dw.find_element_by_name("submit").click()
        self.return_to_homepage()


    def return_to_homepage(self):
        dw = self.app.dw
        dw.find_element_by_link_text("home").click()


    def delete_first_contact(self):
        dw = self.app.dw
        # select first contact
        dw.find_element_by_name("selected[]").click()
        # submit deletion
        dw.find_element_by_css_selector("input[value=\"Delete\"]").click()
        # confirm deletion
        dw.switch_to_alert().accept()


    def clear_contact_form(self):
        dw = self.app.dw
        dw.find_element_by_name("firstname").clear()
        dw.find_element_by_name("lastname").clear()
        dw.find_element_by_name("address").clear()
        dw.find_element_by_name("mobile").clear()
        dw.find_element_by_name("email").clear()
        dw.find_element_by_name("bday").send_keys("")
        dw.find_element_by_name("bmonth").send_keys("")


    def edit_first_contact(self, contact):
        dw = self.app.dw
        # select first contact
        dw.find_element_by_css_selector("#maintable a[href^='edit']").click()
        # clear edit contact form
        self.clear_contact_form()
        self.fill_contact_form(contact)
        # submit edit contact form
        dw.find_element_by_name("update").click()
        self.return_to_homepage()



class ContactHelper:

    def __init__(self, app):
        self.app = app


    def create(self, contact):
        dw = self.app.dw
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
        dw = self.app.dw
        dw.find_element_by_link_text("home").click()
from selenium import webdriver



class Application:

    def __init__(self):
        self.dw = webdriver.Firefox()
        self.dw.implicitly_wait(60)

    def open_home_page(self):
        dw = self.dw
        dw.get("http://localhost/addressbook")

    def login(self, username, password):
        dw = self.dw
        self.open_home_page()
        dw.find_element_by_name("user").send_keys(username)
        dw.find_element_by_name("pass").send_keys(password)
        dw.find_element_by_css_selector("input[type=\"Submit\"]").click()

    def open_groups_page(self):
        dw = self.dw
        dw.find_element_by_link_text("groups").click()

    def create_group(self, group):
        dw = self.dw
        self.open_groups_page()
        # init group creation
        dw.find_element_by_name("new").click()
        # fill out group form
        dw.find_element_by_name("group_name").send_keys(group.name)
        dw.find_element_by_name("group_header").send_keys(group.header)
        dw.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group form creation
        dw.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        dw = self.dw
        dw.find_element_by_link_text("group page").click()

    def logout(self):
        dw = self.dw
        dw.find_element_by_link_text("Logout").click()

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


class SessionHelper:

    def __init__(self, app):
        self.app = app


    def login(self, username, password):
        dw = self.app.dw
        self.app.open_home_page()
        dw.find_element_by_name("user").send_keys(username)
        dw.find_element_by_name("pass").send_keys(password)
        dw.find_element_by_css_selector("input[type=\"Submit\"]").click()


    def logout(self):
        dw = self.app.dw
        dw.find_element_by_link_text("Logout").click()


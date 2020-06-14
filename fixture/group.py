

class GroupHelper:

    def __init__(self, app):
        self.app = app


    def open_groups_page(self):
        dw = self.app.dw
        dw.find_element_by_link_text("groups").click()


    def create(self, group):
        dw = self.app.dw
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
        dw = self.app.dw
        dw.find_element_by_link_text("group page").click()

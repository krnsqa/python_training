

class GroupHelper:

    def __init__(self, app):
        self.app = app


    def open_groups_page(self):
        dw = self.app.dw
        dw.find_element_by_link_text("groups").click()


    def fill_group_form(self, group):
        dw = self.app.dw
        dw.find_element_by_name("group_name").send_keys(group.name)
        dw.find_element_by_name("group_header").send_keys(group.header)
        dw.find_element_by_name("group_footer").send_keys(group.footer)


    def create(self, group):
        dw = self.app.dw
        self.open_groups_page()
        # init group creation
        dw.find_element_by_name("new").click()
        self.fill_group_form(group)
        # submit group form creation
        dw.find_element_by_name("submit").click()
        self.return_to_groups_page()


    def return_to_groups_page(self):
        dw = self.app.dw
        dw.find_element_by_link_text("group page").click()


    def delete_first_group(self):
        dw = self.app.dw
        self.open_groups_page()
        # select first group
        dw.find_element_by_name("selected[]").click()
        # submit deletion
        dw.find_element_by_name("delete").click()
        self.return_to_groups_page()


    def clear_group_form(self):
        dw = self.app.dw
        dw.find_element_by_name("group_name").clear()
        dw.find_element_by_name("group_header").clear()
        dw.find_element_by_name("group_footer").clear()


    def edit_first_group(self, group):
        dw = self.app.dw
        self.open_groups_page()
        # select first group
        dw.find_element_by_name("selected[]").click()
        # submit editing
        dw.find_element_by_name("edit").click()
        self.clear_group_form()
        self.fill_group_form(group)
        # submit edit group form
        dw.find_element_by_name("update").click()
        self.return_to_groups_page()
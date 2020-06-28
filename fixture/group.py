from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app


    def open_groups_page(self):
        dw = self.app.dw
        if not (dw.current_url.endswith("/group.php") and len(dw.find_elements_by_name("new")) > 0):
            dw.find_element_by_link_text("groups").click()
        # OR
        #if (dw.current_url.endswith("/group.php") and len(dw.find_elements_by_name("new")) > 0):
            #return
        #dw.find_element_by_link_text("groups").click()


    def change_field_value(self, field_name, text):
        dw = self.app.dw
        if text is not None:
            dw.find_element_by_name(field_name).clear()
            dw.find_element_by_name(field_name).send_keys(text)


    def fill_group_form(self, group):
        dw = self.app.dw
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)


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
        self.select_first_group()
        # submit deletion
        dw.find_element_by_name("delete").click()
        self.return_to_groups_page()


    def select_first_group(self):
        dw = self.app.dw
        dw.find_element_by_name("selected[]").click()


    def modify_first_group(self, new_group_data):
        dw = self.app.dw
        self.open_groups_page()
        self.select_first_group()
        # open modification form
        dw.find_element_by_name("edit").click()
        # fill out group form
        self.fill_group_form(new_group_data)
        # submit modification
        dw.find_element_by_name("update").click()
        self.return_to_groups_page()


    def count(self):
        dw = self.app.dw
        self.open_groups_page()
        return len(dw.find_elements_by_name("selected[]"))


    def get_group_list(self):
        dw = self.app.dw
        self.open_groups_page()
        groups = []
        for element in dw.find_elements_by_css_selector("span.group"):
            text = element.text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            groups.append(Group(name=text, id=id))
        return groups


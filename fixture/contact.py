class ContactHelper:

    def __init__ (self,app):
        self.app=app

    def create(self, contact):
        wd = self.app.wd
        # init group creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit group creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("lastname", contact.last_name)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_contact(self):
        wd = self.app.wd
        # select first group
        wd.find_element_by_name("selected[]").click()
        # # deletion submit
        wd.find_element_by_css_selector("[value=Delete]").click()
        wd.switch_to_alert().accept()

    def modyfied_contact(self, firstname):
        wd = self.app.wd
        self.select_first_contact()
        # open modification form
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        # fill contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(firstname)
        # submit modyfication
        wd.find_element_by_name("update").click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.select_first_contact()
     # open modification form
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()

        # fill contact form
        self.fill_contact_form(new_contact_data)

         # submit modyfication
        wd.find_element_by_name("update").click()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))
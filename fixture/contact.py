from model.contact import Contact

class ContactHelper:

    def __init__ (self,app):
        self.app=app

    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/") and len(wd.find_elements_by_name("add"))>0):
            wd.find_element_by_link_text("home").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        # init group creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit group creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_contact_page()
        self.contact_cache=None

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

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self,index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self,index):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        self.select_contact_by_index(index)
        # # deletion submit
        wd.find_element_by_css_selector("[value=Delete]").click()
        wd.switch_to_alert().accept()
        self.return_contact_page()
        self.contact_cache = None
        ################

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self,index, new_contact_data):
        wd = self.app.wd
        self.open_contact_page()
        self.select_contact_by_index(index)
     # open modification form
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        # fill contact form
        self.fill_contact_form(new_contact_data)
         # submit modyfication
        wd.find_element_by_name("update").click()
        # self.open_home_page()
        self.return_contact_page
        self.contact_cache = None

    # def modify_first_contact(self, new_contact_data):
    #     wd = self.app.wd
    #     self.open_contact_page()
    #     self.select_first_contact()
    #  # open modification form
    #     wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
    #     # fill contact form
    #     self.fill_contact_form(new_contact_data)
    #      # submit modyfication
    #     wd.find_element_by_name("update").click()
    #     # self.open_home_page()
    #     self.return_contact_page
    #     self.contact_cache = None

    def return_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache=None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_page()
            self.contact_cache = []
        for element in wd.find_elements_by_name("entry"):
            id = element.find_element_by_name("selected[]").get_attribute("value")
            cells = element.find_elements_by_css_selector("td")
            firstname=cells[2].text
            self.contact_cache.append(Contact(first_name=firstname, id=id))
        return self.contact_cache


        # for element in wd.find_elements_by_name("entry"):
        #     text = element.text
        #     id = element.find_element_by_name("selected[]").get_attribute("value")
        #     self.contact_cache.append(Contact(first_name=text, id=id))
        # return self.contact_cache





#-----------------------------------------------
#przed 4.11
        # def get_contact_list(self):
        #     wd = self.app.wd
        #     self.open_contact_page()
        #     contacts = []
        #     for element in wd.find_elements_by_name("entry"):
        #         text = element.text
        #         id = element.find_element_by_name("selected[]").get_attribute("value")
        #         contacts.append(Contact(first_name=text, id=id))
        #     return contacts









        # for element in wd.find_elements_by_css_selector("span.group"):
        #     text = element.text
        #     id = element.find_element_by_name("selected[]").get_attribute("value")
        #     groups.append(Group(name=text, id=id))
        # return groups
        #
        #     cells = element.find_elements_by_css_selector("td")
        #     #css_selector("tr.entry"):
        #     cells = element.cells
        #     cells = element.find_elements_by_css_selector("td")
        #     #id = element.find_element_by_name("selected[]").get_attribute("value")
        #     id = element.find_elements_by_css_selector("td").get_attribute("value")
        #     contacts.append(Contact(name=cells, id=id))
        # return contacts





        # to dziąła
        # for element in wd.find_elements_by_name("entry"):
        #     firstname = element.find_elements_by_css_selector("td")
        #     id = firstname[2].text
        #     contacts.append(Contact(firstname, id=id))
        # return contacts









    #----------------------------------------------------------------
    # def modyfied_contact(self, firstname):
    #     wd = self.app.wd
    #     self.select_first_contact()
    #     # open modification form
    #     wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
    #     # fill contact form
    #     wd.find_element_by_name("firstname").click()
    #     wd.find_element_by_name("firstname").clear()
    #     wd.find_element_by_name("firstname").send_keys(firstname)
    #     # submit modyfication
    #     wd.find_element_by_name("update").click()

class ContactHelper:

    def __init__ (self,app):
        self.app=app

    def create(self, contact):
        wd = self.app.wd
        # init group creation
        wd.find_element_by_link_text("add new").click()
        # fill group form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        # submit group creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session_contact import SessionHelper
from fixture.contact import ContactHelper

class ApllicationContact:
    def __init__(self):

        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
        self.session_contact=SessionHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def create_contact(self,contact):
        wd = self.wd
        # init new contact
        wd.find_element_by_link_text("add new").click()
        # fill contact
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        # submit new contact
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def destroy(self):
        self.wd.quit()
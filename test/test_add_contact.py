# -*- coding: utf-8 -*-
from model.contact import Contact
    
def test_add_contact(app):
    app.contact.create(Contact(first_name="python"))

def test_add_empty_contact(app):
    app.contact.create(Contact(first_name=""))




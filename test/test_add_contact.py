# -*- coding: utf-8 -*-
from model.contact import Contact
from sys import maxsize
    
def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact= Contact(first_name="python")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    def id_or_max(gr):
        if gr.id:
            return int (gr.id)
        else:
            return maxsize
    assert sorted(old_contacts, key=id_or_max) == sorted(new_contacts,key=id_or_max)

#kazął to wyłaćzyć
# def test_add_empty_contact(app):
#     old_contacts = app.contact.get_contact_list()
#     app.contact.create(Contact(first_name=""))
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) + 1 == len(new_contacts)








# wygląd po filmie 4.9
# def test_add_contact(app):
#     old_contacts = app.contact.get_contact_list()
#     app.contact.create(Contact(first_name="python"))
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) + 1 == len(new_contacts)
#
# def test_add_empty_contact(app):
#     old_contacts = app.contact.get_contact_list()
#     app.contact.create(Contact(first_name=""))
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) + 1 == len(new_contacts)

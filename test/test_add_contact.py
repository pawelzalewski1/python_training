# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="python")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def test_add_empty_contact(app):
#     old_contacts = app.contact.get_contact_list()
#     contact= Contact(first_name="")
#     app.contact.create(contact)
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) + 1 == len(new_contacts)
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


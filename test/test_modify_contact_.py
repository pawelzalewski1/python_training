from model.contact import Contact

def test_modify_contact_name(app):
    old_contacts = app.contact.get_contact_list()
    contact=Contact(first_name="new_first_name")
    contact.id=old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts)  == len(new_contacts)
    old_contacts[0]=contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_modify_contact_last_name(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(last_name="new_last_name")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0]=contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# w filmie to nie było modyfikowane ale dla zadania 11 trzeba było:
# def test_modify_contact_last_name(app):
#     old_contacts = app.contact.get_contact_list()
#     app.contact.modify_first_contact(Contact(last_name="new_last_name"))
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
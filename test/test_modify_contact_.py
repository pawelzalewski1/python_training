from model.contact import Contact

def test_modify_contact_name(app):
    # if app.contact.count()==0:
    #     app.contact.create(Contact(first_name="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(first_name="new_first_name"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts)  == len(new_contacts)

def test_modify_contact_last_name(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(last_name="new_last_name"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
from model.contact import Contact

def test_modify_contact_name(app):
    if app.contact.count()==0:
        app.contact.create(Contact(first_name="test"))
    app.contact.modify_first_contact(Contact(first_name="new_first_name"))

def test_modify_contact_last_name(app):
    app.contact.modify_first_contact(Contact(last_name="new_last_name"))
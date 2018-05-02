
def test_modyfied_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modyfied_contact(firstname="zalewski")
    app.session.logout()
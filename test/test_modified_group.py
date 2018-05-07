
def test_modyfied_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modyfied_group(name="change", header="change2", footer="change3")
    app.session.logout()
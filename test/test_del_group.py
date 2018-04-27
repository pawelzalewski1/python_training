
def test_delete_first_group1(app):
    app.session.login(username="admin")
    app.group.delete_first_group1()
    app.session.logout()
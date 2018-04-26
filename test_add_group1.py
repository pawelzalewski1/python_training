# -*- coding: utf-8 -*-

import pytest
from group import Group
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinlizer(fixture.destroy)
    return fixture

def test_add_group1(app):
        app.login(username="admin")
        app.create_group(Group(name="ddd", header="dddd", footer="ddd"))
        app.logout()

def test_add_empty_group1(app):
        app.login(username="admin")
        app.create_group(Group(name="", header="", footer=""))
        app.logout()
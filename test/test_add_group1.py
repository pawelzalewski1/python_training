# -*- coding: utf-8 -*-

import pytest

from fixture.application import Application
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group1(app):
        app.login(username="admin")
        app.create_group(Group(name="ddd", header="dddd", footer="ddd"))
        app.logout()

def test_add_empty_group1(app):
        app.login(username="admin")
        app.create_group(Group(name="", header="", footer=""))
        app.logout()
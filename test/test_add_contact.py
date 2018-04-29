# -*- coding: utf-8 -*-
import pytest

from fixture.application_contact import ApllicationContact
from model.contact import Contact
@pytest.fixture
def appc(request):
    fixture = ApllicationContact()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(appc):
    appc.session_contact.login(username="admin", password="secret")
    appc.contact.create(Contact(firstname="Pawel", lastname="Zalewski", address="Poland", email="test@mail.pl"))
    appc.session_contact.logout()

def test_add_empty_contact(appc):
    appc.session_contact.login(username="admin", password="secret")
    appc.contact.create(Contact(firstname="", lastname="", address="", email=""))
    appc.session_contact.logout()


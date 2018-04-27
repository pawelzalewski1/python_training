# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from application_contact import ApllicationContact

@pytest.fixture
def appc(request):
    fixture = ApllicationContact()
    request.addfinalizer(fixture.destroy)
    return fixture
    
def test_add_contact(appc):
        appc.login(username="admin", password="secret")
        appc.create_contact(Contact(firstname="Pawel", lastname="Zalewski", address="Poland",email="test@mail.pl"))
        appc.logout()

def test_add_empty_contact(appc):
        appc.login(username="admin", password="secret")
        appc.create_contact(Contact(firstname="", lastname="", address="",email=""))
        appc.logout()


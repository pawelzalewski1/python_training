# -*- coding: utf-8 -*-
import pytest

from fixture.application_contact import ApllicationContact
from model.contact import Contact



    
def test_add_contact(app):
        app.session_contact.login(username="admin", password="secret")
        app.contact.create(Contact(firstname="Pawel", lastname="Zalewski", address="Poland", email="test@mail.pl"))
        app.session_contact.logout()

def test_add_empty_contact(app):
        app.session_contact.login(username="admin", password="secret")
        app.contact.create(Contact(firstname="", lastname="", address="", email=""))
        app.session_contact.logout()


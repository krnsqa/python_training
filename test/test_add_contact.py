# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
        app.login(username="admin", password="secret")
        app.create_contact(Contact(firstname="sgsgsggs", lastname="dhdhdh", address="dhdhd", mobile="512-111-1111", email="ssgsgsg@gmail.com", bday="18", bmonth="September"))
        app.logout()


def test_add_empty_contact(app):
        app.login(username="admin", password="secret")
        app.create_contact(Contact(firstname="", lastname="", address="", mobile="", email="", bday="", bmonth=""))
        app.logout()



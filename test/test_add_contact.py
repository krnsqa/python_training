# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="sgsgsggs", lastname="dhdhdh", address="dhdhd", mobile="512-111-1111", email="ssgsgsg@gmail.com", bday="18", bmonth="September"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="", lastname="", address="", mobile="", email="", bday="", bmonth=""))
    app.session.logout()



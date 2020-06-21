# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="sgsgsggs", lastname="dhdhdh", address="dhdhd", mobile="512-111-1111", email="ssgsgsg@gmail.com"))


def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", lastname="", address="", mobile="", email=""))



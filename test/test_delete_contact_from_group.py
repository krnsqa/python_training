from fixture.orm import ORMFixture
from fixture.group import Group
from fixture.contact import Contact
import random


def test_delete_contact_from_group(app):

    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

    groups = db.get_group_list()
    if len(groups) == 0:
        app.group.create(Group(name="test"))
        groups = db.get_group_list()
    group = random.choice(groups)

    contacts = db.get_contacts_in_group(group)
    if len(contacts) == 0:
        contacts = db.get_contact_list()
        if len(contacts) == 0:
            contact = app.contact.create(Contact(firstname="test"))
            contacts = db.get_contact_list()
        contact = random.choice(contacts)
        app.contact.add_contact_to_group(contact, group)
        contacts = db.get_contacts_in_group(group)
    contact = random.choice(contacts)

    app.contact.delete_contact_from_group(group, contact)
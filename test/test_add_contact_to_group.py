from fixture.orm import ORMFixture
import random
from model.contact import Contact
from fixture.group import Group


def test_add_contact_to_group(app):

    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

    groups = db.get_group_list()
    if len(groups) == 0:
        app.group.create(Group(name="test"))
        groups = db.get_group_list()
    group = random.choice(groups)

    contacts = db.get_contacts_not_in_group(group)
    if len(contacts) == 0:
        app.contact.create(Contact(firstname="test"))
        contacts = db.get_contacts_not_in_group(group)
    contact = random.choice(contacts)

    app.contact.add_contact_to_group(contact, group)
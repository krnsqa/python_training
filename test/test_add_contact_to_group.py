from fixture.orm import ORMFixture
import random
from model.contact import Contact
from fixture.group import Group


def test_add_contact_to_group(app, db):

    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

    contacts = db.get_contact_list()
    if len(contacts) == 0:
        app.contact.create(Contact(firstname="test"))
    groups = db.get_group_list()
    if len(groups) == 0:
        app.group.create(Group(name="test"))

    contacts = db.get_contacts_without_groups()
    if len(contacts) != 0:
        contact_id = random.choice(contacts).id
        groups = db.get_group_list()
        group_id = random.choice(groups).id
        app.contact.add_contact_to_group(contact_id, group_id)
from fixture.orm import ORMFixture
import random
from model.contact import Contact
from fixture.group import Group



def test_add_contact_to_group(app, db):
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    contacts_list = db.get_contact_list()
    if len(contacts_list) == 0:
        app.contact.create(Contact(firstname="test"))
    groups_list = db.get_group_list()
    if len(groups_list) == 0:
        app.group.create(Group(name="test"))
    groups_list = db.get_group_list()
    group_id = random.choice(groups_list).id
    contacts_list = db.get_contacts_not_in_group(Group(id=group_id))
    contact_id = random.choice(contacts_list).id
    app.contact.add_contact_to_group(contact_id, group_id)



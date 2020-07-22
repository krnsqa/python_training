from fixture.orm import ORMFixture
import random
from fixture.group import Group



def test_delete_contact_from_group(app):
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    groups_list = db.get_group_list()
    group_id = random.choice(groups_list).id
    contacts_in_group = db.get_contacts_in_group(Group(id=group_id))
    if len(contacts_in_group) != 0:
        contact_id = random.choice(contacts_in_group).id
        app.contact.delete_contact_from_group(contact_id, group_id)
    else:
        pass
from fixture.orm import ORMFixture
import random


def test_delete_contact_from_group(app):

    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

    groups = db.get_groups_with_contacts()
    if len(groups) != 0:
        group_id = random.choice(groups).id
        app.contact.delete_contact_from_group(group_id)

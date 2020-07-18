from model.contact import Contact
import random

def test_modify_contact_firstname(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    new_contact = Contact(firstname="new firstname")
    new_contact.id = contact.id
    app.contact.modify_contact_by_id(contact.id, new_contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == app.contact.count()
    old_contacts.remove(contact)
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


#def test_modify_contact_lastname(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="test"))
#    old_contacts = app.contact.get_contact_list()
#    app.contact.modify_first_contact(Contact(lastname="new lastname"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)
from model.contact import Contact


def test_modify_contact_firstname(app):
    app.contact.modify_first_contact(Contact(firstname="new firstname"))


def test_modify_contact_lastname(app):
    app.contact.modify_first_contact(Contact(lastname="new lastname"))
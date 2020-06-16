from model.contact import Contact


def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="xxx", lastname="xxx", address="xxx", mobile="xxx-xxx-xxxx", email="xxxg@gmail.com", bday="1", bmonth="January"))
    app.session.logout()


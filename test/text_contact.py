import re
from model.contact import Contact



def test_all_contacts_on_homepage(app, db):
    ui_list = app.contact.get_contact_list()
    def clean(contact):
        return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip(),
                       address=contact.address.strip(), homephone=contact.homephone.strip(),
                       mobile=contact.mobile.strip(), workphone=contact.workphone.strip(),
                       email=contact.email.strip(), secondaryphone=contact.secondaryphone.strip())
    db_list = map(clean, db.get_contact_list())
    assert sorted(ui_list, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)
    for c in ui_list:
        for c in db_list:
            assert ui_list.firstname == db_list.firstname
            assert ui_list.lastname == db_list.lastname
            assert ui_list.address == db_list.address
            assert ui_list.all_emails_from_homepage == merge_emails_like_on_homepage(db_list)
            assert ui_list.all_phones_from_homepage == merge_phones_like_on_homepage(db_list)


def merge_emails_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            (map(lambda x: clear(x),
                                 filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3])))))


def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x!="",
                            (map(lambda x: clear(x),
                                 filter(lambda x: x is not None, [contact.homephone, contact.mobile,
                                                                  contact.workphone, contact.secondaryphone])))))


def clear(s):
    return re.sub("[() -]", "", s)
from model.contact import Contact
import random
import string


constant =[
    Contact(firstname="firstname1", lastname="lastname1", address="address1", homephone="homephone1", mobile="mobile1",
        workphone="workphone1", email="email1", secondaryphone="secondaryphone1"),
    Contact(firstname="firstname2", lastname="lastname2", address="address2", homephone="homephone2", mobile="mobile2",
        workphone="workphone2", email="email2", secondaryphone="secondaryphone2")
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


#OR
#testdata = [
    #Contact(firstname=firstname, lastname=lastname, address=address, homephone=homephone, mobile=mobile,
        #workphone=workphone, email=email, secondaryphone=secondaryphone)
        #for firstname in ["", random_string("fn", 10)]
        #for lastname in ["", random_string("ln", 10)]
        #for address in ["", random_string("adr", 10)]
        #for homephone in ["", random_string("hph", 10)]
        #for mobile in ["", random_string("mf", 10)]
        #for workphone in ["", random_string("wph", 10)]
        #for email in ["", random_string("em", 10)]
        #for secondaryphone in ["", random_string("sp", 10)]
#]


#OR
#testdata = [Contact(firstname="", lastname="", address="", mobile="", email="")] + [
    #Contact(firstname=random_string("fn", 10), lastname=random_string("ln", 10), address=random_string("adr", 10),
                    #homephone=random_string("hph", 10), mobile=random_string("mf", 10), workphone=random_string("wph", 10),
                    #email=random_string("em", 10), secondaryphone=random_string("sp", 10)) for i in range(3)]


#OR
testdata = [Contact(firstname=random_string("fn", 10), lastname=random_string("ln", 10), address=random_string("adr", 10),
                    homephone=random_string("hph", 10), mobile=random_string("mf", 10), workphone=random_string("wph", 10),
                    email=random_string("em", 10), secondaryphone=random_string("sp", 10)),
            Contact(firstname="", lastname="", address="", homephone="", mobile="", workphone="", email="", secondaryphone="")]


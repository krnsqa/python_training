from sys import maxsize


class Contact:

    def __init__(self, id=None, firstname=None, lastname=None, address=None,
                 homephone=None, mobile=None, workphone=None, secondaryphone=None, email=None):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.homephone = homephone
        self.mobile = mobile
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.email = email
        self.id = id


    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)


    def __eq__(self, other):
        return ((self.id is None or other.id is None or self.id == other.id) and
                self.firstname == other.firstname and
                self.lastname is None or other.lastname is None or self.lastname == other.lastname and
                self.homephone == other.homephone and self.mobile == other.mobile and
                self.workphone == other.workphone and self.secondaryphone == other.secondaryphone)


    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
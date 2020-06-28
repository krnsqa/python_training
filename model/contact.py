from sys import maxsize


class Contact:

    def __init__(self, id=None, firstname=None, lastname=None, address=None, mobile=None, email=None):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.mobile = mobile
        self.email = email
        self.id = id


    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s" % (self.id, self.firstname, self.lastname,  self.address, self.mobile, self.email,)


    def __eq__(self, other):
        return ((self.id is None or other.id is None or self.id == other.id) and
                self.firstname == other.firstname and
                self.lastname == other.lastname and
                self.address == other.address and
                self.mobile == other.mobile and
                self.email == other.email)



    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
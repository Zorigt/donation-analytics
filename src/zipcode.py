import year

class Zipcode(object):
    condition = 'New'

    def __init__(self, zipcode):
        self.zipcode = zipcode
        self.years = []

    def drive(self):
        self.condition = 'Used'
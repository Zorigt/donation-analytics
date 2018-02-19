class Year(object):
    condition = 'New'
    def __init__(self,year):
        self.year = year
        self.amounts = []
        self.percentile = 0
        self.sum = 0


    def drive(self):
        self.condition = 'Used'

class RecipientZipcodeYear(object):

    def __init__(self,cmte_id_zipcode_year):
        self.cmte_id_zipcode_year = cmte_id_zipcode_year
        self.amounts = []
        self.percentile = 0
        self.sum = 0


    def addAmt(self, amt):
        self.amounts.append(amt)
        print(self.amounts)

    def getSum(self):
        return self.sum

    def getPercentile(self):
        return self.percentile
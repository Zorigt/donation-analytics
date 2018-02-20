from bisect import insort

class RecipientZipcodeYear(object):

    def __init__(self,id_zipcode_year, first_amt, percentile):
        self.id_zipcode_year = id_zipcode_year
        self.percentile = percentile
        self.amounts = [first_amt]
        self.percentile_amt = first_amt
        self.sum = first_amt

    def findPercentile(self):
        n = max(int(round(self.percentile/100 * len(self.amounts) + 0.5)), 1)
        return self.amounts[n - 1]

    def updateAmount(self, amt):
        insort(self.amounts, amt)
        self.sum += amt
        self.percentile_amt = self.findPercentile()

    def getResults(self):
        # remove cents from percentile amount and sum
        results_percentile_amt = self.percentile_amt if self.percentile_amt - int(self.percentile_amt)  > 0 else int(self.percentile_amt)
        results_sum = self.sum if self.sum - int(self.sum) > 0 else int(self.sum)
        return [results_percentile_amt, results_sum, len(self.amounts)]


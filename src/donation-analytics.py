import argparse
import os
import recipient_zipcode_year
from helpers import check_donation, validate_value


def getPercentile(input_percentile):
    file = open(os.path.join(os.pardir, input_percentile), "r")
    percentile = file.readline()
    if (percentile == '' or int(percentile) > 100 or int(percentile) < 0):
        raise AssertionError("Unexpected value in percentile.txt!", percentile)
    else:
        return percentile

if __name__ == "__main__":

    # Parameters
    parser = argparse.ArgumentParser()
    parser.add_argument("INPUT_ITCONT")
    parser.add_argument("INPUT_PERCENTILE")
    parser.add_argument("OUTPUT_REPEAT_DONORS")
    args = parser.parse_args()

    percentile = getPercentile(args.INPUT_PERCENTILE)

    year_array = [[0 for x in range(10)] for y in range(4)] # [A-Z] and [0-9]
    zipcode_array = [[0 for x in range(10)] for y in range(5)] # [0-9]
    name_array = [] # item string type contains [A-Z] and comma and space

    with open(os.path.join(os.pardir, args.INPUT_ITCONT), "r") as donations:
        for donation in donations:
            donation_array= donation.split("|")
            if donation_array[15] == '':
                recipient = validate_value.validateValue(donation_array[0], 'recipient')
                zipcode = validate_value.validateValue(donation_array[10], 'zipcode')
                year = validate_value.validateValue(donation_array[13], 'year')
                name = validate_value.validateValue(donation_array[7], 'name')
                amount = validate_value.validateValue(donation_array[14], 'amount')

                if recipient and zipcode and year and name and amount:
                    concise_donation_array = [recipient, zipcode, year, name]
                    # found_recipient is not necessary
                    found_zipcode, found_name, found_prev_yr_don = check_donation.checkDonation(concise_donation_array, zipcode_array, year_array, name_array)
                    if found_zipcode != '' and found_name != '' and found_prev_yr_don != '':
                        print(found_zipcode, found_name, found_prev_yr_don)
                        temp = recipient_zipcode_year.RecipientZipcodeYear(found_zipcode)
                        a = recipient + found_zipcode
                        print('the object =',a)
                        if a != '':
                            exec(a + "= temp")
                            print(eval(a).addAmt('12345'))
                            #print(a.zipcode)

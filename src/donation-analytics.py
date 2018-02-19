import argparse
import os
from decimal import Decimal
import recipient_zipcode_year
from helpers import check_donation, validate_value
import time


def getPercentile(input_percentile):
    file = open(os.path.join(os.pardir, input_percentile), "r")
    percentile = file.readline()
    if (percentile == '' or int(percentile) > 100 or int(percentile) < 0):
        raise AssertionError("Unexpected value in percentile.txt!", percentile)
    else:
        return percentile

if __name__ == "__main__":
    start_time = time.time()
    print(start_time)

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

    with open(os.path.join(os.pardir, args.INPUT_ITCONT), "r") as donations, \
            open(os.path.join(os.pardir, args.OUTPUT_REPEAT_DONORS), "w") as repeat_donors:
        row_counter = 0
        for donation in donations:
            if row_counter == 1000000 or row_counter == 2000000 or row_counter == 3000000 or row_counter == 4000000 or \
                row_counter == 5000000 or row_counter == 6000000 or row_counter == 7000000 or row_counter == 7900000:
                print('row count and minutes',row_counter, (time.time() - start_time)/60)
            row_counter += 1
            donation_array= donation.split("|")
            if donation_array[15] == '':
                recipient = validate_value.validateValue(donation_array[0], 'recipient')
                zipcode = validate_value.validateValue(donation_array[10], 'zipcode')
                year = validate_value.validateValue(donation_array[13], 'year')
                name = validate_value.validateValue(donation_array[7], 'name')
                amount = validate_value.validateValue(donation_array[14], 'amount')

                if recipient and zipcode and year and name and amount:
                    concise_donation_array = [recipient, zipcode, year, name]
                    found_zipcode, found_name, found_prev_yr_don = check_donation.checkDonation(concise_donation_array, zipcode_array, year_array, name_array)
                    if recipient != '' and found_zipcode != '' and found_name != '' and found_prev_yr_don != '':
                        # print(found_zipcode, found_name, found_prev_yr_don)

                        obj_name = recipient + found_zipcode + year

                        try:
                            eval(obj_name)
                        except NameError:
                            temp = recipient_zipcode_year.RecipientZipcodeYear(obj_name, float(amount), float(percentile))
                            exec (obj_name + "= temp")
                        else:
                            eval(obj_name).updateAmount(float(amount))

                        results = eval(obj_name).getResults()
                        percentile_amt, sum, amt_count = [str(z) for z in results]
                        output_line = recipient+'|'+zipcode+'|'+year+'|'+percentile_amt+'|'+sum+'|'+amt_count+'\n'
                        # print(output_line)
                        repeat_donors.write(output_line)

    print((time.time() - start_time)/60)
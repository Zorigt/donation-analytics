import argparse
import os
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

    name_array = [] # item string type contains [A-Z] and comma and space
    zipcode_name_year_set = set()
    recipient_set = set()  # in file itcont.txt
    found_repeat_donor = ''

    with open(os.path.join(os.pardir, args.INPUT_ITCONT), "r") as donations, \
            open(os.path.join(os.pardir, args.OUTPUT_REPEAT_DONORS), "w") as repeat_donors:
        row_counter = 0
        for donation in donations:
            if row_counter%10000 == 0:
                print('row count at 1k and minutes',row_counter, (time.time() - start_time)/60)
            row_counter += 1
            donation_array= donation.split("|")
            if donation_array[15] == '':
                recipient = validate_value.validateValue(donation_array[0], 'recipient')
                zipcode = validate_value.validateValue(donation_array[10], 'zipcode')
                year = validate_value.validateValue(donation_array[13], 'year')
                name = validate_value.validateValue(donation_array[7], 'name')
                amount = validate_value.validateValue(donation_array[14], 'amount')

                if (recipient and zipcode and year and name and amount) != '':
                    recipient_set.add(recipient)
                    zipcode_name_year_set.add(zipcode+name+year)
                    concise_donation_array = [zipcode, name, year, recipient]
                    found_repeat_donor = check_donation.checkDonation(concise_donation_array, zipcode_name_year_set, recipient_set)

                    if found_repeat_donor != '':
                        obj_name = recipient + zipcode + year

                        try:
                            eval(obj_name)
                        except NameError:
                            temp = recipient_zipcode_year.RecipientZipcodeYear(obj_name, float(amount), float(percentile))
                            exec (obj_name + "= temp")
                        else:
                            eval(obj_name).updateAmount(float(amount))

                        results = eval(obj_name).getResults()
                        percentile_amt, sum, amt_count = [str(z) for z in results]
                        output_line = recipient + '|' + zipcode + '|' + year + '|' + percentile_amt + '|' + sum + '|' + amt_count + '\n'
                        #print(output_line)
                        repeat_donors.write(output_line)

    #for i in array_of_tuples:
     #   pass
    donations.close()
    repeat_donors.close()
    print((time.time() - start_time)/60)
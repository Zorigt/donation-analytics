import argparse
import os
import recipient_zipcode_year
from helpers import check_donation, validate_value, search, ordered_sort
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
    repeat_donors_array = []

    with open(os.path.join(os.pardir, args.INPUT_ITCONT), "r") as donations, \
            open(os.path.join(os.pardir, args.OUTPUT_REPEAT_DONORS), "w") as repeat_donors:
        row_counter = 0
        for donation in donations:
            if row_counter%1000 == 0:
                print('Row reads by 1k:',row_counter, 'Time past in secs/60 (mins):', (time.time() - start_time)/60)
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
                        # check first if found_repeat_donor object was created
                        repeat_donor_exists = search.binarySearch(repeat_donors_array, found_repeat_donor)
                        if repeat_donor_exists:
                            repeat_donor_exists.updateAmount(float(amount))
                            result_obj = repeat_donor_exists
                        else:
                            # insert the donor into a sorted array
                            insert_index = ordered_sort.orderedInsert(repeat_donors_array, found_repeat_donor)

                            temp = recipient_zipcode_year.RecipientZipcodeYear(found_repeat_donor, float(amount),
                                                                               float(percentile))
                            repeat_donors_array[insert_index-1:insert_index-1] = [temp]
                            result_obj = temp


                        results = result_obj.getResults()
                        percentile_amt, sum, amt_count = [str(z) for z in results]
                        output_line = recipient + '|' + zipcode + '|' + year + '|' + percentile_amt + '|' + sum + '|' + amt_count + '\n'
                        # print(output_line)
                        repeat_donors.write(output_line)

    donations.close()
    repeat_donors.close()
    print('total minutes: ',(time.time() - start_time)/60)
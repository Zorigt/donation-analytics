import argparse
#python ./src/donation-analytics.py ./input/itcont.txt ./input/percentile.txt ./output/repeat_donors.txt
import os
import re
import datetime
from bisect import bisect_right, bisect_left, insort_right, insort


def getPercentile(input_percentile):
    file = open(os.path.join(os.pardir, input_percentile), "r")
    percentile = file.readline()
    if (percentile == '' or int(percentile) > 100 or int(percentile) < 0):
        raise AssertionError("Unexpected value in percentile.txt!", percentile)
    else:
        return percentile

# valid return the value, or return null string
def validateValue(value, valueType):
    validated_value = ''
    if valueType == 'recipient':
        pattern = re.compile("^\w+$")
        if pattern.match(value) and len(value) == 9:
            validated_value = value
    elif valueType == 'zip':
        pattern = re.compile("^\d+$")
        if pattern.match(value) and len(value) >= 5:
            validated_value = value[:5]
    elif valueType == 'year':
        try:
            datetime.datetime(year=int(value[4:]),month=int(value[:2]),day=int(value[2:4]))
            correctDate = True
        except ValueError:
            correctDate = False
        pattern = re.compile("^\d+$")
        if pattern.match(value) and len(value) == 8 and correctDate:
            validated_value = value[4:]
    elif valueType == 'name':
        pattern = re.compile("^([a-zA-Z]+)[,]([a-zA-Z\s]+)+$")
        if pattern.match(value):
            validated_value = value
    elif valueType == 'amount':
        pattern = re.compile("^\d*[.]?\d{0,2}$")
        if pattern.match(value):
            validated_value = value
    return validated_value


def checkDonation(array_donation, alpha_num_array, num_array, name_array):
    track_recipient = 0 # return 9 if found otherwise not found. There are 9 char counts for found recipient
    track_name = 0 # return 1 if found and 0 for not found. bisection search index found from the name
    track_zip_year = 0 # return 9 if found otherwise not found. There are 9 counts for found zip (5 chars) and year (4 chars)
    track_prev_yr_don = 0 # return 4 if previous year donation found, otherwise not found

    recipient = validateValue(array_donation[0], 'recipient')
    zip = validateValue(array_donation[10], 'zip')
    year = validateValue(array_donation[13], 'year')
    name = validateValue(array_donation[7], 'name')
    amount = validateValue(array_donation[14], 'amount')

    if recipient and zip and year and name and amount:
        # check recipient value
        for i, char in enumerate(recipient):
            # 48 is '0' and 57 is '9'
            if ord(char) >= 48 and ord(char) <= 57:
                track_recipient += alpha_num_array[i][ord(char)-48]
                alpha_num_array[i][ord(char)-48] = 1
            # 65 is 'A' and 90 is 'Z'
            elif ord(char) >= 65 and ord(char) <= 90:
                track_recipient += alpha_num_array[i][ord(char) - 55]
                alpha_num_array[i][ord(char) - 55] = 1

        # check name value in name_array
        i = bisect_left(name_array, name)
        if len(name_array) == 0:
            name_array.insert(0, name)
        elif i == len(name_array):
            name_array.insert(i, name)
        elif name_array[i] != name:
            name_array.insert(i, name)
        else:
            track_name = 1

        # check zip and year values together
        zip_year = zip + year
        for i, char in enumerate(zip_year):
            # 48 is '0' and 57 is '9'
            if ord(char) >= 48 and ord(char) <= 57:
                track_zip_year += num_array[i][ord(char) - 48]
                num_array[i][ord(char) - 48] = 1

        if track_name == 1:
            prev_year = str(int(year) - 1)
            prev_year_array = [int(prev_year[:1]),int(prev_year[1:2]),int(prev_year[2:3]),int(prev_year[3:])] # split the year digits
            x = 5 # 4 digit year index starts at 5 and ends at 9
            for y in prev_year_array:
                track_prev_yr_don += num_array[x][y]
                x+=1


    found_recipient = track_recipient == 9
    found_name = track_name == 1
    found_zip_year = track_zip_year == 9
    found_prev_yr_don = track_prev_yr_don == 4
    print(track_recipient,track_name,track_zip_year, track_prev_yr_don)
    return [found_recipient, found_name, found_zip_year, found_prev_yr_don]


if __name__ == "__main__":

    # Parameters
    parser = argparse.ArgumentParser()
    parser.add_argument("INPUT_ITCONT")
    parser.add_argument("INPUT_PERCENTILE")
    parser.add_argument("OUTPUT_REPEAT_DONORS")
    args = parser.parse_args()

    percentile = getPercentile(args.INPUT_PERCENTILE)

    alpha_num_array = [[0 for x in range(36)] for y in range(9)] # [A-Z] and [0-9]
    num_array = [[0 for x in range(10)] for y in range(9)] # [0-9]
    name_array = [] # item string type contains [A-Z] and comma and space

    with open(os.path.join(os.pardir, args.INPUT_ITCONT), "r") as donations:
        for donation in donations:
            array_donation= donation.split("|")
            if array_donation[15] == '':
                found_recipient, found_name, found_zip_year, found_prev_yr_don = checkDonation(array_donation, alpha_num_array, num_array, name_array)
                print(bool(found_recipient), bool(found_name), bool(found_zip_year), bool(found_prev_yr_don))

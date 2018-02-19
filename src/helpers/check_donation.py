import validate_value
from bisect import bisect_left

def checkDonation(concise_donation_array, zipcode_array, year_array, name_array):
    zipcode = concise_donation_array[1]
    year = concise_donation_array[2]
    name = concise_donation_array[3]

    track_name = 0 # return 1 if found and 0 for not found. bisection search index found from the name
    track_zipcode = 0 # return 5 if found otherwise not found. There are 5 counts for found zipcode (5 chars)
    track_year = 0
    track_prev_yr_don = 0 # return 4 if previous year donation found, otherwise not found


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

    # check zipcode
    for i, char in enumerate(zipcode):
        # 48 is '0' and 57 is '9'
        if ord(char) >= 48 and ord(char) <= 57:
            track_zipcode += zipcode_array[i][ord(char) - 48]
            zipcode_array[i][ord(char) - 48] = 1

    # check year
    for i, char in enumerate(year):
        # 48 is '0' and 57 is '9'
        if ord(char) >= 48 and ord(char) <= 57:
            track_year += year_array[i][ord(char) - 48]
            year_array[i][ord(char) - 48] = 1

    # if name already exisits then check if they made donations in the previous year
    if track_name == 1:
        prev_year = str(int(year) - 1)
        prev_year_array = [int(prev_year[:1]),int(prev_year[1:2]),int(prev_year[2:3]),int(prev_year[3:])] # split the year digits
        x = 0
        for y in prev_year_array:
            track_prev_yr_don += year_array[x][y]
            x+=1

    found_name = name if track_name == 1 else ''
    found_zipcode = zipcode if track_zipcode == 5 else ''
    found_prev_yr_don = prev_year if track_prev_yr_don == 4 else ''

    print(track_zipcode, track_name, track_prev_yr_don)
    return [found_zipcode, found_name, found_prev_yr_don]

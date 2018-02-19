import validate_value
from bisect import bisect_left

def checkDonation(concise_donation_array, alpha_num_array, num_array, name_array):
    recipient = concise_donation_array[0]
    zipcode = concise_donation_array[1]
    year = concise_donation_array[2]
    name = concise_donation_array[3]

    track_recipient = 0 # return 9 if found otherwise not found. There are 9 char counts for found recipient
    track_name = 0 # return 1 if found and 0 for not found. bisection search index found from the name
    track_zipcode_year = 0 # return 9 if found otherwise not found. There are 9 counts for found zipcode (5 chars) and year (4 chars)
    track_prev_yr_don = 0 # return 4 if previous year donation found, otherwise not found


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

    # check zipcode and year values together
    zipcode_year = zipcode + year
    for i, char in enumerate(zipcode_year):
        # 48 is '0' and 57 is '9'
        if ord(char) >= 48 and ord(char) <= 57:
            track_zipcode_year += num_array[i][ord(char) - 48]
            num_array[i][ord(char) - 48] = 1

    if track_name == 1:
        prev_year = str(int(year) - 1)
        prev_year_array = [int(prev_year[:1]),int(prev_year[1:2]),int(prev_year[2:3]),int(prev_year[3:])] # split the year digits
        x = 5 # 4 digit year index starts at 5 and ends at 9
        for y in prev_year_array:
            track_prev_yr_don += num_array[x][y]
            x+=1


    found_recipient = recipient if track_recipient == 9 else ''
    found_name = name if track_name == 1 else ''
    found_zipcode_year = zipcode_year if track_zipcode_year == 9 else ''
    found_prev_yr_don = prev_year if track_prev_yr_don == 4 else ''
    print(track_recipient,track_zipcode_year, track_name, track_prev_yr_don)
    return [found_recipient, found_zipcode_year, found_name, found_prev_yr_don]

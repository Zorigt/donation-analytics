
def checkDonation(concise_donation_array, zipcode_name_year_set, recipient_set):
    zipcode = concise_donation_array[0]
    name = concise_donation_array[1]
    year = concise_donation_array[2]
    recipient = concise_donation_array[3]

    found_repeat_donor = ''

    # check zipcode name value in name_set
    zipcode_name_prev_year = zipcode + name + str(int(year)-1)
    if zipcode_name_prev_year in zipcode_name_year_set and recipient in recipient_set:
        found_repeat_donor = zipcode_name_prev_year

    return found_repeat_donor

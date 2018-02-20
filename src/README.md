1- read file paths
1a parse line by line
1b check valids and regex name and number and dates

2- construct a global matrix 36x9 - why need if b-tree finds it? 
                        A: no need to create more objects
2a no means insert into matrix
insert cmt, zip, year, name if no

2b yes means create repeat_don obj yyyy & udpate sum in binary trees
if zip, year-1, and name exist
insert cmt, zip, year, name, sum

3- construct binary sort tree - bisect
3a object 
    cd_id to ASCII binary
    zip as int binary
    yyyy as int insert sort
    
    C00384516028952018
    67 48 48 51 56 52 53 49 54 48 50 56 57 53 50 48 49 56 
    67 48 48 51 56 52 53 49 54 0 2 8 9 5 2 0 1 8 
    C00384516028952017
    67 48 48 51 56 52 53 49 54 48 50 56 57 53 50 48 49 55 
    
    list of dec -> insert sort?
    percentile
    running total


with open(INPUT_ITCONT, "r") as intcont:
    array = []
    for line in intcont:
        array.append(line)

    donation = intcont.readline()

    while donation != eof:


        repeat_donors = open(OUTPUT_REPEAT_DONORS, "w")

        file.write("Hello World")

        file.close()

(0, '=', 'C00384818')
(7, '=', 'ABBOTT, JOSEPH')
(10, '=', '028956146') zip
(13, '=', '01122017')
(14, '=', '250') amt

0,7,10,13,14

        pattern = re.compile("^([A-Z][0-9]+)+$")

#python ./src/donation-analytics.py ./input/itcont.txt ./input/percentile.txt ./output/repeat_donors.txt

if prev_year: 
if c == obj:
    find c and update - use var value as var
    how to find c? in list or directly
    for i in ary:
        i == c
else:
    c = recipient.Recipeient(c,zipcode,name,year,amt)
    
    
    print('the object =',a)
                        if a != '':
                            exec(a + "= temp")
                            print(eval(a).addAmt('12345'))
                            #print(a.zipcode)
                            
                            
     recipient_set.add(recipient)
                    if year not in year_set:
                        year_set.add(year)
                        temp2 = "zipcode_name_" + year + "_set"
                        exec ("zipcode_name_" + year + "_set = set()")
                    exec ("zipcode_name_" + year + "_set.add(zipcode+name)")
                    prev_year = str(int(year)-1)
                    if prev_year not in year_set:
                        exec ("eval(temp2) = set()")
                    # exec ("zipcode_name_" + prev_year + "_set = set()")
                    # exec (zipcode_name_prev_year_set + " = eval(temp2)")
                    concise_donation_array = [zipcode, name, year, recipient]
                    found_repeat_donor = check_donation.checkDonation(concise_donation_array, eval(temp2), recipient_set)
                    
                    
                if found_repeat_donor != '':
                        # check first if found_repeat_donor object was created
                        try:
                            eval(found_repeat_donor)
                        except NameError:
                            # use the object directly name rather than creating another set or list storing the objects
                            # this approach will save time on looking up the object in a set or a list
                            # the object's name is inside, i.e., found_repeat_donor = C00030718727622017 for C00030718|72762|2017|
                            temp = recipient_zipcode_year.RecipientZipcodeYear(found_repeat_donor, float(amount), float(percentile))
                            exec (found_repeat_donor+ "= temp")
                        else:
                            # if the object is already created then just add the amount to the object
                            eval(found_repeat_donor).updateAmount(float(amount))

                        results = eval(found_repeat_donor).getResults()
                        percentile_amt, sum, amt_count = [str(z) for z in results]
                        output_line = recipient + '|' + zipcode + '|' + year + '|' + percentile_amt + '|' + sum + '|' + amt_count + '\n'
                        #print(output_line)
                        repeat_donors.write(output_line)
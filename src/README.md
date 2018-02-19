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
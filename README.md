I tested my code on Python 2.7

Description of the code logic

1- read percentile file

2- open itcont.txt file and read line by line

3- open output file 

4- validate all fields: recipient, name, zipcode, year

5- check if the zipcode and name have been detected previously in zipcode_name_year_set

6- check if the recipient has been detected previously in recipient_set

7- results from steps 5 & 6 determine if the donnor is a repeat donor

8a- If repeat donor is found, then perform a binary search for the recipient_zipcode_year object by attribute id_zipcode_year

8b- If the object already created then update it with the donation amount

9a- If not found then create a new object with the zipcode and name 

9b- Insert the new object into a sorted list by attribute id_zipcode_year

10- Capture the output line in the results variable from either step 8 or 9 and write to output file

Results
Binary search and ordered insert - 20 minutes 62 seconds

Hash table - 20 minutes 86 seconds

I went with the first option as there was 24 second improvement. 

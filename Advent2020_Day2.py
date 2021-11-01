# -*- coding: utf-8 -*-
"""
Spyder Editor

This is to solve day #02 of the Advent of Code 2020
https://adventofcode.com/2020/day/2


These are the details:
--- Day 2: Password Philosophy ---
Your flight departs in a few days from the coastal airport; 
the easiest way down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. 
"Something's wrong with our computers; 
we can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: 
some of the passwords wouldn't have been allowed by the 
Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) 
of passwords (according to the corrupted database) 
and the corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password. 
The password policy indicates the lowest and highest number of times a given 
letter must appear for the password to be valid. 
For example, 1-3 a means that the password must contain a 
at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. 
The middle password, cdefg, is not; 
it contains no instances of b, but needs at least 1. 
The first and third passwords are valid: they contain one a or nine c, 
both within the limits of their respective policies.

How many passwords are valid according to their policies?


Part 2 of the puzzle:
While it appears you validated the passwords correctly, 
they don't seem to be what the Official Toboggan Corporate 
Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally 
explained the password policy rules from his old job at the 
sled rental place down the street! 
The Official Toboggan Corporate Policy actually works a little differently.

Each policy actually describes two positions in the password, 
where 1 means the first character, 
2 means the second character, and so on. 
(Be careful; Toboggan Corporate Policies have no concept of "index zero"!) 
Exactly one of these positions must contain the given letter. 
Other occurrences of the letter are irrelevant 
for the purposes of policy enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
How many passwords are valid according to the new interpretation of the policies?    


"""


import csv

database = csv.reader(
    open("advent_day2.txt"))


# The first puzzle
policy_passed = 0

for row in database:
    # print ("--------------------")
    # print (row)
    row_str = str(row)
    # print (row_str.index("-"))
    # Skip the first two characters "['"
    # read till the "-"
    min_policy=int(row_str[2:row_str.index("-")])
    # print (min_policy)
    # Then read the next character to "-"
    # .. until the whitespade
    max_policy=int(row_str[row_str.index("-")+1:row_str.index(" ")])
    # print (max_policy)
    # Read the policy character ...
    # .. by searching for the ":"
    policy_char=(row_str[row_str.index(":")-1:row_str.index(":")])
    # print (policy_char)
    # Now extract the password
    password = row_str[row_str.index(":")+2:len(row_str)-2]
    # print(password)
    # Now count the policy character in the string
    
    # print(password.count(policy_char))
    
    if (password.count(policy_char) >= min_policy) and (password.count(policy_char) <= max_policy):
        # print (row)
        # print ("Found a match !")
        policy_passed = policy_passed +1
print ("Password matches - 1. puzzle: ", policy_passed )
# The correct answer is : 515 !
        

# The second puzzle
database = csv.reader(
    open("advent_day2.txt"))

policy_passed = 0

for row in database:
    # print ("--------------------")
    # print (row)
    row_str = str(row)
    # print (row_str.index("-"))
    # Skip the first two characters "['"
    # read till the "-"
    position_1=int(row_str[2:row_str.index("-")])
    #print (position_1)
    # Then read the next character to "-"
    # .. until the whitespade
    position_2=int(row_str[row_str.index("-")+1:row_str.index(" ")])
    #print (position_2)
    # Read the policy character ...
    # .. by searching for the ":"
    policy_char=(row_str[row_str.index(":")-1:row_str.index(":")])
    #print (policy_char)
    # Now extract the password
    password = row_str[row_str.index(":")+2:len(row_str)-2]
    #rint(password)
    # Now count the policy character in the string
    position_1_char = password[position_1-1]
    #print (position_1_char)
    position_2_char = password[position_2-1]
    #print (position_2_char)
    
    
    # Does the first character match ?
    #if (position_1_char ==  policy_char):
        #print ("First position matches")
    #if (position_2_char ==  policy_char):
        #print ("Second position matches")


    if ((position_1_char ==  policy_char) and (position_2_char !=  policy_char)) or ((position_1_char !=  policy_char) and (position_2_char ==  policy_char)):
        policy_passed = policy_passed+1
        #print ("Actual match found")
        
print ("Password matches - 2. puzzle: ", policy_passed )
# The correct number is 711



# Sources for help
# https://www.kite.com/python/examples/3281/csv-read-a-csv-file-and-ignore-spaces-after-delimiters
# https://python-reference.readthedocs.io/en/latest/docs/str/split.html
# https://youtu.be/rfscVS0vtbw
# https://www.freecodecamp.org/news/how-to-substring-a-string-in-python/
    

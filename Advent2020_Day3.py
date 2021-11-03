# -*- coding: utf-8 -*-
"""
Spyder Editor

This is to solve day #03 of the Advent of Code 2020
https://adventofcode.com/2020/day/3


These are the details:
Part 1:
--- Day 3: Toboggan Trajectory ---
With the toboggan login problems resolved, you set off toward the airport. 
While travel by toboggan might be easy, it's certainly not safe: 
there's very minimal steering and the area is covered in trees. 
You'll need to see which angles will take you near the fewest trees.

Due to the local geology, trees in this area only grow on exact integer 
coordinates in a grid. 
You make a map (your puzzle input) of the open squares (.) and trees (#) 
you can see. For example:

..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
These aren't the only trees, though; due to something you read about once 
involving arboreal genetics and biome stability, 
the same pattern repeats to the right many times:

..##.........##.........##.........##.........##.........##.......  --->
#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........#.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...##....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
You start on the open square (.) in the top-left corner and need to reach 
the bottom (below the bottom-most row on your map).

The toboggan can only follow a few specific slopes (you opted for a 
cheaper model that prefers rational numbers); 
start by counting all the trees you would encounter 
for the slope right 3, down 1:

From your starting position at the top-left, 
check the position that is right 3 and down 1. 
Then, check the position that is right 3 and down 1 from there, 
and so on until you go past the bottom of the map.

The locations you'd check in the above example are marked here with O 
where there was an open square and X where there was a tree:

..##.........##.........##.........##.........##.........##.......  --->
#..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........X.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...#X....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->

My try:
..##.........##.........##.........##.........##.........##.......  --->
#..0#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....1..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#0#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..2...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.3#.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#.0..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........4.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.5#...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...#6....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...7.#.#..#...#.#.#..#...#.#.#..#...#.#  --->



In this example, traversing the map using this slope would cause 
you to encounter 7 trees.

Starting at the top-left corner of your map and following 
a slope of right 3 and down 1, how many trees would you encounter?    

"""

# f = open("Advent2020_Day3Easy.txt", "r")
f = open("Advent2020_Day3.txt", "r")

map=f.readlines()
f.close()

# print (map)

# map ist a list of strings
# for row in map: 
    # print (row)

# we can print the first line
# print (map[0])

# and we can print the first char
# print (map[0][0])


# print ("Number of rows ",  len(map))
# print ("Number of columns ", len(map[0]))


# we start at [0][0]
# then we go to [1][3]
# then we go to [2][6]

# iterate through all rows
col = 0
hits = 0
for i in range(len(map)-1):
    col=col+3
    col = col % (len(map[0])-1)
#    print(i+1,col, map[i+1][col])
    if (map[i+1][col] == "#"  ):
        hits = hits +1
#        print ("Hit !")

print ("Total hits", hits)

# The correct answer is 272 hits

"""
# the second part
Time to check the rest of the slopes - you need to minimize the 
probability of a sudden arboreal stop, after all.

Determine the number of trees you would encounter if, 
for each of the following slopes, you start at the top-left corner and 
traverse the map all the way to the bottom:

Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) 
respectively; multiplied together, these produce the answer 336.

What do you get if you multiply together the number of trees 
encountered on each of the listed slopes?
"""

# This is to count when row increments by 1
def count_trees (increment):
    col = 0
    hits = 0
    for i in range(len(map)-1):
        col=col+increment
        col = col % (len(map[0])-1)
        # print(i+1,col, map[i+1][col])
        if (map[i+1][col] == "#"  ):
            hits = hits +1
            # print ("Hit !")
    return hits

    

print (count_trees(1)) # answer 85
print (count_trees(3)) # answer 272
print (count_trees(5)) # answer 66
print (count_trees(7)) # answer 73

print ("The product is so far ", 
       count_trees(1)*count_trees(3)*count_trees(5)*count_trees(7) )
       # answer 111392160


# This is to count with row & column increments
def count_trees2 (col_inc, row_inc):
    col = 0
    hits = 0
    i=0
    while i < len(map)-1:
        col=col+col_inc
        col = col % (len(map[0])-1)
        
        # print(i+1,col, map[i][col])
        if (map[i+1][col] == "#"  ):
            hits = hits +1
            # print ("Hit !")
        i=i+row_inc
    return hits

print ("The product is so far ", 
       count_trees2(1,1)*count_trees2(3,1)*count_trees2(5,1)*count_trees2(7,1) )

print ("The last product is ", count_trees2(1,2))
# my result 38
# counted 34 -> 3787333440 is too low
# The correct answer is 3898725600  that would mean the last value is 35 
# MY CODE DOES NOT WORK CORRECTLY !

print ("The FINAL product is ", 
       count_trees2(1,1)*count_trees2(3,1)*count_trees2(5,1)*count_trees2(7,1) * count_trees2(1,2))

print ("BUT: This is wrong! The correct answer is 3898725600") 
print ("This is remarkable since the correct value is given for the simple example") 
print ("My algo counts for the last slope Right 1 Down 2 38 trees but the correct value is 35") 
print ("It means that the function count_trees2 doesn't work correctly") 
       





"""
Helper
 https://youtu.be/rfscVS0vtbw
 https://docs.python.org/3/tutorial/datastructures.html
 https://realpython.com/python-strings/
"""








#COLORS OF DRESS BY WORKERS AT BINCOM ICT FOR THE WEEK

Monday = ['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'BLUE', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN']


Tuesday = ['ARSH', 'BROWN', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLUE', 'PINK', 'PINK', 'ORANGE', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'WHITE', 'BLUE', 'BLUE', 'BLUE']

WEDNESDAY = ['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'RED', 'YELLOW', 'ORANGE', 'RED', 'ORANGE', 'RED', 'BLUE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'WHITE', 'WHITE']

THURSDAY = ['BLUE', 'BLUE', 'GREEN', 'WHITE', 'BLUE', 'BROWN', 'PINK', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN']

FRIDAY = ['GREEN', 'WHITE', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLACK', 'WHITE', 'ORANGE', 'RED', 'RED', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'WHITE']


#Merging all colors
All_Colors = Monday + Tuesday + WEDNESDAY +THURSDAY +FRIDAY
print(All_Colors)
print()

#Total number of colors in a week
total_colors = len(All_Colors)
print(total_colors)
print()
#Eliminating duplicates
colo_set = set(All_Colors)
print(colo_set)
print()

#number of unique colors
count = len(colo_set)
print(count)
print()




# mean_color = sum(All_Colors)/len(All_Colors)
# print(mean_color)

colors = []
#extracting each color
def num_each_col(color):
    colors.clear()
    for i in All_Colors:
        if i == color:
            colors.insert(0,i)
            
    print()
num_each_col('BLACK')

black_colors = colors.copy()
print(black_colors)

num_each_col('YELLOW')
yellow_colors = colors.copy()

num_each_col('CREAM')
cream_colors = colors.copy()

num_each_col('WHITE')
white_colors = colors.copy()

num_each_col('BLUE')
blue_colors = colors.copy()

num_each_col('PINK')
pink_colors = colors.copy()


num_each_col('GREEN')
green_colors = colors.copy()


num_each_col('ARSH')
arsh_colors = colors.copy()


num_each_col('RED')
red_colors = colors.copy()

num_each_col('ORANGE')
orange_colors = colors.copy()

num_each_col('BROWN')
brown_colors = colors.copy()

# colors and values

color_set = {'brown_colors':len(brown_colors), 'orange_colors': len(orange_colors),'red_colors':len(red_colors), 'arsh_colors':len(arsh_colors),'green_colors':len(green_colors), 'pink_colors':len(pink_colors), 'blue_colors':len(blue_colors), 'white_colors':len(white_colors), 'cream_colors': len(cream_colors), 'yellow_colors':len(yellow_colors), 'black_colors':len(black_colors) } 
print(color_set)

#importing required module
from statistics import *
import math

#Question 1: Which color of shirt is the mean color?

meanOfShirtColor = total_colors/count
print(meanOfShirtColor)

#Question 2: Which color is mostly worn throughout the week?

most_worn = 'BLUE'

#Question 3: Which color is the median?
All_Colors.sort()

median_color =median(All_Colors)    #'GREEN'


#Question 4: Get the variance of the colors
valuesList = [] #get values of color occurrence
for i in color_set.values():
    valuesList.insert(0,i)
    
variance_of_color = variance(valuesList) #75.05
#Question 5: if a color is chosen at random, what is the probability that the color is red?

pr_of_red = (9/sum(valuesList))*100 # 9.47%

#Question 6: Save the colors and their frequencies in postgresql database
#import modules
import psycopg2

#connecting to database
conn = psycopg2.connect(database = "testdb", user = "postgres", password = "pass123", host = "127.0.0.1", port = "5432")
print "Opened database successfully"

cur = conn.cursor()
#insteing values into assignment table
cur.execute("INSERT INTO assignment (ID, WHITE, PINK, BLUE, BROWN, ARSH, ORANGE, YELLOW, CREAM, RED, BLACK, GREEN) \
      VALUES (1, '16', '5','31','6','1','9','5','2','9','1','10')");


conn.commit()
print "Records created successfully";
conn.close()

#Question 7:   write a recursive searching algorithm to search for a number entered by user in a list of numbers

def recursive_search(num, my_list, start=0, end=None):
    # Set the end index to the length of the list if it is not provided
    if end is None:
        end = len(my_list)
    
    # Base case: if the start index is greater than or equal to the end index, the number was not found
    if start >= end:
        return False
    
    # Calculate the middle index
    mid = (start + end) // 2
    
    # Check if the middle element is equal to the target number
    if my_list[mid] == num:
        return True
    
    # If the target number is less than the middle element, search the left half of the list
    elif num < my_list[mid]:
        return recursive_search(num, my_list, start, mid)
    
    # If the target number is greater than the middle element, search the right half of the list
    else:
        return recursive_search(num, my_list, mid+1, end)

num = int(input("Enter a number to search for: "))
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
found = recursive_search(num, my_list)
if found:
    print("The number", num, "was found in the list.")
else:
    print("The number", num, "was not found in the list.")

# question 8. Write a program that generates random 4 digits number of 0s and 1s and convert the generated number to base 10.

import random

#Generate random numbers
bin_num = " "
for i in range(4):
    bin_num += str(random.randint(0, 1))

#Convert to binary string
dec_num = int(bin_num, 2)

# Convert the binary string to base 10
decimal_num = int(bin_num, 2)

# Print the result
print("Binary: ", bin_num)
print("Decimal: ", decimal_num)

#9.      Write a program to sum the first 50 fibonacci sequence.

# Function to generate the first n calc numbers
def calc(n):
    my_list = [0, 1]
    for i in range(2, n):
        my_list.append(my_list[i-1] + my_list[i-2])
    return my_list

# Calculate sum of first 50 Fibonacci numbers
my_sum = sum(calc(50))

# Print the result
print(my_sum)
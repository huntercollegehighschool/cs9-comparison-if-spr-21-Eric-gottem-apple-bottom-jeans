'''
______
PART 1
______
The code below prompts the user to enter two numbers, and then prints out the smaller of the numbers entered. Modify so that it prompts the user to enter THREE numbers, and then prints the smallest of the three numbers entered in a sentence.

(Hint: You'll need to be careful for the cases when the user enters the same number twice or all three times.)

An example of what should appear on the console when the code is run:

Enter a number: 11
Enter another number: 2
Enter another number: 5

The smallest number is 2
'''

"""
x = int(input("Enter a number: "))

smallest = x

y = int(input("Enter another number: "))

if y < x:
  smallest = x
  
print("The smallest number is ", smallest)

"""

a = int(input("enter number babeh: "))
b = int(input("enter another number hun:"))
c = int(input("enter a third number boo-boo:"))

if a < b and a < c :
  smallest = a
  print("The smallest number is", smallest,", honey muffin")
elif b < a and b < c :
 smallest = b
 print("The smallest number is", smallest,", sugar plum")
elif c < a and c < b :
 smallest = c
 print("The smallest number is", smallest,", sweet pea")

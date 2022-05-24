'''
______
PART 5
______

Write a program that asks the user to enter the name of a month as a string. The program will then print how many days that month could have in any given year, or print a statement saying that what the user entered is not the name of a month.

(Hint: This should require only four code blocks, but it can be done with 12 or more if you insist. If you are familiar with lists or other container datatypes, you may implement this using those, though it still requires four code blocks)

Four examples of what should appear on the console when the program runs (note: the test driver is case sensitive):

Enter a month:  March
31

Enter a month:  June
30

Enter a month:  February
28 or 29

Enter a month:  Saturday
not a month
'''

#start writing your code below

month = input("enter a month: ")

if month == "january" or month == "January":
 print("31")
  
elif month == "february" or month == "February":
 print("28 or 29")
  
elif month == "march" or month == "March":
 print("31")
  
elif month == "april" or month == "April":
 print("30")
  
elif month == "may" or month == "May":
 print("31")
  
elif month == "june" or month == "June":
 print("30")
  
elif month == "july" or month == "July":
 print("31")
  
elif month == "august" or month == "August":
 print("31")
  
elif month == "september" or month == "September":
 print("30")
  
elif month == "october" or month == "October":
 print("31")
  
elif month == "november" or month == "November":
 print("30")
  
elif month == "december" or month == "December":
 print("31")
  
else:
  print("that is not a month")
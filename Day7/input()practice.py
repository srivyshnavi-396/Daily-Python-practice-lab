#1. What is the input() function in Python used for? 
'''In Python, input() function is a built-in function used for taking the input from user.'''

#2. How can you accept an integer as input from the user using input()? 

#we can accept by using int(input)
'''score = int(input('Enter your exam score:'))
print("My exam score is:",score)'''

#3. How do you accept a float input from the user? 

'''gpa = float(input("Enter your gpa:"))
print(gpa)'''

'''#4. How can you take multiple space-separated values as input? 
str = input("Enter a sentence:").split()
print(str))'''

'''#5. How do you check if a number entered by the user is positive, negative, or zero? 
 
num = int(input('Enter a number:'))
if num<0:
    print('The number is negative')
elif num>0:
    print('The number is positive')
else:
    print('The number is zero')'''


#6. How do you convert user input to a list of integers? 

'''nums = int(input(' Enter list of numbers :'))
print((nums))....>it is not working so, we have to use list comprehension'''


'''The Definition
"List comprehension is a concise(giveing a lot of information in simple wors......>The Goal: Maximize meaning, minimize space.),
one-line syntax in Python 
used to create a new list by iterating over an existing sequence. 
It combines the functionality of a for loop and an optional
if statement into a single bracketed expression, making the code
more readable and efficient."


The "Three-Part" Breakdown
If the interviewer asks you to elaborate, you can break it down into these three core benefits:

Syntactic Sugar: It replaces multiple lines of for loops and .append() calls with a single, readable line.

Performance: It is generally faster than a standard loop because it is optimized at the C-level within Python.

Declarative Style: It allows you to focus on what you want in the list rather than the step-by-step process of how to build it.'''


'''Breaking Down the Syntax
You can read a list comprehension from left to right like a sentence. It generally follows this formula:

new_list = [expression for item in iterable if condition]

expression: What do you want to end up in the list? (e.g., the fruit itself).

for item in iterable: Where are you getting the data from? (e.g., the basket).

if condition (Optional): Does the item meet your criteria? (e.g., is it an "apple"?).

why we use this over loops

we use this because it is

shoter
faster
cleaner '''

'''nums = [int(x) for x in input('enter numbers:').split()]
print(nums)

# square nums

nums = input('Enter numbers :')
squares = [int(n)**2 for n in nums.split()]
print(squares)'''


'''#7. How do you accept a string input and print it in uppercase? 

str = input('Enter any String :')
print(str.upper())'''

#8. Write a Python program that accepts a string and prints 
# the number of vowels in it.

'''str = input('Enter a string :')
vowels = 'aeiou'
count = sum(1 for char in str if char in vowels)#you have doubt about 1 u can also use 
#letter instead but it not returns sum but 1 can eg:when it find a=1,e=1...1+1=2 it returns
print('Number of vowels',count)'''


'''str = input('Enter a string :')
vowels = 'aeiou'
count = sum(1 for letter in str if letter in vowels)#you can use any word not only char/letter
print('Number of vowels',count)'''

'''9. Write a program that takes a number as input and checks 
# if it is even or odd. 

num = int(input("Enter any num: "))
if num%2==0:
    print("even num = ",num)
else:
    print("odd num : ",num)'''
    
'''10. How would you check if a string is a palindrome using input()? 
     #A palindrome is a word that reads the same backward as forward (like "radar" or "madam")
     #palindrome means how ever we look the string it appears same
    # racecar,refer,level
    
str = input('Enter any string:')
if str == str[::-1]:
    print("str is palindrome")
else:
    print('str is not palindrome')'''
    
        
    
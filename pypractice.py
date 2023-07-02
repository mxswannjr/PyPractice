#!/bin/python
#Executable script that that encompasses skillset, compiled during coursework. The resulting output will be of the examples created. Please see comments below for additional guidance.

#String Practice
print("Hello World")
print('Hello World')

#Multi-line string uses triple quotation
print("""This string runs
on multiple lines""")

print("String 1 " + "and String 2") #String concatenation
print('\n') #New line creation
print('New Line Test')
print('\n')

#Math
print(50 + 50) #Addition
print (50 - 50) #Subtraction
print (50 * 50) #Multiplication
print(50 / 50) #Division
print(50 + 50 - 50 * 50 / 50) #PEMDAS
print (50 ** 2) #Exponents
print(50 % 6) #Modulo - takes what is left over, used to find the remainder.
print(50 / 6) #Division with remainder output
print(50 // 6) #Division without the remainder presented - whole number
print('\n')

#Variables and Methods
quote = 'All is fair in love and war' #storing this string as the variable 'quote'
print(quote)
#Methods are functions that are available for a given ovject. Built into python to allow us to do something.
print(quote.upper()) #Upper-case method
print(quote.lower()) #Lower-case method
print(quote.title()) #Title-case -- meant to capitalize every first letter
print(len(quote)) #Character count
print('\n')

name = 'Mario' #string
age = 28 #integer
height = 73.5 #float - a number with a decimal

print(int(age))
print(int(30.1))
print(int(30.9)) #Integers do not round. Output is 30, not 31

print('My name is ' + name + ' and I am ' + str(age) + ' years old.') #A styntax error was presented when using double quotations when building this string, variable object. Be sure to check syntax.
print('\n')

age += 1
print(age) #Redefined the variable, by adding one in this example.

birthday = 1
age += birthday #Created a variable that serves as birthday.
print(age) #Variable redefined once again.
print('\n')
 
 
#Functions
#Functions are an organized blocks of code, commonly interpreted as mini programs.

def who_am_i(): #This is a function without parameters.
	name = 'Mario' #local variable
	age = 28 #local variable, even though (age) was defined before, outside of this function
	print('My name is ' + name + ' and I am ' + str(age) + ' years old.')

who_am_i() #Calling the function should only result in the output of what is locally stored in the function. Hence local function.
print(age) #This is not within the local function, therefore should produce output that defined outside of the function.
print('\n')

def add_one_hundred(num):
	print(num + 100)
add_one_hundred(100)

def add(x,y):
	print(x + y)
add(7,7)

def multiply(x,y):
	return x * y #Return is different that print. Return stores the values within the function, to be called and used later within the function. There is no correct user output when using return.
multiply(7,7)
print(multiply(7,7)) #Used to actually produce proper input for the user.

def square_root(x):
	print(x ** .5)
square_root(64) #Returns a float

def nl(): #New line function, created instead of having to type out print everytime.
	print('\n')
nl()
print('New line function test')
nl()

#Boolean Expressions (True or False / On or Off)
bool1 = True
bool2 = 3*3 == 9 #True Statement
bool3 = False 
bool4 = 3*3 != 9 #False Statement
print(bool1,bool2,bool3,bool4)
print(type(bool1))
nl()
bool5 = "True" #This is a string, not a boolean expression
print(type(bool5))
nl()

#Relational and Boolean Operators
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7

test_and = (7 > 5) and (5 < 7) #True Statement
test_and2 = (7 > 5) and (5 > 7) #False Statement becasue both are not true
test_or = (7 > 5) or (5 > 7) #Still a true statement becasue one is true, both are not false
test_not = not True #False
test_not2 = not False #True
#THESE WILL NOT SHOW IN SCRIPT BECASUSE THEY WERE NOT CALLED - BOOLEAN PRACTICE.

#Conditional Statements - (if/then/else statements)
def drink(money):
	if money >= 2:
		return "You've got enough for the drink"
	else:
		return "You do not have enough for the drink"
print(drink(4))
print(drink(1))
nl()

def bar_tab(age,money): #Multiple variables. Here it is (x,y). 
	if (age >= 21) and (money >= 5):
		return "Let's drink"
	elif (age >= 21) and (money < 5):
		return "Need more cash"
	elif (age < 21) and (money >= 5):
		return "I'm sorry, you're just not old enough"
	else: #Statement for if all fails.
		return "Come on lil bro"
print(bar_tab(32,6))
print(bar_tab(23,4))
print(bar_tab(19,7))
print(bar_tab(17,2))
nl()

#Lists - Lists use brackets []. They are data structures, ordered elements. These are change-able, tuples are not.
movies = ['Avatar','Hangover','iRobot']
print(movies[0]) #first item
print(movies[1]) #second item
#Indexes start at zero, not one.
print(movies[1:2]) #returns the second item, and cuts off at the beginning of the second called item.
print(movies[1:])#Prints the first called and the rest of what is called.
print(movies[:1]) #Prints up until the second.
print(movies[-1]) #Prints the last item in the list
print(len(movies)) #Length of the list
movies.append('Jaws') #Append method adds to the end of the list.
print(movies)
movies.insert(2,'Hustle & Flow') #Inserts item into second position on the list
print(movies)
movies.pop() #removes the last item on the list
print(movies)
movies.pop(2) #removies a specific item
print(movies)

girl_movies = ['Barbie', 'Powerpuff Girls','Dora the Explorer']
our_favorite_movies = movies + girl_movies
print(our_favorite_movies)
nl()
#Two Dimensional lists. Notice how to index.
grades = [['Bob', 82],['Alice',98],['Jeff',73]]
bobs_grade = grades[0][1] #Identifies the second item with in the first item.
print(bobs_grade) #result should be 82 (Bobs grade in the list)
grades[0][1] = 65 #this should modify Bobs grade to 65 - LISTS ARE CHANGEABLE!!!
print(grades)
nl()

#Tuples - Lists that cannot be changed. They use parentheses (). Not brackets []. Immutable.
new_grades = ('A', 'B', 'C', 'D', 'F')
print(new_grades[1]) #Result should be 'B'. Methods such as pop and append will not work.
nl()

#Looping

#For Loops - start to finish of an iterate
vegetables = ['Avocado', 'Kale', 'Spinach']
for veg in vegetables:
	print(veg)
#For Loops are great to run through a sequence of events. Imagine an ip sweeper that checks for contingency of a range of ip addresses. This can be created using a for loop.
nl()


#While Loops - execute a certain function while parameters are True.
i = 1 #starting variable defined
while i < 10:
	print(i)
	i += 1 #if still within parameter then add one, and check again - until out of parameter.
nl()

#Advanced Strings - strings are immutable. They can be redefined if called to do so, but they are immutable until done so.
my_name = 'Mario'
print(my_name[0]) #first letter of name
print(my_name[-1]) #last letter of name
nl()
sentence = 'This is a sentence.'
print(sentence[:4])
print(sentence.split()) #Delimiter - default delimiter in python is ' '. Cuts item on this defined limitation.
sentence_split = sentence.split() #Creation of sentence broken down on delimiter
sentence_join = ' '.join(sentence_split) #Conjoining of each delimited item
print(sentence_join) #Reconstructed sentence
nl()

quote = "'Wow that is a big boulder,' he said"
print(quote)
quote = "He said \"wow that is a big boulder\"." #Character escaping uses the back slash- similar to the new line. It ignores the following character.
nl()

too_much_space = '                          hello            '
print(too_much_space.strip()) #.strip eliminates the extra space.

print('A' in 'Apple') #Boolean Statement - True
print('a' in 'Apple') #Boolean Statement - False because case sensitivity matters
letter = 'a'
word = 'Apple'
print(letter.lower() in word.lower()) #improved check of matching

movie = "Avatar"
print('My favorite movie is {}'.format(movie)) # .format method old school method
print('My favorite movie is %s' % movie) #%s method - NEW 
print(f'My favorite movie is {movie}') #String literal - f string LATEST AND GREATEST.
nl()

#Dictionaries - Key Value Pairs, that use {} 
drinks = {"Pineapple":6, "Cranberry":5, "Pear":3, "Apple":8}
#In this example, the fruit is the key, and the price is the value
print(drinks)
nl()
employees = {"Finance":["Bob", "Linda" , "John"], "IT": ["Cam", "Mario", "Tobias"], "Marketing": ["Karen","Gia"]}
print(employees)

employees["Legal"] = ["Papa Ray"] #Adds new key:value pair
print(employees)
employees.update({"Sales":["Jovan","Natalie"]}) #also adds another key:value pair
print(employees)
nl()
drinks["Pineapple"] = 9 #Updates value of the called key
print(drinks)
print(drinks.get("Pineapple"))
nl()
print('Please see code for proper direction of output - Thank you!')
#END OF SCRIPT


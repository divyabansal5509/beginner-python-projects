# Python Basics — AI Learning Journey

## Day 1 — Core Concepts

### Variables
name = input("Enter your name:")
- f before quote = tells Python to scan for variables inside {}
print(f"Hello, {name}!")

exercise 1: a patient in hospital, define 3 variables for name,age and if he already exist in record
 name = John Smith
 age= 24
 already_exist = True

 exercise 2: ask person's name and favourite color and print like "Divya likes brown"

 person_name = input("Enter your name: ")
 fav_color = input("Enter your favourite color: ")
 print(f"{person_name} likes {fav_color})

### Type Conversion

birth_year = input("Enter birth year: ")
print(type(birth_year))      //str
age = 2026- int(birth_year)
print(type(age))             //int
print(age)

 exercise 3:Ask a user their weight (in pounds), convert it to kilograms and print on the terminal.

 weight_in_pounds = input("Enter your weight:")
 weight_kg =int(weight_in_pounds) * 0.45
 print( weight_kg)


### f-strings
- {} = replace this with the actual variable value

### Data Types
## Mistakes I Fixed Today
- str  → text → "Divya"
- int  → whole number → 21
- float → decimal → 3.14
- bool → True/False

- int(input()) is for numbers only, NOT names
- print() needs f-string or commas to combine variables

### Strings - single quote or double quote

''' multi line string ''' - using triple quote

""Index:""
text= "python for beginners"
another=text[:]
print(text[0])     //p
print(text[-1])    //s
print(text[1:5])   //ytho
print(text[0:])    //python for beginners
print(another)     //python for beginners

### Formatted String:
first = "Divya"
last = Bansal"
message = first + "[" + last +"] is a coder"
mssg =f"{first}[{last} is a coder]"   //formatted string
print(message)

### String Methods
course= "python for beginners"
print(len(course))    //length of string
print(course.upper()) //methods belong to some particular thing like here for string and len is general function
print(course.find('o')) //print index
print(course.replace('o',why'))   // replace o with why
print("python" in course)  //Write boolean value


## Airthmetic Operators

x=10
x+=3
x-=2
print(x)

### Operator Precedence

x=(20+3)*2 **2

Parenthesis->Exponentiation->multi or divi->add or sub

## Math Functions

x=2.9
print(round(x))  //3
print(abs(-2.9)) //2.9

import math
print(math.ceil(2.9)) //3
print(math.floor(2.9)) //2

## IF Statements

is_hot = False
is_cold = True
if is_hot:
    print("It 's a hot day")
    print("Drink plenty of water)
elif is_cold:
    print("It's a cold day)
    print("Wear warm clothes)
else:
    print("It's a lovely day)
print("Enjoy your day")


Exercise : Price of a house is $1M.
If buyer has good credit,- they need to put down 10%
Otherwise - they need to put down 20%
WAP with these rules an display the down payment required for a buyer with good credit.

price = 1000000
has_good_credit = True
if has_good_credit:
     down_payment = 0.1*price
else:
     down_payment = 0.2*price
print(f"Down payment: ${down_payment}")

### Logical Operators  - and(both true),or(at least one true),not

has_high_income = True
has_good_credit = True
if has_high_income and has_good_credit:
     print("Eligible for loan")

### Comparison Operators -  <,>,==,>=,<=,!=

temp = 30
if temp > 30:
   print("hot day")
else:
   print("not a hot day")

Exercise:
if name is less than = name must be at least 3 characters
otherwise if it's more than 50 characters
name can be a maximum of 50 characters
otherwise - name looks good!

name = input("Enter your name:")
leng = len(name)
if leng < 3:
   print("Name must be at least 3 characters")
elif leng > 50:
   print("Name can be a maximum of 50 characters")
else:
   print("Name looks good!")
     

#### Weight Convertor
Exercise:
if user gives weight in pound or kg ,change it into other unit.

weight = int(input("Enter your weight:"))
unit =input("L for pounds or K for kilogram:" )
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"Your weight is {converted} kilos")
else:
    converted = weight / 0.45
    print(f"Your weight is {converted} pounds")

## While Loops

i=1
while i <=5:
   print('*' * i)
   i+=1
print("Done")

**Building a guessing game:**

secret_num = 9
guess_count = 0
guess_limit = 3
while guess_count <= guess_limit :
    guess = int(input("Guess:"))
    guess_count +=1
    if guess = secret_num:
        print("You Won!")
        break
else:
    print("Sorry,You Failed!")

**Car Game:**

command = ""
started = False
while True:
    command = input("Enter command:").lower()
    if command = "start" :
        if started:
           print("Car is already started!") 
         else:
            started = True
            print("Car started...Ready to go !")
   elif command = "stop" :
        if not started:
            print("Car is already stopped!")
        else:
            print("Car stopped.")
   elif command = "help":
        print("""
start - to start a car
stop - to stop a car
quit - to quit
    """)
   elif command == "quit":
        break   
   else:
        print("Sorry,I don't understand that")

## For Loops:

for item in range(5, 10, 2):
   print(item)

prices = [10,20,30]
total = 0
for price in prices:
    total += price
print(f"Total: {total}")

### Nested Loops: (for each x value having some y value)

for x in range(4):
   for y in range(3):
      print(f"({x},{y} )")

Exercise:

numbers = [5,2,5,2,2]
for x_count in numbers:
   output = ''
   for count in range(x_count):
      output += 'x'
    print("output")

## LIST












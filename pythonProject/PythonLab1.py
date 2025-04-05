#Python lab 1
#Learn from the online interactive tutorial and finish below tasks
#You can edit in this file by filling blanks after each question.
#Submit the .py file for your own reference
#This practice is graded only on submission.
#It will help you to get started on Python for the homework
#####
#Example function
#####
def example():
    print("I am the example code")
#Now, go to the end of this file, and you will find the main function & how to run your code there
#Around line #94
#####
#1. function in python
####
def printhello():
    print("Hello") #Remove the # at the beginning of this line.
#tab is IMPORTANT in python. tab in python replaces {} in C++
#print string hello world. One line of code here. Make sure it is indented to show it belongs to this function
#####
#2. variable definition in python
#####
def somevars():
    one = 1
    two = 2.0
    three = 3.4
    four = one + two + three
    print(four)

#define a few integer and float numbers, add them together and print result out
#call the function to run it in the main function at the end of the filfe
#####
#3. define a list in python
#####
def mylist():
    mylist = [1, 2, 3, 4, 5]

    print(mylist)

    empty_list.append(10)
    empty_list.append(20)
    empty_list.append(30)
    print(empty_list)

    for x in mylist:
        print(x)
#define a list with 5 numbers, print it out
#define an empty list and append a few numbers into it, then print it out
#call your mylist func to execute in the main function at the end of the file
#####
#4. string output
#####
def printstr(input_str1, input_int1):
    long_str = input_str1 + str(input_int1)
    print(long_str)

#convert int into string and append the int with the string to form a long string
#(technical googling practice -- google what func to use)
#print the long str out
#In the main function, define an input string and an input int.
#Pass them in as parameters to the function. Call and run the function to see results.
####
#5. passing var to func and return
####
def funcvars(inputvar1, inputvar2):
    result = inputvar1 + inputvar2
    return result
#add the input numbers together
#return the result
#Define the input variables in main, pass them into the function.
#In main, use a result variable to receive the result from funcvars and print the result out
####
#6. for loop
####
def go_over_list(mylist):
    for item in mylist:
        print(item)
#use for loop to go over the input list and print out items one by one
def go_over_list1():
    for number in range(10,18):
        print(number)
#use for loop to directly print out numbers from 10 to 17
def go_over_list2(mylist):
    for item in mylist:
        print(item * 2)

#use for loop & go over your list
#multiply 2 to every item in your list, print results out
def go_over_list3(mylist):
    resLis = []
    for item in mylist:
        resLis.append(item * 2)
        return resLis
#create an empty list resLis
#go over items in the input list, multiply 2 to every item
#add result one by one to resLis
#return resLis
#Call all the functions in main. Provide necessary inputs to the functions.
#For those with return values, print the return values out in main.
####
#7. while loop
####
#do all the problems in 6 using while loop instead
def go_over_list_while(mylist):
    index = 0
    while index < len(mylist):
        print(mylist[index])
        index += 1

def go_over_list1_while():
    number = 10
    while number <= 17:
        print(number)
        number += 1

def go_over_list2_while(mylist):
    index = 0
    while index < len(mylist):
        print(mylist[index] * 2)
        index += 1

def go_over_list3_while(mylist):
    resLis = []

    index = 0
    while index < len(mylist):
        resLis.append(mylist[index] * 2)
        index += 1
    return resLis

#####
#Here is the main function
#You can have only 1 main function in 1 script
#Left-click on the green arrow next to the line number of the line of the main function definition
#Your code would run.
if __name__ == '__main__': #a quick way to type this line is: type "main" and then tab
    print("****Example****")
    example()

    print("****Question 1****")
    printhello()

    print("****Question 2****")
    somevars()

    print("****Question 3****")
    mylist()

    print("****Question 4****")
    printstr("Number" , 123)

    print("****Question 5****")
    result = 5,10
    print(result)

    print("****Question 6****")
    go_over_list([1, 2, 3, 4, 5])
    go_over_list1()
    go_over_list2([1, 2, 3, 4, 5])
    result_list = go_over_list3([1, 2, 3, 4, 5])
    print(result_list)

    print("****Question 7****")
    go_over_list_while([1, 2, 3, 4, 5])
    go_over_list1_while()
    go_over_list2_while([1, 2, 3, 4, 5])
    result_list_while = go_over_list3_while([1, 2, 3, 4, 5])
    print(result_list_while)


#you can start call and run your functions here
######

#Python is an easier PL to learn than C++ and looks like C++
#From this lab experience, reflect and summary what it feels like
#when you are learning a new PL that is similar to a PL that you already know?
#Your answer here: For me, its reassuring knowing that there are some similarities because it does take me longer to learn.

#In this case, when you want to learn a new PL that looks like a PL that you already know,
#how can you learn the new PL quickly? Any steps?
#Your answer here:I feel like the first thing to do is look for the similarities within both PLs.

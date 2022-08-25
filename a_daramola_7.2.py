#Akinola Daramola Jr
#Programming Exercise 7.2
#Due Date: 07/31/2022

"""
Lottery Number Generator
Design a program that generates a seven-digit lottery number.
The program should generate seven random numbers, each in the range of 0 through 9, and assign each number to a list element.
(Random numbers were discussed in Chapter 5.)
Then write another loop that displays the contents of the list.
"""

#Import random module
import random


#Define main() function to call numberGenerator() function
def main():
    #Invoking numbeGenerator() function to produce random number
    numberGenerator()


#Define numberGenerator() function
def numberGenerator():
    #Declaring lottery_ticket variable as list
    lottery_ticket = []
    #Initializing ticket_number variable to zero
    ticket_number = 0

    #Looping through range between 0 and 9
    for numbers in range(0,7):
        #Declaring new random_number upon each iteration
        random_number = random.randint(1,9)
        #Appending random number to list
        lottery_ticket.append(random_number)
    #Displaying list generated
    print("List:", lottery_ticket)
    #Looping through content of list
    for content in lottery_ticket:
        print(content, end = ", ")
        #Displaying content of list generated
        #print(f"E{ticket_number}:", content)
        

#Calling mainline function to run program
main()

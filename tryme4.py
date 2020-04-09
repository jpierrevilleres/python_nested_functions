# Jean-Pierre de Villeres Programming Assigment Unit 2 Submission
# This python file tryme4.py was run on Python version 3.8.0

# defines the function new_line which prints a single '.' per line. 
def new_line():

    print('.')

# defines the function three_lines which calls the nested function new_line three times to print one line
def three_lines():

    new_line()

    new_line()

    new_line()

#defines the function nine_lines which calls the nested function three_lines three times to print nine lines
def nine_lines():

    three_lines()

    three_lines()

    three_lines()

#defines the function clear_screen which calls the nested function nine_lines two times, three_lines two times and new_line 1 time to print twenty lines
def clear_screen():

    nine_lines()

    nine_lines()

    three_lines()

    three_lines()

    new_line()

print("Printing nine lines using nine_lines()") #printed message that nine lines will be printed out.
nine_lines() #executes the nine_lines() function to print out nine lines.
print("Printing twenty five lines using clear_screen()") ##printed message that twenty five lines will be printed out.
clear_screen() ##executes the clear_screen() function to print out nine lines.














#!/usr/bin/python3

# INET4031
# Logan Johnson
# 03/22/2026
# 03/22/2026

#REPLACE THIS COMMENT - identify what each of these imports is for.
import os
import re
import sys

def main():
    #Takes the second argument of the command and sets that as the file to read from, dont have to use < as it messes with user inputs
    filename = sys.argv[1]
    #Takes a user input and stores it in a variable for later when determining what to do with execution
    user_input = input("Would you like to run the code in dry mode? Prompt Y to run dry-mode or N to run code normally: ")
    #Opens the file in read mode and reads line by line
    with open(filename, 'r') as file:
        for line in file:

            #Match variable that looks for the presence of a # or ^, (NONE or Match) used later 
            match = re.match("^#",line)

            #Creates an array that sperates the line by : in the input file, each field should be an element
            fields = line.strip().split(':')

            #Checks if one of the characters was present or if there are nnot the correct amoount of fields in the input file and skips the line
            if match or len(fields) != 5:
                continue

            #Create variables for each field used in the creation of a user in the system, username takes the first field that was seperated in the fields array, password is the second field, full name combines the 3rd and 4th field
            username = fields[0]
            password = fields[1]
            gecos = "%s %s,,," % (fields[3],fields[2])

            #Creates a group variable based on the last field in the input file and field array, can be mutiple hence why we split it to create another array containing all groups the user is apart of
            groups = fields[4].split(',')

            #Lets us know who the account is for
            print("==> Creating account for %s..." % (username))
            #Creates a variable cmd that houses the actual command waiting to be ran in the system inputted with the correct information from the input file
            cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

            #This is what actually runs the command on the operating system, can leave commented out for dry runs and test, if no will execute the command and could be a messy cleanup if an error in the input file is present
            #If statement based on user input from earlier, if its ran normally execute the command to add a user if not print out what the command would be
            if user_input == "N":
                os.system(cmd)
            else:
                print(cmd)
            #Lets us know we are now setting the password for the given user
            print("==> Setting the password for %s..." % (username))
            #Edits the cmd variable with a new command that sets the password for a given user using root privileges
            cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

            #Executes the set password command, leave commented out for dry runs and when testing, any errors in the input file will be executed
            #If statement based on user input from earlier, if its ran normally execute the command to add a user if not print out what the command would be
            if user_input == "N":
                os.system(cmd)
            else:
                print(cmd)
            for group in groups:
                #Loops through the group array created could have mutiple groups might have just one, if a group is specified that is not "-" will assign the user to that group and execute the command if "-" is detected do nothing.>
                if group != '-':
                    print("==> Assigning %s to the %s group..." % (username,group))
                    cmd = "/usr/sbin/adduser %s %s" % (username,group)
                    #If statement based on user input from earlier, if its ran normally execute the command to add a user if not print out what the command would be
                    if user_input == "N":
                        os.system(cmd)
                    else:
                        print(cmd)

if __name__ == '__main__':
    main()

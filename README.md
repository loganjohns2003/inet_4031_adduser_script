# INET4031 Add Users Script and User List

## Program Description

This program is designed to automate the tedious task of adding users to a system one by one. Instead it takes in an input file of all users needing to be added with each line being its own user. It reads it line by line and parses the information within the file to create an array of inputs that are the fields for what is used in the actual command. It then runs the respective commands, using those parsed fields from the file, for adding a user, setting their password, and finally adding them to their groups. It is created to help speed up this task that would be tedious for administrators especially when dealing with thousands of users.

## Program User Operation

The program is quite simple to run, all you need is the python file storing all the code, and an input file that contains all users needing to be added to a system. Once those 2 conditions are met, within the terminal run the following command ./create-user.py < my-user-list.input. Obviously, replace my-user-list.input with whatever input file you desire. Once entered the terminal should begin adding users to the system based on whatever is in the file.

### Input File Format

The input file needs to be .input, and the contents within the file need to follow a specific format for the script to properly run and add users.
  1. Each line needs to contain all 5 fields for a user, Username, Password, Last Name, First Name, any Groups they belong to
  2. Each line needs to seperate these fields using a :
  3. If there are multiple groups seperate them by a ,
  4. Ex. user04:pass04:Last04:First04:group01
  5. Ex. user04:pass04:Last04:First04:group01,group2
Additionally, if you want to not include specific users for a system, adding a # or ^ as the first character of the line will have the script ignore it
  1. Ex. #user04:pass04:Last04:First04:group01 or ^user04:pass04:Last04:First04:group01
If a user does not specifically belong to any groups, instead of leaving the field blank (script will ignore it because < 5 fields), use a - instead
  1. Ex. user04:pass04:Last04:First04:-

### Command Excuction
To execute the code simple run,
  ./create-user.py < my-users.input, replacing my-users.input with whatever your file name is
Sometimes, you may get an error not allowing you to execute the file. In this case change the permissions of the file using sudo chmod 744 create-user.py

### "Dry Run"
If you want to dry run the code to see what it does and not have it actually create users, open the python file with your editor of choice and comment out the lines including os.system(cmd). This will not execute the commands used to create users.

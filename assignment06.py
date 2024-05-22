# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Leena Chaudhuri,21/05/2024,Created Script
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"
# Define the Data Variables and constants

student_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict[str]= {}# one row of student data
students:list[dict[str]]=[] # a table of student data
csv_data: str = ''  # Holds combined string data separated by a comma.
json_data: str = ''  # Holds combined string data in a json format.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.

class FileProcessor:
# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
    @staticmethod
    def read_data_from_file(FILE_NAME: str, student_data: list):
        try:
            with open(FILE_NAME, "r") as file:
                student_data = json.load(file)
            students.append(student_data)
        except FileNotFoundError as error_message:
            IO.output_error_messages("FILE DOESNT EXIST", error_message)
        except Exception as error_message:
            IO.output_error_messages("Some error happened in reading the file", error_message)
        finally:
            if file.closed == False:
                file.close()
        return student_data


    @staticmethod
    def write_data_to_file(FILE_NAME: str, student_data: list):
        try:
            with open(FILE_NAME, "w") as file:
                json.dump(student_data,file)
        except FileNotFoundError as error_message:
                IO.output_error_messages("FILE DOESNT EXIST", error_message)
        except Exception as error_message:
            IO.output_error_messages("Some error happened while writting", error_message)
        finally:
            if file.closed == False:
                    file.close()
       
class IO:
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        print(message, end="\n\n")
        if error is not None:
             print("--Exception Details--")
             print(error,error.__doc__,type(error),sep="\n")

    @staticmethod
    def output_menu(MENU: str):
        print(MENU, end ='\n')

    @staticmethod
    def input_menu_choice():
        menu_choice = "0"
        try:
            menu_choice = input("What would you like to do? ")
            if menu_choice not in ("1","2","3","4"):
                raise Exception( " Please only choose: 1,2,3 or 4")
        except Exception as error_message:
            IO.output_error_messages(error_message.__str__())
        return menu_choice

    @staticmethod
    def output_student_courses(student_data: list):
        print("-"*50)
        for student in student_data:
            print(f"{student["FirstName"]},{student["LastName"]} is enrolled in {student["CourseName"]}")
        print("-"*50)
    
    @staticmethod
    def input_student_data(student_data: list):
        try:
            while True:
                try:
                    student_name= input("Enter first name: ")
                    if not student_name.isalpha():
                        raise ValueError()              
                    break
                except ValueError :
                    print("Value Error, please re enter name using alphabets only")
            while True:
                try:
                    student_last_name= input("Enter last name: ")
                    if not student_last_name.isalpha():
                        raise ValueError()
                    break
                except ValueError :
                    print("Value Error, please re enter name using alphabets only")    
            

            course_name = input("Please enter the name of the course: ")
            '''''
            student_data =  {
                "student_name":student_name,
                "student_last name": student_last_name,
                "course_name": course_name,
            }
            '''
            student_data.append({"FirstName":student_name, "LastName":student_last_name, "CourseName":course_name})
            #print(f"You have registered {student_name} {student_last_name} for {course_name}.")
        
        except Exception as error_message:
            IO.output_error_messages("SOME ERROR HAPPENED",error_message)
        return student_data
    
if __name__=="__main__":
    students = FileProcessor.read_data_from_file(FILE_NAME=FILE_NAME, student_data=students)

    # Present and Process the data
    while True:
        # Present the menu of choices
        IO.output_menu(MENU)
        menu_choice = IO.input_menu_choice()

        # Input user data
        if menu_choice == "1":
            students= IO.input_student_data(student_data=students)
            print("Current data is")
            IO.output_student_courses(student_data=students)
            continue

        # Present the current data
        if menu_choice == "2":
            IO.output_student_courses(student_data=students)
            continue

        # Save the data to a file
        if menu_choice == "3":
            FileProcessor.write_data_to_file(FILE_NAME=FILE_NAME, student_data=students)
            continue

        # Stop the loop
        if menu_choice == "4":
            break

print("Program Ended")

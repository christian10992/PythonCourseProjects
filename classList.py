# This program records the names of 8 students in a list, sorts them alphabetically,
# reverses that order, appends my name and the instructor name onto the list,
# writes it to a file, then reads the file back, then stores the list as a tuple

# instructor and student names
INSTRUCTOR = "Professor Polanco"
MYNAME = "Christian Harris"

def main():
    # create empty list for student names
    students = []
    # get student names
    students = getNames(students)
    # print names entered
    print("You entered: ")
    displayList(students)

    
    # print names in alphabetical order 
    students.sort()
    print("Students in alphabetical order: ")
    displayList(students)
    # print names in reverse alphabetical
    students.reverse()
    print("Students in reverse alphabetical order: ")
    displayList(students)

    
    # append instructor name to end of list
    students.append(INSTRUCTOR)
    # insert my name at beginning of list
    students.insert(0, MYNAME)


    # open a file for writing and write names to it, then close it
    writeFile(students)
    # open a file for reading, print contents, then close it
    displayFile()

    # convert list to tuple and print
    studentsTuple = tuple(students)
    print("Names stored as a tuple: ")
    displayList(studentsTuple)

def getNames(students):
    # get input for 8 names
    for count in range (1, 9):
        name = str(input("Enter name for student #" + \
                         str(count) + ": "))
        # append names to list
        students.append(name)
    print("\n")
    # return list back to main function
    return students

def displayList(students):
    # iterate over list and print each name
    for x in students:
        print(x)
    print("\n")

def writeFile(students):
    namesList = open("names.txt", "w")
    for x in students:
        namesList.write(x + "\n")
    namesList.close()

def displayFile():
    print("Names on file: ")
    namesList = open("names.txt", "r")
    for x in namesList:
        x = x.strip("\n")
        print(x)
    print("\n")
    namesList.close()
    
main()

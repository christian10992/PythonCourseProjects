## This program will write to a file the name and test grade of 6 students
## It will the close the file, reopen it, and print what was written to the
## file previously

def main():
    # open file for writing
    studentGrades = open('grades.txt', 'w')
    name = str
    grade = -1.0
    # write student names and grades to file
    for name in range(0,6):
        name = getStudentName()
        while grade < 0 or 100 < grade:
            grade = getStudentGrade()
            if grade < 0 or 100 < grade:
                print('Grade must be between 0-100')
            
        gradeReturn = str(format(grade, '.2f'))
        grade = -1

        studentGrades.write('Name: ' + name + '\n')
        studentGrades.write('Grade ' + gradeReturn + '\n\n')

    studentGrades.close()
    print('')
    # file is closed and then reopened for reading
    try:
        studentGrades = open('grades.txt', 'r')
        # read each line of file
        for x in studentGrades:
            line = x
            line = line.rstrip('\n')
            print(line)
    except:
        print('File not found')
    studentGrades.close()
    
def getStudentName():
    name = str(input('Enter student name: '))
    return name

def getStudentGrade():
    try:
        grade = float(input('Enter student grade: '))
    except:
        grade = -1
        print('Grade must be a float.')
    return grade

main()

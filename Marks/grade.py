#initialising constants of the upper grade boundries
GRADE_U_UB=9
GRADE_1_UB=19
GRADE_2_UB=29
GRADE_3_UB=39
GRADE_4_UB=49
GRADE_5_UB=59
GRADE_6_UB=69
GRADE_7_UB=79
GRADE_8_UB=89

#repeatively asking for the number of students until a valid number between 1 and 20 is entered
def validate_students():
    while True: 
        students= int( input("Number of students? (0-20)") )
        if 1 <= students <= 20 :
            return students

#repeatively asking for the amount of marks until a valid number between 0 and 100 is entered
def validate_marks():
    while True:
        marks= int( input("Number of marks? (0-100)") )
        if 0 <= marks <= 100 :
            return marks

#converting the mark to the corresponding grade
def get_grade(marks):
    if marks <= GRADE_U_UB : 
        return "grade u"
    elif marks <= GRADE_1_UB :
        return 1
    elif marks <= GRADE_2_UB :
        return 2
    elif marks <= GRADE_3_UB :
        return 3
    elif marks <= GRADE_4_UB :
        return 4
    elif marks <= GRADE_5_UB :
        return 5
    elif marks <= GRADE_6_UB :
        return 6
    elif marks <= GRADE_7_UB :
        return 7
    elif marks <= GRADE_8_UB :
        return 8
    else:
        return 9

def main():
    grade9s=0
    names=[]
    students = validate_students()
    for i in range(0,students):
        marks = validate_marks()
        grade = get_grade(marks)
        #counts number of grade 9s and adds the grade 9 student name to a list
        if grade==9:
            grade9s=+1
            name=input("student name?")
            names=names.append(name)
        print("Grade:" , grade)

main()


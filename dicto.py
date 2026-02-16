print("Welcome to Grade Calculator!")

student_grades = {}

off = False
while not off:
    name = input("Enter student name: ")
    grade = input("Enter student grade: ")
    student_grades[name] = grade
    print(student_grades)

    add_another = input("Would you like to add new student ? Y or N: ").lower()
    if add_another == "y":
        pass
    else:
        off = True






    # marks = int(input("Enter your marks here: "))
    # if marks >= 80 and marks <= 100:
    #     print(name, "You have scored A")
    # elif marks > 64:
    #     print(name, "You have scored B")
    # elif marks > 44:
    #     print(name, "You have scored C")
    # elif marks > 30:
    #     print(name, "You have scored D")
    # elif marks > 0:
    #     print(name, "You have failed!")
    # else:
    #     print("Enter valid Scores!")
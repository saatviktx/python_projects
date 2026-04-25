#FUNCTION 1: add_student()
# Get name, clean it
# Get grades for each subject, and store in list
# Store in dict, with subjects as a set
avg = 0
subjects = ["English", "Math", "Science", "History / Social studies", "Advisory", "Elective 1", "Elective 2", "Elective 3"]
students = {}

def add_student(name):
    stdntProf = {}
    grades = []
    name = str(name).strip().title()

    for i in subjects:
        while True:
            try:
                grade = int(input(f"Enter grade for {i} (0-100): "))
                break
            except ValueError as e:
                print('Invalid input. Please enter integers only.')
        grades.append(grade)
        stdntProf[i] = grade
    students[name] = stdntProf

#FUNCTION 2: calc_avg(grades)
# - Takes list of grades
# - returns avg
def calc_avg(grades):
    sum = 0
    for i in grades.values():
        sum += i
    avg = sum/len(grades)
    return avg

#FUNCTION 3: get_letter_grade(avg)
# - takes avg
# - returns A, B, C, D, or F
def get_letter_grade(avg):
        if avg >= 90:
            return "A"
        elif avg >= 80 and avg <= 89:
            return "B"
        elif avg >= 70 and avg <= 79:
            return "C"
        elif avg >= 60 and avg <= 69:
            return "D"
        else:
            return "F"

#FUNCTION 4: find_performers(students)
# - Take full student dict
# - Returns highest and lowest performer
def find_performers(students):
    highest_avg = 0
    highest_name = ''
    lowest_avg = 100
    lowest_name = ''
    for name, grades in students.items():
        avg = calc_avg(grades)
        if avg > highest_avg:
            highest_avg = avg
            highest_name = name
        if avg < lowest_avg:
            lowest_avg = avg
            lowest_name = name
    print(f'Highest performer: {highest_avg}, {highest_name}')
    print(f'Lowest performer: {lowest_avg}, {lowest_name}')


#FUNCTION 5: print_report(students)
# - Loops thru dict
#- Prints clean summary for each student
def print_report(students):
    for name, grades in students.items():
        print(f"""
Student Name: {name}
{'-'*30}""")
        for i, grade in grades.items():
            print(f"""{i}: {grade}""")
        avg = calc_avg(grades)
        print(f"""{'-'*30}\nAverage: {avg}\n{'-'*30}\nLetter Grade: {get_letter_grade(avg)}
""")

#FUNCTION G: menu()
#While loop, runs until user quits
# - Options: add student, view report find performers, quit
# Error handling - no crashes
def menu():
    while True:
        opt = input('What would you like to do: add student (A), view report (V), find performers (F), quit (Q)? ').upper()
        if opt == 'A':
            inpName = (input('Enter name: '))
            add_student(inpName)
        elif opt == 'V':
            print_report(students)
        elif opt == 'F':
            find_performers(students)
        elif opt == 'Q':
            break
        else:
            print('Invalid input. Please input either \'A\', \'V\', \'F\', or \'Q\'.')

menu()


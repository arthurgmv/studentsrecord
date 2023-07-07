# By Arthur Gabriel (github.com/arthurgmv)
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def adicionar_nota(self, grades):
        self.grades.append(grades)

    def calcular_media(self):
        if len(self.grades) > 0:
            media = sum(self.grades) / len(self.grades)
            return media
        else:
            return 0

Studentslist = []

def cadastrar_aluno():
    name = input("Type student's name: ")
    age = int(input("Type students age: "))
    # Create a new instance of the Student class
    student = Student(name, age)
    Studentslist.append(student)
    print("Student files recorded successfully!")

def adicionar_nota_aluno():
    name = input("Type student's name: ")
    student_found = None
    # Iterate over the Studentslist to find the student with the matching name
    for student in Studentslist:
        if student.name == name:
            student_found = student
            break
    if student_found:
        grade = float(input("Insert Student's grade: "))
        # Call the adicionar_nota method of the found student
        student_found.adicionar_nota(grade)
        print("Grade recorded successfully!")
    else:
        print("Student not found.")

def exibir_media_aluno():
    name = input("Type student's name: ")
    student_found = None
    # Iterate over the Studentslist to find the student with the matching name
    for student in Studentslist:
        if student.name == name:
            student_found = student
            break
    if student_found:
        # Call the calcular_media method of the found student
        media = student_found.calcular_media()
        print("The student final grade", student_found.name, "is:", media)
    else:
        print("Student not found.")

def exibir_menu():
    print("1. Record student")
    print("2. Add student grade")
    print("3. Show student final grade")
    print("4. Exit")

def main():
    while True:
        exibir_menu()
        opcao = input("Type the desired option: ")
        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            adicionar_nota_aluno()
        elif opcao == "3":
            exibir_media_aluno()
        elif opcao == "4":
            break
        else:
            print("Invalid option. Try again.")

main()

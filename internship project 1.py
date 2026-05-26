students=[]

def add_student():
    name=input("Enter student's name:")
    age=input("Enter student's age:")
    marks=input("Enter the marks:")
    subject=input("Enter the subjects:")

    student=[name,age,marks,subject]
    students.append(student)

    print("student added sucessfully!1")

def view_student():
    if len(students)==0:
        print("student details not added yet!")
        return
    
    print("\nNO.| name| age | marks | subject ")
    print("________________________________________")

    for i in range(len(students)):
        s=students[i]
        print(i+1, "|", s[0], "|", s[1], "|", s[2], "|", s[3])

def delete_student():
        view_student()
        num=int(input("enter the number of student to be removed:"))
        removed=students.pop(num-1)
        print(removed[0],"deleted!")
def edit_student():
    view_student()
    num=int(input("enter the number of student to be edited:"))

    s=students[num-1]
    new_name    = input("New name    (" + s[0] + "): ")
    new_age     = input("New age     (" + s[1] + "): ")
    new_marks   = input("New marks   (" + s[2] + "): ")
    new_subject = input("New subject (" + s[3] + "): ")

    if new_name !="":s[0]=new_name
    if new_age !="":s[1]=new_age
    if new_marks !="":s[2]=new_marks
    if new_subject!="":s[3]=new_subject

    print("edited successfully")

while True:
    print(".......student records........")
    print("1. add student record")
    print("2. view student record")
    print("3. edit student record")
    print("4. delete student record")
    print("5. exit")
        
    option=input("select your choice:")
    if option =="1":add_student()
    elif option=="2":view_student()
    elif option=="3":edit_student()
    elif option=="4":delete_student()
    elif option=="5":
      print("exiting...!")
      break
    else:
      print("invalid option..!")

            

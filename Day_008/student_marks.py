print("================== Student Record=======================")

marks = []

total_students = int(input("Enter Number of Students: "))

for student in range (1, total_students + 1):
    mark = int(input("Enter marks: "))
    name = input("Student Name: ")
    print(f"Student {student}  {name}  Marks : {mark}")
    marks.append(mark)

    print(f"Student Marks : {marks}")

print("=========================================================")

print("===========Student Record Stats==========================")

print(f"Maximum Marks : {max(marks)}")
print(f"Minimum Marks : {min(marks)}")
print(f"Total Students : {len(marks)}")

print("=========================================================")

print("=================Student Status==========================")

fifty_plus_marks = 0
fifty_below_marks = 0

for mark in marks:

    if mark > 50:
       
     
        fifty_plus_marks += 1

       

    else:
       
       
        fifty_below_marks += 1

        print(f"Qualified Students: {fifty_plus_marks}")
                

        print(f"Not Qualified Students : {fifty_below_marks}")
        


    

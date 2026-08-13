print("====================Employee Records====================")

employees = [
    {
        "name":"Aaron",
        "role":"Data Analyst",
        "salary":40000,
        "location":"Delhi",
        "company":"Microsoft"},

        {"name":"John",
        "role":"AWS Engineer",
        "salary":80000,
        "location":"Mumbai",
        "company":"Amazon"},

         {"name":"Deepu",
        "role":"Python Developer",
        "salary":40000,
        "location":"Hyderabad",
        "company":"Google"},
        
]

print("===========================================================")
print("===========Employee Individual Record===========")
print(employees[0]["name"])
print(employees[0]["role"])
print(employees[0]["salary"])
print(employees[0]["location"])
print(employees[0]["company"])

print("================================================")

print(employees[1]["name"])
print(employees[1]["role"])
print(employees[1]["salary"])
print(employees[1]["location"])
print(employees[1]["company"])

print("================================================")

print(employees[2]["name"])
print(employees[2]["role"])
print(employees[2]["salary"])
print(employees[2]["location"])
print(employees[2]["company"])

print("================================================")

employees[0]["skills"] = ["Python","Excel"]
employees[1]["skills"] = ["Python","SQL","AWS","Docker"]
employees[2]["skills"] = ["R","Google Sheets", "Power BI","GCP"]

print("==================================================")

for employee in employees:

    print(f"Empolyee Name : {employee}['name']skills: ")

    for skill in employee["skills"]:
        print(skill)

print("============Skill Loop Analysis===============")

for employee in employees:

    if employee["salary"] >= 80000:
        print("High Salary")

    elif employee["salary"]>=60000:
        print("Excellent Salary")

    else:
        print("Good Salary")

print("=======================End of Report==================")

    
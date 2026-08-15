print("==================== UK MSc Admission Report ====================")


def student_funds(name, funds):

    if funds < 20000:
        print(f"Hey {name}, funds are not sufficient.")

    elif funds < 80000:
        print(f"Hey {name}, admission may require additional financial review.")

    elif funds <= 100000:
        print(f"Hey {name}, funds requirement for this practice project is met.")

    else:
        print(f"Hey {name}, funds are more than sufficient for this practice project.")


student_funds("David", 150000)
student_funds("Amelia", 72000)


def student_language(name, country):

    country = country.strip().lower()

    if country == "india":
        print(f"Hey {name}, English language assessment may be required.")

    elif country == "srilanka":
        print(f"Hey {name}, please check the university language requirements.")

    else:
        print(f"Hey {name}, please verify the university language requirements.")


student_language("David", "France")
student_language("Amelia", "Srilanka")


def student_status(name, funds, country):

    country = country.strip().lower()

    if 80000 <= funds <= 100000 and country == "india":
        print(f"Hey {name}, you meet the practice eligibility conditions.")

    elif funds < 20000:
        print(f"Hey {name}, unfortunately the funds requirement is not met.")

    else:
        print(f"Hey {name}, your application requires further review.")


student_status("David", 99000, "France")
student_status("Amelia", 75000, "Srilanka")


print("================================================================")
print("This is a beginner Python practice project using fictional rules.")
print("======================= End of Report ==========================")
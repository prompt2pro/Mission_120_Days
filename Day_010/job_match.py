print("===============Job Application Match=================")

job_skills = {"Python","SQL","Excel","Power BI","AWS"}

my_skills = {"Python","Excel","Tableau"}

total_skills = job_skills.union(my_skills)

matched_skills = job_skills & my_skills

missing_skills = job_skills - my_skills

extra_skills = my_skills - job_skills

print(f"Total Skills : {total_skills}")
print(f"Matched Skills : {matched_skills}")
print(f"Missing Skills : {missing_skills}")
print(f"Extra Skills : {extra_skills}")

print("========================================================")

print("=================Skills Analysis========================")

total = len(job_skills)

required = len(matched_skills)

shortage = len(missing_skills)

skill_match_percentage = required/total*100

shortage_skill_percentage = shortage/total*100

print(f"Matched Skills Percentage : {skill_match_percentage: .2f}%")
print(f"Shortage Skills Percentage : {shortage_skill_percentage: .2f}%")

print("=============================================================")

print("====================Job Reporting============================")

if skill_match_percentage >= 80:
    print("Excellent Fit for the Job")

elif 80 > skill_match_percentage and skill_match_percentage >= 60:
    print("Good Enough")

elif 60 > skill_match_percentage and skill_match_percentage >= 40:
    print("Improvement Needed")

else:
    print("Unfortunately required skills are missing.")

print("=================Thank you for watching & if you like practice sessions and content, please subscribe.======")

print("===================Thank You=====================")
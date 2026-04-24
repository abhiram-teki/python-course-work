jd={'python','mysql','javascript','flask'}
skills=set(input("Enter the skills: ").split())
if jd==skills:
    print("Shortlisted.")
else:
    print(f'Sorry, insufficient skillset. You need {jd-skills}')

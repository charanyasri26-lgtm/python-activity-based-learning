subjects = ["Python", "Maths", "English"]
exam1 = [60, 75, 80]
exam2 = [70, 65, 85]

for i in range(len(subjects)):
    difference = exam2[i] - exam1[i]

    print("\nSubject:", subjects[i])
    print("First Exam:", exam1[i])
    print("Second Exam:", exam2[i])

    if difference > 0:
        print("Improved by", difference, "marks")
    elif difference < 0:
        print("Declined by", -difference, "marks")
    else:
        print("No Change")

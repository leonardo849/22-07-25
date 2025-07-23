quantityOfPeople = int(input("how many people do you want to create?"))

dayShifts = ["M", "A", "N"]
acceptedStudents = []
reprovedStudents = []
for i in range(quantityOfPeople):
    dayShift = ""
    while dayShift not in dayShifts:
        dayShift = input("what day shift do you want to study in").upper()
    age = int(input("how old are you?"))
    errors = 0
    accepted = False
    while not accepted and errors < 2:
        if dayShift == "M" and (age < 15 or age > 25):
            errors += 1
            print("reproved")
            age = int(input("how old are you?"))
        elif  dayShift == "A" and (age < 18 or age > 35):
            errors += 1
            print("reproved")
            age = int(input("how old are you?"))
        elif dayShift == "N" and age < 26 :
            errors += 1
            print("reproved")
            age = int(input("how old are you?"))
        else:
            accepted = True
    
    if errors == 2:
        print("that student was reproved three in a row. next")
        reprovedStudents.append({"day_shift": dayShift, "age": age, "approved": False})
        continue
    
    acceptedStudents.append({"day_shift": dayShift, "age": age, "approved": True})
    print("aproved")


allOfStudents = acceptedStudents + reprovedStudents


for dayshift in dayShifts:
    print("day shift:", dayshift)
    reprovedStudents = list(filter(lambda student: student["approved"] == False and student["day_shift"] == dayshift, allOfStudents))
    approvedStudents = list(filter(lambda student: student["approved"] == True and student["day_shift"] == dayshift, allOfStudents))
    print(f"approved students in {dayshift} shift: {approvedStudents}, quantity of them: {len(approvedStudents)}")
    print(f"reproved students in {dayshift} shift: {reprovedStudents}, quantity of them: {len(reprovedStudents)}")
    print(f"quantity of students: {len(reprovedStudents) + len(approvedStudents)}")
    

canContinue = True
patients = []



# i can't use while True teacher i know, but that while can be True or False. So technically, it isn't a while True
while canContinue == True:
    
    if len (patients) > 0:
        wantsToContinue = input("Do you want to continue creating patients?").upper()
        if wantsToContinue == "N":
            canContinue = False
            continue
   

    patient = {
        "name": "",
        "age": 0,
        "symptom": 0,
        "high_fever": False,
        "dificulty_breathing": False,
        "several_pain": False,
        "priority": 1
    }
    patientInfo = input("what are the patient's infos? name space age space symptom").split(" ")
    patient["name"] = patientInfo[0]
    patient["age"] = int(patientInfo[1])
    patient["symptom"] = patientInfo[2]  

    doesPatientHaveHighFever = input("does patient have high fever?").upper()

    if doesPatientHaveHighFever == "Y":
        patient["high_fever"] = True

    doesPatientHaveDificultyBreathing = input("does patient have dificulty breathing").upper()

    if doesPatientHaveDificultyBreathing == "Y":
        patient["dificulty_breathing"] = True
    
    doesPatientHaveSeveralPain = input("does patient have several pain?").upper()

    if doesPatientHaveSeveralPain == "Y":
        patient["several_pain"] = True


    if patient["dificulty_breathing"] or patient["high_fever"] or patient["several_pain"]:
        filter = dict(filter(lambda property: property[1] == True, patient.items()))
        if len(filter) == 1:
            patient["priority"] = 2
        elif len(filter) >= 2 or patient["age"] >= 60:
            patient["priority"] = 3
    

    patients.append(patient)


print("quantity of patients:", len(patients))

groupOfRisk = [patient for patient in patients if patient["priority"] == 3]


print(f"quantity of people in group of risk {len(groupOfRisk)}")


for priority in range(1, 4):
    group = [patient for patient in patients if patient["priority"] == priority]
    print(f"quantity people in priority {priority}: {len(group)}")
    


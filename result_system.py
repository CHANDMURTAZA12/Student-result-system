students={
    "Chand":{
        "Age":20,
        "city":"Lahore",
        "Marks":[85,90,78,92,88]
    },
    
    "Ali":{
        "Age":22,
        "city":"Karachi",
        "Marks":[70,65,80,75,60]
    },
    "Sara":{
        "Age":21,
        "city":"Lahore",
        "Marks":[92,95,88,97,90]
    },
    "Umar":{
        "Age":20,
        "city":"Islamabad",
        "Marks":[55,60,50,65,58]
    },
    "Zara":{
        "Age":23,
        "city":"Karachi",
        "Marks":[78,82,80,75,85]
    }
}
topper=""
highest_average=0
weakest=""
lowest_average=1000
Grade_A=0
Grade_B=0
Grade_C=0
Grade_D=0
Grade_F=0
lahori=0
for name,details in students.items():
    total=0
    grade=""
    
    for mark in details['Marks']:
       
        total+=mark
    average=total/len(details["Marks"])
    if average>=90:
        grade="A"
        Grade_A+=1
    elif average>=80:
        grade="B"
        Grade_B+=1
    elif average>=70:
        grade="C"
        Grade_C+=1
    elif average>=60:
        grade="D"
        Grade_D+=1
    else:
        grade="F"
        Grade_F+=1
    
    print(f"----- {name} ----")
    print(f"Age:{details['Age']}")
    print(f"City:{details["city"]}")
    print(f"Total Marks:{total}")
    print(f"Average:{average}")
    print(f"Grade:{grade}")

    # finding topper
    if average>highest_average:
        highest_average=average
        topper=name
    if average<lowest_average:
        lowest_average=average
        weakest=name
    if details["city"]=="Lahore":
        lahori+=1

        
print("---------------Topper--------------")
print(f"Topper: {topper} Highest Average:{highest_average}")
print("---------------Weakest--------------")
print(f"weakest: {weakest} Highest Average:{lowest_average}")
print("----------count of Students with their grades")
print(f"count of students with A grade:{Grade_A}")
print(f"count of students with B grade:{Grade_B}")
print(f"count of students with C grade:{Grade_C}")
print(f"count of students with D grade:{Grade_D}")
print(f"count of students with F grade:{Grade_F}")
print("-----------Count of students from Lahore--------")
print(f"count of Students from Lahore :{lahori}")
print("-----------Students with Average above 75---------------")
for name,details in students.items():
    total=0
    for mark in details["Marks"]:
        total+=mark
    average=total/len(details["Marks"])
    if average>75:
         print(f"student name:{name} ,ciyt:{details["city"]} ,total marks :{total} average:{average}")

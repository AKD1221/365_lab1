import pandas as pd

def main():
    listcsv = pd.read_csv("list.txt", header=None)
    listcsv.columns = ["StLastName", "StFirstName", "Grade", "Classroom", "Bus", "GPA"]

    teachercsv = pd.read_csv("teachers.txt", header=None)
    teachercsv.columns = ["TLastName", "TFirstName", "Classroom"]
    #print(mycsv)

    while(True):
        command = input("Enter command for schoolsearch: ").split()
        #print(command)

        if (len(command) > 3):
            print("Invalid Command")

        elif (command[0] == "S:" or command[0] == "Student:"):

            #Implements requirement R4
            if (len(command) == 2):
                search = listcsv[listcsv["StLastName"]==command[1]]
                for x in range(len(search)):
                    myrow = search.iloc[x]
                    teacher = teachercsv[teachercsv["Classroom"]==myrow["Classroom"]].iloc[0]
                    print(myrow["StLastName"] + ", " + myrow["StFirstName"] + ", " + str(myrow["Grade"]) + ", " + str(myrow["Classroom"]) + ", " + teacher["TLastName"] + ", " + teacher["TFirstName"])

            #Implments requirement R5
            elif (len(command) == 3 and (command[2] == "B" or command[2] == "Bus")):
                search = listcsv[listcsv["StLastName"]==command[1]]
                for x in range(len(search)):
                    myrow = search.iloc[x]
                    print(myrow["StLastName"] + ", " + myrow["StFirstName"] + ", " + str(myrow["Bus"]))
    
        #Implements requirement R6
        elif ((command[0] == "T:" or command[0] == "Teacher:") and len(command) == 2):
            search = teachercsv[teachercsv["TLastName"]==command[1]]
            temp = search.iloc[0]["Classroom"]
            search2 = listcsv[listcsv["Classroom"]==temp]
            for x in range(len(search2)):
                myrow = search2.iloc[x]
                print(myrow["StLastName"] + ", " + myrow["StFirstName"])

        elif (command[0] == "G:" or command[0] == "Grade:"):

            #Implements requirement R7
            if (len(command) == 2):
                search = listcsv[listcsv["Grade"]==int(command[1])]
                #print(search)
                for x in range(len(search)):
                    myrow = search.iloc[x]
                    print(myrow["StLastName"] + ", " + myrow["StFirstName"])

            #Implements requirement for NR3
            elif (len(command) == 3 and (command[2] == "T" or command[2] == "Teacher")):
                search = listcsv[listcsv["Grade"] == int(command[1])]
                classrooms = search["Classroom"].unique()
                teachers = teachercsv[teachercsv["Classroom"].isin(classrooms)]
                for x in range(len(teachers)):
                    myrow = teachers.iloc[x]
                    print(myrow["TLastName"] + ", " + myrow["TFirstName"])
            
            #Implements requirement R8 for high
            elif (len(command) == 3 and (command[2]=="H" or command[2]=="High")):
                search = listcsv[listcsv["Grade"]==int(command[1])]
                high = search["GPA"].max()
                for x in range(len(search)):
                    myrow = search.iloc[x]
                    if (myrow["GPA"]==high):
                        teacher = teachercsv[teachercsv["Classroom"]==myrow["Classroom"]].iloc[0]
                        print(myrow["StLastName"] + ", " + myrow["StFirstName"] + ", " + str(myrow["GPA"]) + ", " + teacher["TLastName"] + ", " + teacher["TFirstName"] + ", " + str(myrow["Bus"]))  

            #Implements requirement R8 for low
            elif (len(command) == 3 and (command[2]=="L" or command[2]=="Low")):
                search = listcsv[listcsv["Grade"]==int(command[1])]
                low = search["GPA"].min()
                for x in range(len(search)):
                    myrow = search.iloc[x]
                    if (myrow["GPA"]==low):
                        teacher = teachercsv[teachercsv["Classroom"]==myrow["Classroom"]].iloc[0]
                        print(myrow["StLastName"] + ", " + myrow["StFirstName"] + ", " + str(myrow["GPA"]) + ", " + teacher["TLastName"] + ", " + teacher["TFirstName"] + ", " + str(myrow["Bus"])) 

        #Implements requirement R8
        elif ((command[0] == "B:" or command[0] == "Bus:") and len(command)==2):
            search = listcsv[listcsv["Bus"]==int(command[1])]
            for x in range(len(search)):
                myrow = search.iloc[x]
                print(myrow["StLastName"] + ", " + myrow["StFirstName"] + ", " + str(myrow["Grade"]) + ", " + str(myrow["Classroom"]))

        #Implements requirement R10
        elif ((command[0] == "A:" or command[0] == "Average:") and len(command)==2):
            search = listcsv[listcsv["Grade"]==int(command[1])]
            if not search.empty:
                print("Grade " + command[1] + " has average GPA of " + str(search["GPA"].mean()))

        #Implements NR1 and NR2
        # C: 103 S or C: 103 T
        elif ((command[0] == "C:" or command[0] == "Classroom:") and len(command)==3):
            if (command[2] == "S" or command[2] == "Student"):
                search = listcsv[listcsv["Classroom"] == int(command[1])]
                for x in range(len(search)):
                    myrow = search.iloc[x]
                    print(myrow["StLastName"] + ", " + myrow["StFirstName"])

            elif (command[2] == "T" or command[2] == "Teacher"):
                search = teachercsv[teachercsv["Classroom"] == int(command[1])]
                for x in range(len(search)):
                    myrow = search.iloc[x]       
                    print(myrow["TLastName"] + ", " + myrow["TFirstName"])         

        elif ((command[0]=="E" or command[0]=="Enrollment")):
            classrooms = listcsv["Classroom"].unique()
            classrooms.sort()
            
            for classroom in classrooms:
                size = len(listcsv[listcsv["Classroom"]==classroom])
                print(str(classroom) + " has " + str(size) + " students")


           

        #Implements requirement R11
        elif (command[0] == "I" or command[0] == "Info"):
            print(listcsv["Grade"].value_counts(ascending=True))

        #Implements requirement R12
        elif (command[0] == "Q" or command[0] == "Quit"):
            return()

        else:
            print("Invalid Command")



if __name__ == "__main__":
    main()
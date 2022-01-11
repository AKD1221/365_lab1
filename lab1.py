import pandas as pd

def main():
    mycsv = pd.read_csv("students.txt", header=None)
    mycsv.columns = ["StLastName", "StFirstName", "Grade", "Classroom", "Bus", "GPA", "TLastName", "TFirstName"]
    #print(mycsv)

    while(True):
        command = input("Enter command for schoolsearch: ").split()
        #print(command)

        if (len(command) > 3):
            print("Invalid Command")

        elif (command[0] == "S:" or command[0] == "Student:"):

            #Implements requirement R4
            if (len(command) == 2):
                search = mycsv[mycsv["StLastName"]==command[1]]
                for x in range(len(search)):
                    myrow = search.iloc[x]
                    print(myrow["StLastName"] + ", " + myrow["StFirstName"] + ", " + str(myrow["Grade"]) + ", " + str(myrow["Classroom"]) + ", " + myrow["TLastName"] + ", " + myrow["TFirstName"])

            #Implments requirement R5
            elif (len(command) == 3 and (command[2] == "B" or command[2] == "Bus")):
                search = mycsv[mycsv["StLastName"]==command[1]]
                for x in range(len(search)):
                    myrow = search.iloc[x]
                    print(myrow["StLastName"] + ", " + myrow["StFirstName"] + ", " + str(myrow["Bus"]))
    
        #Implements requirement R6
        elif ((command[0] == "T:" or command[0] == "Teacher:") and len(command) == 2):
            search = mycsv[mycsv["TLastName"]==command[1]]
            for x in range(len(search)):
                myrow = search.iloc[x]
                print(myrow["StLastName"] + ", " + myrow["StFirstName"])

        elif (command[0] == "G:" or command[0] == "Grade:"):

            #Implements requirement R7
            if (len(command) == 2):
                search = mycsv[mycsv["Grade"]==int(command[1])]
                #print(search)
                for x in range(len(search)):
                    myrow = search.iloc[x]
                    print(myrow["StLastName"] + ", " + myrow["StFirstName"])
            
            #Implements requirement R8 for high
            elif (len(command) == 3 and (command[2]=="H" or command[2]=="High")):
                search = mycsv[mycsv["Grade"]==int(command[1])]
                high = search["GPA"].max()
                for x in range(len(search)):
                    myrow = search.iloc[x]
                    if (myrow["GPA"]==high):
                        print(myrow["StLastName"] + ", " + myrow["StFirstName"] + ", " + str(myrow["GPA"]) + ", " + myrow["TLastName"] + ", " + myrow["TFirstName"] + ", " + str(myrow["Bus"]))  

            #Implements requirement R8 for low
            elif (len(command) == 3 and (command[2]=="L" or command[2]=="Low")):
                search = mycsv[mycsv["Grade"]==int(command[1])]
                low = search["GPA"].min()
                for x in range(len(search)):
                    myrow = search.iloc[x]
                    if (myrow["GPA"]==low):
                        print(myrow["StLastName"] + ", " + myrow["StFirstName"] + ", " + str(myrow["GPA"]) + ", " + myrow["TLastName"] + ", " + myrow["TFirstName"] + ", " + str(myrow["Bus"])) 

        #Implements requirement R8
        elif ((command[0] == "B:" or command[0] == "Bus:") and len(command)==2):
            search = mycsv[mycsv["Bus"]==int(command[1])]
            for x in range(len(search)):
                myrow = search.iloc[x]
                print(myrow["StLastName"] + ", " + myrow["StFirstName"] + ", " + str(myrow["Grade"]) + ", " + str(myrow["Classroom"]))

        #Implements requirement R10
        elif ((command[0] == "A:" or command[0] == "Average:") and len(command)==2):
            search = mycsv[mycsv["Grade"]==int(command[1])]
            if not search.empty:
                print("Grade " + command[1] + " has average GPA of " + str(search["GPA"].mean()))
           

        #Implements requirement R11
        elif (command[0] == "I" or command[0] == "Info"):
            print(mycsv["Grade"].value_counts(ascending=True))

        #Implements requirement R12
        elif (command[0] == "Q" or command[0] == "Quit"):
            return()

        else:
            print("Invalid Command")



if __name__ == "__main__":
    main()
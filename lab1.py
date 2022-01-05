import pandas as pd

def main():
    mycsv = pd.read_csv("students.txt", header=None)
    mycsv.columns = ["StLastName", "StFirstName", "Grade", "Classroom", "Bus", "GPA", "TLastName", "TFirstName"]
    print(mycsv)

    while(True):
        command = input("Enter command for schoolsearch: ").split()
        print(command)

        if (len(command) > 3):
            print("Incorrect command")

        elif (command[0] == "S:" or command[0] == "Student:"):

            if (len(command) == 2):
                search = mycsv[mycsv["StLastName"]==command[1]]
                for x in range(len(search)):
                    myrow = search.iloc[x]
                    print(myrow["StLastName"] + ", " + myrow["StFirstName"] + ", " + str(myrow["Grade"]) + ", " + str(myrow["Classroom"]) + ", " + myrow["TLastName"] + ", " + myrow["TFirstName"])
        
        elif (command[0] == "T:" or command[0] == "Teacher:"):
            print("Teacher")
        
        elif (command[0] == "B:" or command[0] == "Bus:"):
            print("Bus")

        elif (command[0] == "G:" or command[0] == "Grade:"):
            print("Grade")

        elif (command[0] == "A:" or command[0] == "Average:"):
            print("Average")

        elif (command[0] == "I" or command[0] == "Info"):
            print("Info")
            print(mycsv["Grade"].value_counts(ascending=True))

        elif (command[0] == "Q" or command[0] == "Quit"):
            return()
        
        else:
            print("Incorrect command!")

        
    pass




if __name__ == "__main__":
    main()
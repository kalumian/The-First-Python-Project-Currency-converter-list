#  Start Prog

# Welcome Print -!

welcome = "|-- Welcome to the program for creating currency converter lists --|".title()
print(len(welcome) * "_" + "\n")
print(welcome)
print(len(welcome) * "_")

# Questions For Create File

nameFile = input("What is the name of the file you want to create?: ".title())
print("")  # New Line

# Function to Ask Dose He Want Change Path Yes Or Not
def AskDoseHeWantChangePath():
    ac = input(
        "Do you want to change the path of the file or create it in the current path? (Y,N): ".title())
    if ac == "y" or ac == "Y" or ac == "n" or ac == "N":
        return ac
    else:
        AskDoseHeWantChangePath()


AcPath = AskDoseHeWantChangePath()
Path = False

if AcPath == "y" or AcPath == "Y":
    Path = input("Select the path correctly: ".title())
print("")  # New Line


def isNum(num):
    res = []
    for ch in num:
        if ch == "1" or ch == "2" or ch == "3" or ch == "4" or ch == "5" or ch == "6" or ch == "7" or ch == "8" or ch == "9" or ch == ".":
            res.append(True)
        else:
            res.append(False)
    return all(res)

# Get Names
def getName(n):
    kind = n
    res = name = input(f"What is the name of the {kind} coin?: ".title())
    if isNum(name):
        print("-----------------------------------------------------------")
        print("There was an error processing the name..try again please !!".title())
        print("------------------------------------------------------------")
        res = getName(kind)
    
    return res
firstName = getName("First".title())
print("")  # New Line
secondName = getName("Second".title())


print("")  # New Line
# Function To Get Rate
def inputRate():
    res = []
    res = number = input("Enter the rate of difference between the two currencies: ".title())
    if not isNum(number):
        print("----------------------------------------------------------")
        print("There was an error processing the rate..try again please!!".title())
        print("----------------------------------------------------------")
        res = inputRate()
  
    return res
rate = inputRate()
print("")  # New Line

From = input("The list starts with: ".title())

To = input("to the number: ".title())

    
        


def createList(file = nameFile , name1 = firstName , name2 = secondName, Rate = rate , path = Path, To = To , From = From):
    if path == False:
        file = open(f"{file}.txt", "a")
    else:
        file = open(f"{path}/{file}.txt", "a")

    file.write("---This program was created by Mohamed Kalumian-- \n \n")
        
    for n in range(int(To) - int(From) + 2):
        file.write(
            f"\n \n{name2} : {n} =  {name1} : {round(float(Rate) * n,2)}\n \n_________________________________")

    file.close()
    print("successfully done !!".title())

createList()


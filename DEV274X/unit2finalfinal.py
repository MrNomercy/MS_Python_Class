##def return open .readline() .append() .strip() input len if .upper() or .lower()
##for / in print


elements_20 = open('elements1_20.txt','r')
elements = elements_20.read()
myelements = elements.split("\n")
myelement = []
for i in range(len(myelements)):
    element = myelements[i].lower()
    myelement.append(element)
elements_20.close()

mylist =[]
found = []
not_found = []

def get_names():
    while len(mylist) < 5:        
        myinput = input("Enter the name of an element: ").lower()
        while not myinput:
            myinput = input("Enter the name of an element: ").lower()
        if myinput in mylist:
            print(myinput,"was already entered")
        else:
            if myinput in myelement:
                mylist.append(myinput)
                found.append(myinput.title())
            elif myinput == "kejfaijdkej;aklf":
                return ""
            else:
                mylist.append(myinput)
                not_found.append(myinput.title())


print("list any 5 of the first 20 elements in the Period table")
get_names()    
print("\n")
print(len(found)*20,"% correct")
print("Found: ",end="")
for i in found:
    print(i,end=" ")
print('\nNot found: ',end='')
for i in not_found:
    print(i,end=" ")

elements_20 = open('elements1_20.txt','r')
elements = elements_20.readline().strip()

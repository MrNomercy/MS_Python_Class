# def return print() input() if in .append() .pop() .remove()

animal_list = ['cat','goat','cat']

def list_o_matic(animal):
    if animal == "":
        show = animal_list[-1]
        animal_list.pop()
        message = show+" popped form the list\n"
        return message
    else:
        if animal in animal_list:
            item = str(animal_list.remove(animal))
            message = "1 instance of "+animal+" removed from list\n"
            return message
        else:
            item = str(animal_list.append(animal))
            message = "1 instance of "+animal+" appended to list\n"
            return message


while animal_list:
    print("look at all the animals",animal_list)
    myinput = input("enter the name of an animal: ")
    if myinput == "Quit":
        print("\nGoodbye!")
        break
    else:
        result = list_o_matic(myinput)
        print(result)
        if animal_list == []:
            print("Goodbye!")
    
            
    

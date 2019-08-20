print('Input an interger to add to the total or "Q" to quit')
total = list()

def adding_report(A):
    total.append(int(A))
    return total
    
while True:
    inp_value = input('Enter an integer or "Q": ')
    if inp_value.isdigit():
        result = adding_report(inp_value)
    elif inp_value == "q":
        print("Items")
        for i in range(len(total)):
            item = total[i]
            print(item)
        print("\nTotal")
        print(sum(total))
        break
    elif inp_value.startswith("Q"):
        print("Total")
        print(sum(total))
        break
    else:
        print(inp_value,"is invalid input")


        

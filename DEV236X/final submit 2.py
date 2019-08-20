

def adding_report(T):
    total = 0
    items = ""
    while True:
        myinput = input('Enter an integer or "Q": ')
        if myinput.isdigit():
            total += int(myinput)
            if report.upper().startswith("A"):
                items += myinput + "\n"
        elif myinput.upper().startswith("Q"):
            if report.upper().startswith("A"):
                print('\nItems')
                print(items)
                print('Total')
                print(total)
                print(" ")
                break
            elif report.upper().startswith("T"):
                print('\nTotal')
                print(total)
                print(" ")
                break
        else:
            print(myinput,"is invalid input")


print('Report Types include All Items ("A")or Total Only ("T")')
while True:
    get_input = input('Choose Report Type ("A" or "T"): ')
    if get_input.upper().startswith("A"):
        report = "A"
        result = adding_report(report)
        print(result)
        break
    elif get_input.upper().startswith("T"):
        report = "T"
        result = adding_report(report)
        print(result)
        break
    else:
        print(get_input,"is invalid input")

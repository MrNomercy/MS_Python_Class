def fishstore(fish,price):
    result = ("Fish Type : "+fish+" costs $"+price)
    return result
fish_entry = input("enter fish name: ")
price_entry = input("enter the fish price (no symbols): ")

final = fishstore(fish_entry,price_entry)
print(final)

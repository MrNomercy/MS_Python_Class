# print() input() for/in .isalpha() if else .upper() or .lower()
# Wheresoever you go, go with all your heart

quote = input("enter a 1 sentence quote, non-alpha separate words: ")+" "
word = ""

for character in quote:
    if character.isalpha():
        word += character
    elif character.isalpha() == False:
        if word.lower() >= "h":
            print(word.upper())
            word = ""
        else:
            word = ""
    else:
        word = ""


        

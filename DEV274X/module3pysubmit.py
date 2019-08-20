# def, return, print, if, input, for/in, .lower&.upper, .append, .pop, .split
# len, range
# Little fly, Thy summer’s play My thoughtless hand Has brushed away. Am not I A fly like thee? Or art not thou A man like me?

first_list = []
new_list = []

def word_mixer(word_list):
    word_list.sort()
    while len(word_list)>5:
        new_list.append(word_list.pop(-5))
        new_list.append(word_list.pop(0))
        new_list.append(word_list.pop(-1))

poem = input("enter a saying or poem: ")
my_word_list = poem.split()

mylen = len(my_word_list)
for word in my_word_list:
    if len(word) <= 3:
        first_list.append(word.lower())
    elif len(word) >= 7:
        first_list.append(word.upper())
    else:
        first_list.append(word)

word_mixer(first_list)

for words in new_list:
    print(words, end=" ")

print()
for words in range(len(new_list)):
    print(new_list[words], end=" ")


##first_list = []
##new_list = []
##
##def word_mixer(word_list):
##    word_list.sort()
##    while len(word_list)>5:
##        new_list.append(word_list.pop(-5))
##        new_list.append(word_list.pop(0))
##        new_list.append(word_list.pop(-1))
##        if len(word_list)<5:
##            return ""
##            break
##
##poem = input("enter a saying or poem: ")
##my_word_list = poem.split()
##
##mylen = len(my_word_list)
##for word in my_word_list:
##    if len(word) <= 3:
##        first_list.append(word.lower())
##    elif len(word) >= 7:
##        first_list.append(word.upper())
##    else:
##        first_list.append(word)
##
##word_mixer(first_list)
##
##for words in new_list:
##    print(words, end=" ")
##    
##print("\n")
##
##for i in range(0,len(new_list),3):
##    print(new_list[i],new_list[int(i)+1],new_list[int(i)+2])














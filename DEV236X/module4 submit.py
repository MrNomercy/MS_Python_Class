
def str_analysis(my_string):
  if my_string.isdigit():
      if int(my_string)>99:
          return my_string+" is a pretty big number"
      elif int(my_string)<=99:
          return my_string+" is a smaller number than expected"
  else:
       if my_string.isalpha():
          return '"'+my_string+'"'+" is all alphabetical characters!"
       else:
          return '"'+my_string+'"'+" is a surprise! It\'s neither all alpha nor all digit characters!"

my_input = input("enter word or interger: ")
while my_input == "":
    my_input = input("enter word or interger: ")

result = str_analysis(my_input)
print(result)
        






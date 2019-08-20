
order = input("Enter cheese order weight (numeric value): ")
if float(order) > 100:
    print(float(order),"is more than currently available stock")
elif float(order) < .25:
    print (float(order),"is below minimum order amount")
else:
    print(float(order),"costs $",float(order)*7.99)


           

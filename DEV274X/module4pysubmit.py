##print() while .split() open .readline() .seek() .write() .close()

!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/world_temp_mean.csv -o mean_temp.txt

new_file = open('mean_temp.txt','a+')
new_file.write("Rio de Janeiro,Brazil,30.0,018.0\n")

new_file.seek(0)
headings = new_file.readline().strip()
myheading = headings.split(',')

city_temp = []
line = new_file.readline().strip()
while line:
    city_temp.append(line)
    line = new_file.readline().strip()

new_file.close()
print()
for i in city_temp:
    info = i.split(',')
    print(myheading[0],"of",info[0],myheading[2],"is",info[2],"Celsius")

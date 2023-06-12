with open('C:\Python\01_python-workspace\99_Test\result02.txt', 'r') as file:
    data = file.readlines()

myfile2 = open('C:\Python\01_python-workspace\99_Test\sample02.txt', 'w')

for line in data:
    name, age = line.strip().split(',')
    if int(age) >= 19:
        status = '성인'
    else:
        status = '미성년'
    result = name + '/' + status
    myfile2.write(result + '\n')
myfile2.close()

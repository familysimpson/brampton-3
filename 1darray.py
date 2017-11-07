#1D ARRAY
#7/11/17


# DECLARE AGES : INTEGER

ages = []
for p in range (0,10):
    num=int(input("Enter Num between 0 and 10"))
    while num < 0 or num > 10:
        print("ERROR NOT VALID SILLY")
        num = int(input("Enter Num between 0 and 10"))

    ages.append(num)

for index in range (0,10):
    print(ages[index])




for index in range (0,10):
    for y in range (0,9):
     if ages[y]>ages[y+1]:
         temp=ages[y]
         ages[y]=ages[y+1]
         ages[y+1]=temp

for index in range (0,10):
    print(ages[index])
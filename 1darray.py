#1D ARRAY
#7/11/17


# DECLARE AGES : INTEGER
ages= [9,14,15,16,16,4,15,17,18,19]


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
mylist1 = [1, 2, 3, 4, 5, 6, 7, "NaN", 9, 10,  12, "NaN", 14]
mylist2 = [1, 2, 3, 4, 5, 6, 7, "NaN", 9, "NaN",  12, 13, 14]
mylist3 = [1, 2, 3, 4, 5, 6, 7, "NaN", 9, 10, 12, 13, 14]

for n, i in enumerate(mylist1):
     if i == "NaN":
        mylist1[n] = 0

for n, i in enumerate(mylist2):
     if i == "NaN":
        mylist2[n] = 0

for n, i in enumerate(mylist3):
     if i == "NaN":
        mylist3[n] = 0

print(mylist1 + mylist2, mylist3)

list1_save = mylist1
list2_save = mylist2

average_list = []

value1 = mylist1[0] + mylist2[0] + mylist3[0]
value2 = mylist1[1] + mylist2[1] + mylist3[1]
value3 = mylist1[2] + mylist2[2] + mylist3[2]
value4 = mylist1[3] + mylist2[3] + mylist3[3]
value5 = mylist1[4] + mylist2[4] + mylist3[4]
value6 = mylist1[5] + mylist2[5] + mylist3[5]
value7 = mylist1[6] + mylist2[6] + mylist3[6]
value8 = mylist1[7] + mylist2[7] + mylist3[7]
value9 = mylist1[8] + mylist2[8] + mylist3[8]
value10 = mylist1[9] + mylist2[9] + mylist3[9]
value11 = mylist1[10] + mylist2[10] + mylist3[10]
value12 = mylist1[11] + mylist2[11] + mylist3[11]
value13 = mylist1[12] + mylist2[12] + mylist3[12]

value1 /= 13

if mylist1[9] == 0 or mylist2[9] == 0 or mylist3[9] == 0:
    

print(value1)

























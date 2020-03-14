import numpy as np
import math
#sucseeful

mylist = [1, 2, 3, 4, 5, 6, 7, "NaN", 9, 10, 11, 12, 13, 14, "NaN", 16, 17, 18, 19, 20]
Mylist = ["a", "b", "c"]

#myarray = np.asarray(mylist, Mylist)
#print(myarray[0])
print(mylist)

for n, i in enumerate(mylist):
     if i == "NaN":
        mylist[n] = 0

print(mylist)

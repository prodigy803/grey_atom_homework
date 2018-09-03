import numpy as np
list1 = []
count_1 = 0
for i in range(1,151):
    if i % 2 == 0:
        count_1 +=1
        if count_1 > 5:
            list1.append(i)
results = list()
for x in list1:
    results.append((lambda x:x**2)(x))
arr = np.array(results)
print(arr.sum())
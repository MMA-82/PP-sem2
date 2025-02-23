from sys import getsizeof
from typing import Hashable

data = [1, "строка", 5.1, [1, 2, 3]]
for i in range(len(data)):
    print(i+1, end = "\t")
    print(data[i], end = "\t") 
    print(id(data[i]), end = "\t") 
    print(getsizeof(data[i]), end = "\t")
    if (isinstance(data[i], Hashable)): 
        print(hash(data[i]), end = "\t")
    if (isinstance(data[i], int)):
        print("Целое", end = "\t")
    if (isinstance(data[i], str)):
        print("Строка", end = "\t") 
    print()
    

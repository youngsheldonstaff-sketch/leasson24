myset = {1,2,3}
print(myset)

myset = {0.1,"hello",(1,2,3)}
print(myset)

myset = {1,2,3,4,5,5,3}
print(myset)

myset= set([1,2,3,2])
print(myset)

noset = set([1,2,3,4,5,5])
print(noset)

noset.pop()
print("after .pop()",noset)

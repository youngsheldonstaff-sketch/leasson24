import array as arr

arraynum = arr.array("i",[1,2,2,3,4,5,6,7,8])
print(arraynum)

print("number of occurrences of 2:")
print(arraynum.count(2))

arraynum.reverse()

print ("reversed array:",arraynum)

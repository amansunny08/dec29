x = tuple(range(1,12))
print(x)

print("#########for loop####################")
for i in x:
    print(i)
print("#############In keyword && if else ################")
if 5 in x:
    print("5 is present")
else:
    print("5 is not present")    

print("#############Count################")
print(x.count(2))
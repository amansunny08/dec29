x = list(range(1,11))

print("##########Complete list###################")
print(x)

print("########## for loop###################")
for i in x:
    print(i)

print("############In Keyword && if else#################")
if 5 in x:
    print("5 is present")
else:
    print("5 is not present")

print("############append list#################")

x.append("apple")
x.append("kiwi")
print(x)

print("##########append list inside list###################")
y = ['abc', 'xyz']

x.append(y)
print(x)

print("##################Extend list###########")
z = ['bus', 'car', 123]
y.extend(z)

print(y)
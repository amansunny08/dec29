user = {
    "name" : "aman",
    'age' : 24,
    'hobbies' : ['cricket', 'football', 'hockey']
 }

print("############In keyword && If condition#################")

if 'name' in user:
    print(f"{'name'} is present" )
else: 
    print(f"{'name'} is not present")

print("##########for loop###### full list#############")

for i,j in user.items():
    print(f"{i} : {j}")

print("###########update dictionary##################")    

other_info = {
    "section" : 'B',
    "Roll no" : 123
}

user.update(other_info)

print(user)

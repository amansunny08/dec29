user = {
    "name" : "aman",
    'age' : 24,
    'hobbies' : ['cricket', 'football', 'hockey']
 }

print("############In keyword && If condition#################")

if 'ages' in user:
    print(f"{'ages'} is present" )
else: 
    print(f"{'age'} is not present")

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

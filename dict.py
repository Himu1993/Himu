user = {"id":1, "name":"himu", "dob" : "1994.04.22"}

#print(len(user))  #print(user ["id"]), print(user)

#for data in user:
   # print(data) #index came with data 

 #for data in user.values():
    #print(data )
user = {"id":1, "name":"himu", "dob" : "1994.04.22"}

for key, data in user.items():  #when i need to see data with value
    #print(key,data )

    sam_dist ={"a":1,"b":2,"c":3}
    new_dist = {key:value  for key,value in sam_dist.items() if value<3}

    print(new_dist)
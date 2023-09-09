
cake_list = ["bf" , "vc" , "cc"]
# list access - i) indexing ii) slicing
print(cake_list[2])
#print(len(cake_list))

product_list =[0,1,2,3,4,5,6,7,8,9,10]

#print (product_list[6])
#print (product_list[2:7])

print (product_list[-2::-2]) # start:end:step. #based on index



serial = [1,2,3,4,5,6,3,3]
print(serial)
serial.append(7) # append alwaays make single value 
print (serial)
serial.extend([8,9,10]) #extend formula can add multiple value at a same time.
print(serial)


serial.insert(0,11)
print(serial)

serial.remove(11) #remove function can remove single or multiple value at a same time. or pop function also possible 
print (serial)

index = serial.index(9) #inform where the value is 
print(index)

count = serial.count(3)
print(count)



name = "Md Mohaiminul islam"
up_case = name.upper()
lower_case = up_case.lower
cap_case = name.capitalize()


demo1='mmi,developer,food lover' 
rep_text=demo1.replace('mmi','softwar developer')
print(rep_text)

split_text1 =demo1.split()   
split_text2 =demo1.split('d')

print(split_text1) #space oriented separetor 
print(split_text2)
print(rep_text) 

demo3 = 'item found' 
split_text4 = demo3.split(" ")
print(split_text4)
count = split_text4[-1]
print(demo3[-1])
size_demo3= len(demo3)
print(demo3[size_demo3-1])
pos1=demo3.find("item")
pos2=demo3.index("item")
print(pos1)
print(pos1)
cnt=demo3.count("item")
print(cnt)
pref=demo3.endswith("found")
print(pref)


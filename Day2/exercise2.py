import re

file_object = open(r"input.txt","r")

count = 0
valid = 0
valid1 = 0

#split password string
def split(inputstring):
	return[char for char in inputstring]


for i in file_object.read().strip().splitlines():
	#split data info
	my_list = re.split('[ :-]',i)
	a = split(my_list[4])
	#part1
	for j in a:
		if my_list[2] == j:
			count +=1
	if int(my_list[0]) <= count <= int(my_list[1]):
		valid += 1
	count = 0

	#part2
	if (my_list[2] == a[int(my_list[0])-1]) ^ (my_list[2] == a[int(my_list[1])-1]):
		valid1 +=1

print(valid)
print(valid1)



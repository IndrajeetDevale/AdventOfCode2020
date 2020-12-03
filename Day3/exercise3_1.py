#file_object = open(r"input.txt","r")

p1 =0
count = 0
with open('input.txt') as fin:
	next(fin) # cast into oblivion
	for line in fin:
		#print(len(i))
		p1+=3
		#my_list = i.strip()
		if p1+1 > len(line)-1:
			p1 = p1 - 31 
		if line[p1] == '#':
			count+=1

print(count)
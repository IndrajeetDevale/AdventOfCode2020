file_object = open(r"input.txt","r")
values = [int(i) for i in file_object.read().strip().splitlines()]
n = len(values)

#solution 1
for i in range(len(values)-1):
	for j in range(i+1,len(values)):
		if values[i] + values[j] == 2020:
			print (values[i]*values[j])
			break
			
#solution 2
for i in range(len(values)-2):
	for j in range(i+1,len(values)-1):
		if values[i]+values[j] <2020:
			for k in range(j+1,len(values)):
				if values[i]+values[j]+values[k] == 2020:
					print(values[i]*values[j]*values[k])
					break
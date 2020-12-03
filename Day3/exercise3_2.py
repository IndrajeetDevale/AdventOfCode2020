
G=[]

slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
with open('input.txt') as fin:
	#next(fin)  cast into oblivion
	for line in fin:
		G.append(list(line.strip()))
ans = 1
for (ac,ar) in slopes:
	r = 0
	c = 0
	p2 = 0
	while r+1 < len(G):
		c+=ac
		r+=ar
		if G[r][c%len(G[r])]=='#':
			p2 +=1
	ans *= p2
print(ans)
import re
import string

f1 = open("bmoe.txt",'r',encoding = 'utf-8')
f = open("bmoe1.txt","r",encoding = 'utf-8') 
f2 = open("node.js",'w',encoding = 'utf-8')


f2.write("var nodes = [")
t = 0
node = []
for x in range(0,256):
	single = []

	num = f1.readline().strip()
	name = f1.readline().strip()
	cartoon = f1.readline().strip()
	ID = x
	single.append(num)
	test = cartoon.split(" ")
	line = f.readline().strip()
	result = re.findall(r'\S*\s/\s\S*\s/\s\S*',line)
	if result:
		tag = result[0].split('/')
		for y in range(0,len(tag)):
			tag[y] = tag[y].strip()
		print(tag)
		single.append(tag)
	
	search = line.split(" ")
	if test[0].strip() == search[0].strip() and result:
		node.append(single)
		if t >= 1:
			f2.write(", ")
		f2.write("{num: \"" + num +"\",");
		f2.write("name: \"" + name +"\","); 
		f2.write("cartoon: \"" + cartoon +"\","); 
		f2.write("id: {:d}".format(ID)+"}"); 
		t = t + 1
f2.write("];")
f2.write("var edges = [")
s = 0
p = []
t = 0
for x in range(0,74):
	for y in range(x + 1,74):
		w = 0
		f = []
		for z in node[x][1]:
			if z in node[y][1]:
				w = w + 1
		if w > 0:
			f.append(x)	
			f.append(y)	
			f.append(w)	
			p.append(f)	
	t = t + 1
t = 0
print(t)
for x in p:
	if t >= 1:
		f2.write(", ")
	f2.write("{"+"source: {:d},".format(x[0]));
	f2.write("target: {:d},".format(x[1])); 
	f2.write("weight: {:f}".format(abs(int(re.findall("\d+", node[x[0]][0])[0]) - int(re.findall("\d+", node[x[1]][0])[0]))/ x[2] / 100)+"}"); 
	t = t + 1
f2.write("];")
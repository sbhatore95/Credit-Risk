f = open('result.csv', 'r')
fw = open('result1.csv', 'w')
line = f.readline()
out = ""
count = 0
for i in range(0, len(line)):
	if(line[i] == '.'):
		count = count + 1
	if(count == 3):
		fw.write(out + '\n')
		out = ""
		count = 0
	else:
		out = out + line[i]

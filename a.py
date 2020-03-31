f = open('dataset.csv', 'r')
f1 = open('id_dataset.csv','w')
line = f.readline()
count = 1
while(line != ""):
	line = str(count) + ',' + line
	f1.write(line)
	line = f.readline()
	count = count + 1
f.close()
f1.close()

f = open('result.csv', 'r')
line = f.readline()

ans = [0]*10
while(line != ""):
	sp = line.split(',')
	if(float(sp[0]) < 0.1):
		ans[0] = ans[0] + 1
	elif(float(sp[0]) < 0.2):
		ans[1] = ans[1] + 1
	elif(float(sp[0]) < 0.3):
                ans[2] = ans[2] + 1
	elif(float(sp[0]) < 0.4):
                ans[3] = ans[3] + 1
	elif(float(sp[0]) < 0.5):
                ans[4] = ans[4] + 1
	elif(float(sp[0]) < 0.6):
                ans[5] = ans[5] + 1
	elif(float(sp[0]) < 0.7):
                ans[6] = ans[6] + 1
	elif(float(sp[0]) < 0.8):
                ans[7] = ans[7] + 1
	elif(float(sp[0]) < 0.9):
                ans[8] = ans[8] + 1
	else:
                ans[9] = ans[9] + 1
	line = f.readline()
f.close()
print(ans)

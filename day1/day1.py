file_reader = open("text", 'r')
for i in file_reader:
	data = str(i)
data = data.split(" ")
data = data[:len(data) - 1 :]
sum = 0
num_dict = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
print(data[0:5])
for i in data:
	temp_num = ""
	for j in range(len(i)):
		try:
			if(i[j:j+3] in num_dict.keys()):
				temp_num += str(num_dict[i[j:j+3]])
			elif(i[j:j+4] in num_dict.keys()):
				temp_num += str(num_dict[i[j:j+4]])
			elif(i[j:j+5] in num_dict.keys()):
				temp_num += str(num_dict[i[j:j+5]])
			elif(i[j] in "0123456789"):
				temp_num += i[j]
		except IndexError:
			pass
	temp_num_num = int( str(temp_num[0]) + str(temp_num[-1]))
	sum += temp_num_num
print(sum)

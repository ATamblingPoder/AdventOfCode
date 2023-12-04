not_special = "0123456789."
numms = "0123456789"
limit = 10
file = open("text", "r")
data = []
for i in file.readlines():
    data.append(i.lstrip().rstrip())

covered = []
for j in range(limit):
    temp = []
    for k in range(limit):
        temp.append(0)
    covered.append(temp)

for k in range(limit):
    for lol in range(limit):
        if (data[k][lol] not in not_special):
            try:
                covered[k - 1][lol - 1] = 1
                covered[k - 1][lol] = 1
                covered[k - 1][lol + 1] = 1
                covered[k][lol - 1] = 1
                covered[k][lol] = 1
                covered[k][lol + 1] = 1
                covered[k + 1][lol - 1] = 1
                covered[k + 1][lol] = 1
                covered[k + 1][lol + 1] = 1
            except IndexError:
                pass

numbers = []
# for k in range(limit):
#    l = -1
#    for t in range(limit):
#        l+= 1
#        if(data[k][l] in numms):

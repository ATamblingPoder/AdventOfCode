file = open("text", "r")
sum = 0
count = 0
valid_states = []
for i in file:
    min_valid = {"red":0,"blue":0, "green":0}
    count += 1
    i = i.split(":")
    i = i[1]
    i = i.split(";")
    i = [j.lstrip().rstrip() for j in i]
    #print(f"{count} : {i}")
    for roll in i:
        roll = roll.split(",")
        roll = [j.lstrip().rstrip() for j in roll]
        #print(roll)
        for dice in range(len(roll)):
            temp = roll[dice].split(" ")
            #print(temp)
            if(int(temp[0])) > min_valid[temp[1]]:
                min_valid[temp[1]] = int(temp[0])
    print(min_valid)
    sum += min_valid["red"] * min_valid["green"] * min_valid["blue"]
print(sum)

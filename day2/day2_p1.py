file = open("text", "r")
the_valids = {"red":12, "green":13, "blue":14}
count = 0
valid_states = []
for i in file:
    #if(count > 10):
    #    exit()
    count += 1
    i = i.split(":")
    i = i[1]
    i = i.split(";")
    i = [j.lstrip().rstrip() for j in i]
    print(f"{count} : {i}")
    super_valid_roll = 1
    for roll in i:
        roll = roll.split(",")
        roll = [j.lstrip().rstrip() for j in roll]
        #print(roll)
        valid_roll = 1
        for dice in range(len(roll)):
            temp = roll[dice].split(" ")
            #print(temp)
            if(the_valids[temp[1]] >= int(temp[0])):
                valid_roll = valid_roll and 1
            else:
                valid_roll = valid_roll and 0
        super_valid_roll = super_valid_roll and valid_roll
    print(super_valid_roll)
    if(super_valid_roll):
        valid_states.append(count)
print(valid_states)
print(sum(valid_states))

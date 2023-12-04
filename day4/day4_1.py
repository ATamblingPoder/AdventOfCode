file = open("text", "r")

sum = 0


def remove_spaces(list_to_remove):
    new_list = []
    for i in list_to_remove:
        # print(i)
        if (i == " " or i == ''):
            pass
        elif (i == "  "):
            pass
        elif (i == "   "):
            pass
        else:
            new_list.append(i)
    return new_list


for line in file.readlines():
    line = line.split(":")
    line = line[1]
    column = line.split("|")
    column = [duh.lstrip().rstrip() for duh in column]
    test_from = column[0].split(" ")
    test_from = remove_spaces(test_from)
    test_from = [int(duh) for duh in test_from]
    test_to = column[1].split(" ")
    test_to = remove_spaces(test_to)
    test_to = [int(duh) for duh in test_to]
    count = 0
    for i in test_from:
        if (i in test_to):
            count += 1
    if (count):
        sum += 2**(count - 1)

print(sum)

f = open('persian_dict_19k.txt')
h = open('words.txt', 'w', encoding='utf-8')

for line in f:
    line = line.split(':')
    firstElement = line[0]
    # print(firstElement)
    h.write(firstElement + '\n')

f.close()


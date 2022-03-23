import csv

f = open("./persian_dict_19k.csv", "r")
# print(f.read())

with open('persian_dict_19k.txt', 'w', encoding='utf-8') as h:
    h.write(f.read())
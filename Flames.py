#!/usr/bin/env python3
boy_name = list(input("Type Name of Boy: ").lower())
girl_name = list(input("Type Name of Girl: ").lower())
i = j = index = 0
for i in range(len(boy_name)):
    for j in range(len(girl_name)):
        if (boy_name[i] == girl_name[j]):
            boy_name[i] = girl_name[j] = ""
            #break
count = len("".join(boy_name)+"".join(girl_name))

flames = ["F", "L", "A", "M", "E"]

while len(flames) > 1:
    for i in range(count):
        index += 1
        if index > len(flames):
            index = 1
    flames.remove(flames[index-1])
    index -= 1

result = {"F" : "Friends", "L" : "Love", "A" : "Affection",
            "M" : "Marriage", "E" : "Enemy"}

print(result[flames[0]])
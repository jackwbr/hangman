word = input("enter word: ")
listword = list(word)
print(listword)
    
contlist = listword

z = len(word)

i = 0
while i < z:
    contlist[i] = "_"
    i = i + 1

print(contlist)
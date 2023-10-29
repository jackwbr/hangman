word = input("enter word: ")
listword = list(word)
print(listword)
    
contlist = listword

x = 0
global x

for i in range(25):
    contlist[x] = "_"
    x = x + 1

print(contlist)
print("Enter a string: ")
s = input()
s = s.lower()
letters = []
for i in s.split():
    for j in i:
     letters.append(j)
d = {x: s.count(x) for x in s if x in letters}
print(d)

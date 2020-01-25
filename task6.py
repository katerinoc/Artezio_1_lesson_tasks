print("Enter a number")
n = int(input())
count = 0
list_of_n = []
while count < n:
    count = count+1
    list_of_n.append(count)
d = {x: x*x for x in list_of_n}
print(d)

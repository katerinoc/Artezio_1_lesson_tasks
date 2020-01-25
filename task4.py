print("How many words do you want in your list?")
numb = int(input())
count=0
your_list=[]
res=0
while count<numb:
    print("Enter a word: ")
    word = input()
    while len(word) < 2:
        print("Incorrect length! Try again")
        word = input()
    your_list.append(word)
    count = count+1
print(your_list)

for w in your_list:
    if w[-1] == w[:1]:
        res = res+1
print(res)


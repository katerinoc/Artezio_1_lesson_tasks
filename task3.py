print("Enter a string: ")
s = input()
first = s[:2]
last = s[len(s)-2:len(s)]
new_s = first + last
if len(s)<2:
    print('Empty string!')
else:
    print(new_s)

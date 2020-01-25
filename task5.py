print("Enter your first set:")
set_1=input()
set_1=set_1.split()
set_1=set(set_1)
print("Enter your second set:")
set_2=input()
set_2=set_2.split()
set_2=set(set_2)
print("Enter your third set:")
set_3=input()
set_3=set_3.split()
set_3=set(set_3)
if set_3.issubset(set_1) and set_3.issubset(set_2):
    print('True')
else:
    print('False')


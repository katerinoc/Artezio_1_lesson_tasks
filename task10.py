print('Enter 1 list:')
first_list=input()
first_list=first_list.split()
print('Enter 2 list:')
second_list=input()
second_list=second_list.split()

difference_list=set(first_list)^set(second_list)

print(difference_list)

print('Enter name and surname: ')
name = input()
name = name.split()
print(' '.join(i.capitalize() for i in name))

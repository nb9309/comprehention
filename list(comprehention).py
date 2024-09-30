lst = []
while 9:
    inp = input()
    if inp == '!':
        break
    elif inp.isdigit():
        lst.append(inp)
    else:
        print('invalid input ---> try again')

print(lst)
ls = [val for val in lst if int(val)<40]
print(ls)
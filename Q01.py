# Q1
suplist = ['math', 'chemistry', 'english', 'history', 'bio', 'physics']
print(suplist)
supdel = input('welcome dear,please which one of the list above you dont like !:')
# flag = False
# while flag:
if supdel == suplist[0]:
    suplist.pop(0)
    print(suplist)
elif supdel == suplist[1]:
    suplist.pop(1)
    print(suplist)
elif supdel == suplist[2]:
    del suplist[2]
    print(suplist)
elif supdel == suplist[3]:
    suplist.pop(3)
    print(suplist)
elif supdel == suplist[4]:
    suplist.pop(4)
    print(suplist)
elif supdel == suplist[5]:
    suplist.pop(5)
    print(suplist)

else:
    print('not recognize  subject , please choose again!')

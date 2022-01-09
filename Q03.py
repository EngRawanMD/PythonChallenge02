#Q03
print('****WELCOME****')
partyList = []
maxlenlist = 3
while len(partyList) < maxlenlist:
    invitedList = input('Please enter unless three names you want to invite them to party^^: ')
    partyList.append(invitedList)
print(partyList)
choice = input('Do you want to enter more! yes/no: ')
if choice == 'yes':
    while True:
        invitedList = input('Please enter more names you want to invite them to party^^: ')
        partyList.append(invitedList)
        choice = input('Do you want to enter more! yes/no: ')
elif choice == 'no':
        print('here is your number of names in invited list', len(partyList))
        print(partyList)
# elif choice == 'no':
#     print('here is your number of names in invited list', len(partyList))
#     print(partyList)








print('Welcome To The SplitSmart App')
person = input('Enter Your Name: ')

print('Enter 1 if you want to view your Balance or Enter 2 if you want to Add Expense: ')
while True:
    rn = int(input('Enter 1 or 2: '))
    if rn == 1:
        print("You have chosen 'View Balance'.")
        break
    elif rn == 2:
        print("You have chosen 2 'Add Expenses'. ")
        print('enter the comma separated names of the members.')
        aa = input()
        print('Total amount paid.')
        bb = int(input())
        d = aa,bb
        with open(person, 'a') as filecope:
            for leadset in d:
                filecope.write('%s\n' % leadset)

        g = open(person, 'r')
        cc = (g.readlines())
        # g.close()
        break
    else:
        print('Please enter no. 1 or 2')


file = open(person, 'a')
# file.write('I Paid: rs.'+str(exp)+'\n')
file.close()




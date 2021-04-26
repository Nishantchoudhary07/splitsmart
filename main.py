# print("Welcome To The Split Smart Calculator")
# total_bill = int(input("What is the total bill?: "))
# number_of_people = int(input("How many people are splitting the bill?: "))
# print("\n")
# payment_per_person = int(total_bill / number_of_people)
# total_bill_float = int(total_bill)
# tip_and_total = total_bill_float
# print(f"Total bill : tip_and_total")
# print(f"Each person owes: {payment_per_person}")

# not complete yet.



print('Welcome To The SplitSmart App')
person = input('Enter Your Name: ')
# exp = int(input('Enter The Expense: '))

print('Enter 1 if you want to view your Balance or Enter 2 if you want to Add Expense: ')
while True:
    rn = int(input('Enter 1 or 2: '))
    if rn == 1:
        print("You have chosen 'View Balance'.")
        # r'C:\Users\Akhilesh\Desktop\splitsmart\Nishant'
        break
    elif rn == 2:
        print("You have chosen 2 'Add Expenses'. ")
        break
    else:
        print('Please enter no. 1 or 2')


file = open(person, 'a')
# file.write('I Paid: rs.'+str(exp)+'\n')
file.close()

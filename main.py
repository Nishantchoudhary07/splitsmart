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
exp = int(input('Enter The Expense: '))

file = open(person, 'a')
file.write('I Paid: rs.'+str(exp)+'\n')
file.close()

# def one_or_two():
#     inp = input("Choose 1 or 2")   # Choose 1 to View Balance and choose 2 to Add Expenses.
#     if inp == "1":
#         print("View Balance: ")
#     elif inp == "2":
#         print("Add Expenses: ")
#     else:
#         print("You must choose between 1 or 2")
#         return one_or_two()
# one_or_two()

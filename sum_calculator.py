# I use this program to sum my expenses by month

month_expenses = []
prompt = 'Enter your expense. Enter "0" when finished:  '
expense = input(prompt)

while expense != 0:
    month_expenses.append(expense)
    expense = input(prompt)

total = 0
for item in month_expenses:
    total += item

print("Monthly expenses are " + str(total))
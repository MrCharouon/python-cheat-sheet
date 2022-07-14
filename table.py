from prettytable import PrettyTable
name = ["ali", "mehdi"]
age = ["23", "12"]

columns = ['Name', 'Age']

newTable = PrettyTable()
newTable.add_column(columns[0], name)
newTable.add_column(columns[1], age)

print(newTable)

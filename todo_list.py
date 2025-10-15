todos = ["Do homework", "Buy Milk", "Go to school"]
print(todos)
for i in range(2):
    todos.append(input("Enter tasks: "))
    print(todos)
with open('todos.txt', 'w') as f:
    f.write("\n".join(todos))
with open('todos.txt', 'r') as f:
    print(f.read())
f.close()
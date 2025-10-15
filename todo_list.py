todos = ["Do homework", "Buy Milk", "Go to school"]
for i in range(2):
    task = input("Enter tasks: ").strip()
    todos.append(task)
with open('todos.txt', 'w') as f:
    f.write("\n".join(todos))
with open('todos.txt', 'r') as f:
    print(f.read())
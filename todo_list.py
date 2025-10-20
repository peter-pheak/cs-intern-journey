todos = ["Do homework", "Buy Milk", "Go to school"]
for i in range(2):
    task = input("Enter tasks: ").strip()
    todos.append(task)
print(" | ".join(todos))
try:
    index = int(input(f"Delete task by INDEX(0-{len(todos)}): "))
    todos.pop(index)
except ValueError:
    print(">>Nothing changed(input error)<<")
except IndexError:
    print(">>Nothing changed(out of range error)<<")
with open('todos.txt', 'w') as f:
    f.write("\n".join(todos))
with open('todos.txt', 'r') as f:
    print(f.read())
todos = ["Do homework", "Buy Milk", "Go to school"]
while True:
    try:
        option = int(input("Enter 1: Add, 2: Delete, 3: View, 4: Exit: "))
        if option == 1:
            task = input("Enter tasks: ").strip()
            todos.append(task)
        elif option == 2:
            index = int(input(f"Delete task by INDEX(0-{len(todos)-1}): "))
            todos.pop(index)
        elif option == 3:
            print("\n".join(todos))
        elif option == 4:
            break
        else:
            print(">>Invalid input")
        with open('todos.txt', 'w') as f:
            f.write("\n".join(todos))
    except ValueError:
        print(">>Nothing changed(input error)<<")
    except IndexError:
        print(">>Nothing changed(out of range error)<<")
with open('todos.txt', 'r') as f:
    print(f.read())
number_of_commands = int(input("Enter number of commands: "))
counter = 0
items_list = []
while counter < number_of_commands:
    command = input(f"Enter command {counter + 1}: ")
    operation_item = command.split(" ")
    operation = operation_item[0]
    if(operation == "insert" or operation == "remove" or operation == "append"):
        item = int(operation_item[1])
    if operation == "insert":
        index = int(operation_item[1])
        item = int(operation_item[2])
        items_list.insert(index,item) 
    elif operation == "print":
        print(items_list)
    elif operation == "remove":
        items_list.remove(item)
    elif operation == "append":
        items_list.append(item)
    elif operation == "sort":
        items_list.sort()
    elif operation == "pop":
        items_list.pop()
    elif operation == "reverse":
        items_list.reverse()
    counter += 1

stack = []
stack.insert(3, 6)
stack.append(5)
print(stack)
stack.remove(6)
print(stack)


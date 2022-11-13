coment='''todo1 = input(user_prompt)
todo2 = input(user_prompt)
todo3 = input(user_prompt)

# list with todos
todos_list = [todo1, todo2, todo3]
print(todos_list)'''

coment = '''user_prompt = ('Enter a todo:')

# list of todos with append method
list_todos = []

while True:
    todo = input(user_prompt)
    todo = todo.title()
    list_todos.append(todo)
    print(list_todos)'''

# user decide to add or show todos
# lists, while, for

while True:
    user_action = input('Type "add", "show", "edit", "complete" or "exit": ')

    # remove possible white spaces
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input('Insert a to do: ') + '\n'

            # read the existint entries on the txt file
            # way 1
            comment='''file = open('files/todos.csv', 'r')

            #create list with entries from the text file
            todos = file.readlines()
            file.close()'''

            # way 2: we don't need to close the file
            with open('files/todos.csv', 'r') as file:
                todos = file.readlines()

            # add entry to list
            todo = todo.title()
            todos.append(todo)

            # write to file
            # way 1
            comment='''file = open('files/todos.csv', 'w')
            file.writelines(todos)
            file.close()'''

            # way 2: we don't need to close the file
            with open('files/todos.csv', 'w') as file:
                file.writelines(todos)

        case 'show' | 'display': # | means or
            # read the existint entries on the txt file

            file = open('files/todos.csv', 'r')
            todos = file.readlines()
            file.close()

            # ways to remove \n
            commeent='''new_todos = []
            for item in todos:
                item = item.replace('\n', '')
                new_todos.append(item)

            # or new_todos = [item.strip('\n') for item in todos] '''

            # show todos
            for index, item in enumerate(todos): # to indicate the to do index
                item = item.strip('\n') # remove the '\n'
                row = f'{index + 1}-{item}'
                print(row)

        case 'edit':
            number = int(input('Number of the entry to edit: ')) # qsk the user which to do to edit
            new_todo = input('Write the replace todo: ')

            with open('files/todos.csv', 'r') as file:
                todos = file.readlines()

            number = number - 1
            todos[number] = new_todo.capitalize() + '\n'

            with open('files/todos.csv', 'w') as file:
                file.writelines(todos)

        case 'complete':
            number = int(input('Number of the entry to mark as completed: '))

            with open('files/todos.csv', 'r') as file:
                todos = file.readlines()

            todo_to_remove = todos[number - 1]

            todos.pop(number - 1)

            with open('files/todos.csv', 'w') as file:
                file.writelines(todos)

            message = f'The todo removed was: {todo_to_remove}'
            print(message)

        case 'exit':
            break

        case _: # _ means anything else
            print('Please write something correct...')

print('end of program!')
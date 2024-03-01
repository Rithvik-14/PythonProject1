import functions
import PySimpleGUI as sg
import time

sg.theme("Black")

clock = sg.Text('',key='clock')
label = sg.Text("Type in a to-do:")
input_box = sg.InputText(tooltip="Enter todo", key="todo")  # tooltip show text when mouse hovers over it.
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todo(),key="todos",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")


window = sg.Window('My To-Do App',
                   layout=[[clock],
                           [label], [input_box, add_button],
                           [list_box, edit_button,complete_button],
                           [exit_button]],
                   font=('Arial', 12))
# So every list is like a row in GUI.
while True:                              # so gui doesn't get off
    event, values = window.read(timeout=400)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case "Add":
            todos = functions.get_todo()
            new_todo = values['todo'] + "\n"   # since values output is in dict. so values{key:value}-->values[key]== value.
            todos.append(new_todo)
            functions.write_todo(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todo()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todo(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item from the list.",font=('Arial',12))

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todo()
                todos.remove(todo_to_complete)
                functions.write_todo(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')            # this to remove from the input box too
            except IndexError:
                sg.popup("Please select an item from the list.",font=('Arial',12))
        case "Exit":
            break
        case 'todos':                                       # todos is key of listbox
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break
window.close()

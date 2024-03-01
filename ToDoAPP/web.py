import streamlit as st
import functions


todos = functions.get_todo()       # import list of todos to here


def add_todo():
    todo = st.session_state["new_todo"]+ "\n"
    todos.append(todo)
    functions.write_todo(todos)


st.title("My Todo App")
st.subheader("This is my todo lists")
st.write("This app is for increasing productivity.")


st.text_input(label="Enter todo:",placeholder='Add new todo...',
              on_change=add_todo,key="new_todo")       # text box

incrementor = 1
for index,todo_s in enumerate(todos):
    checkbox= st.checkbox(todo_s, key=incrementor)
    incrementor = incrementor+1
    if checkbox:
        todos.pop(index)
        functions.write_todo(todos)
        del st.session_state[incrementor]
        st.experimental_rerun()


st.session_state
import streamlit as st
from modules import todo_functions as f

# import todos
todos = f.get_todos()

# get and write todo
def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    f.write_todos(todos)

todos = f.get_todos()

st.title('Todo app')

# to complete the todo selected
# eliminate the todo from the state
# and rerun the checkboxes
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox == True:
        todos.pop(index)
        f.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.write('##')
st.text_input('',
              placeholder='Enter a todo',
              on_change=add_todo,
              key='new_todo')


st.session_state
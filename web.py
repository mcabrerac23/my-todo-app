import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.set_page_config(layout="wide")

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your <b>productivity<b>", unsafe_allow_html=True)


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="New Jersey", placeholder="Add a new todo..",
              on_change=add_todo, key='new_todo')



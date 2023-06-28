import streamlit as st
# library to create webapp
import functions
Tasks = functions.get_tasks()


def add_task():
    task_local = st.session_state["new_task"] + "\n"  # session state is a type of dictionary
    Tasks.append(task_local)
    functions.write_tasks(Tasks)


st.title("My Task App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

for index, task in enumerate(Tasks):  # Task is the list
    checkbox = st.checkbox(task, key=task)  # checkbox stores the value of the dictionary
    if checkbox:
        Tasks.pop(index)
        functions.write_tasks(Tasks)
        del st.session_state[task]  # deletes the key with present ticked task from the session state
        st.experimental_rerun()


st.text_input(label="", placeholder="Enter a task:",
              on_change=add_task, key='new_task')


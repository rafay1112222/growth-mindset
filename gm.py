import streamlit as st
import json

# Load tasks from a file
TASKS_FILE = "tasks.json"
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save tasks to a file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file)

# Initialize tasks
tasks = load_tasks()

# Streamlit UI
st.set_page_config(page_title="To-Do List App", layout="wide")
st.sidebar.title("⭐ Manage Your Tasks")

# Input box to add new tasks
new_task = st.sidebar.text_input("➕ Add a new task:", placeholder="Enter your task here...")
if st.sidebar.button("Add Task"):
    if new_task:
        tasks.append(new_task)
        save_tasks(tasks)
        st.sidebar.success("Task added!")
        st.rerun()

    else:
        st.sidebar.warning("Please enter a task before adding.")

st.title("📝 To-Do List App")
st.subheader("📋 Your To-Do List")

if tasks:
    for i, task in enumerate(tasks):
        if st.checkbox(f"{task}", key=f"task_{i}"):
            tasks.pop(i)
            save_tasks(tasks)
            st.rerun()

else:
    st.info("No tasks added yet. Start by adding a task from the sidebar!")

if st.button("🗑 Clear All Tasks"):
    tasks.clear()
    save_tasks(tasks)
st.rerun()

st.markdown("✅ **Stay organized & productive with this simple To-Do List App!**")

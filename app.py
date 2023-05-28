# to-do list flask app

import os
from flask import Flask, request, render_template
from datetime import date
from models import TaskManager

#### Defining Flask App
app = Flask(__name__)
task_manager = TaskManager()


#### Saving Date today in 2 different formats
date_today = date.today().strftime("%d-%B-%Y")


################## ROUTING FUNCTIONS #########################


#### Our main page
@app.route("/")
def home():
    task_list = task_manager.get_task_list()
    return render_template("index.html", dateToday=date_today, tasklist=task_list)


# Function to clear the to-do list
@app.route("/clear")
def clear_list():
    task_manager.create_new_task_list()
    task_list = task_manager.get_task_list()
    return render_template(
        "index.html",
        dateToday=date_today,
        tasklist=task_list,
    )


# Function to add a task to the to-do list
@app.route("/addtask", methods=["POST"])
def add_task():
    task = request.form.get("newtask")
    task_manager.add_task(task)
    task_list = task_manager.get_task_list()
    return render_template(
        "index.html",
        dateToday=date_today,
        tasklist=task_list,
    )


# Function to remove a task from the to-do list
@app.route("/deltask", methods=["GET"])
def remove_task():
    task_index = int(request.args.get("deltaskid"))
    task_list = task_manager.get_task_list()
    if task_index < 0 or task_index > len(task_list):
        return render_template(
            "index.html",
            dateToday=date_today,
            tasklist=task_list,
            mess="Invalid Index...",
        )
    else:
        removed_task = task_list.pop(task_index)
    task_manager.update_task_list(task_list)
    return render_template("index.html", dateToday=date_today, tasklist=task_list)


#### Our main function which runs the Flask App
if __name__ == "__main__":
    app.run(debug=True)

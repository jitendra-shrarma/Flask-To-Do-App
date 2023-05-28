import os


class TaskManager:
    def __init__(self):
        if "tasks.txt" not in os.listdir("."):
            with open("tasks.txt", "w") as f:
                f.write("")

    def add_task(self, task):
        with open("tasks.txt", "a") as f:
            f.writelines(task + "\n")
    
    def get_task_list(self):
        with open("tasks.txt", "r") as f:
            task_list = f.readlines()
        return task_list
    
    def create_new_task_list(self):
        os.remove("tasks.txt")
        with open("tasks.txt", "w") as f:
            f.write("")

    def update_task_list(self, task_list):
        os.remove("tasks.txt")
        with open("tasks.txt", "w") as f:
            f.writelines(task_list)

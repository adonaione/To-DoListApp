from app.models import Task

#To-Do List Class
# Implement a ToDoList class to manage a list of tasks.
# Include methods for adding tasks, viewing tasks, editing task completion status, deleting tasks, and retrieving tasks by ID.
class ToDoList:
    def __init__(self, task_id, descript, completion_status):
        self.task_id = task_id
        self.descript = descript
        self.completion_status = completion_status
        self.tasks = []
    # #Display Task in a user-freindly manner
    # def __str__(self):
    #     print(f'The unique ID for this task is {self.uniq_id}, their task(s) are/is {self.descript}. Their completion status is: {self.completion_status}')

    # Private Method that will get a task by its ID or return None if no task with that ID
    def _get_task_from_id(self, task_id):
        # Loop through all of the tasks in the app
        for task in self.tasks:
            # If the task's ID matches the task_id arugment
            if task.id == task_id:
                # return the task instance
                return task
        # If we finish the loop, that means the post with that ID does not exist
        return None


    
    def __init__(self, uniq_id, descript, completion_status):
        super().__init__(uniq_id, descript, completion_status)
        
    #Method for adding a task
    def moreTasks(self, listTask):
        self.listTask = listTask
        
        action = self.list_of_tasks.append(listTask)
        print(f'{listTask} has been added to the list of tasks.')

    #method for viewing tasks
    def viewTask(self):
        print(self.list_of_tasks)

    #method for editing task completion status
    def editTask(self, editCompletion):
        self.completion_status

    #method for deleting task
        

    #method for retrieving by ID

        



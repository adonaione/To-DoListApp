from app.models import Task

#To-Do List Class
# Implement a ToDoList class to manage a list of tasks.
# Include methods for adding tasks, viewing tasks, editing task completion status, deleting tasks, and retrieving tasks by ID.
class ToDoList:
    def __init__(self):
        self.tasks = []
        

    # Private Method that will get a task by its ID or return None if no task with that ID
    def _get_task_from_id(self, task_id):
        # Loop through all of the tasks in the app
        for task in self.tasks:
            # If the task's ID matches the task_id arugment
            if task.id == task_id:
                # return the task instance
                return task
        # If we finish the loop, that means the task with that ID does not exist
        return None


    #Method for adding a task
    def create_task(self):
        # Get the name and description for the new task from input
        task_id = input('What would you like to add to the to-do list? ').lower()
        #check to see if task exists already
        if task_id in [t.tasks for t in self.tasks]:
            print(f"The task {task_id} is already on the to-do list.")
        else:
            description = input('Please enter a description: ').lower()
            completion_status = input(f'Please enter "complete" or "incomplete": ').lower()
            # Create new instance of a task with the info provided
            new_task = Task(task_id, description, completion_status)
            # add the new task to the to-do list
            self.tasks.append(new_task)
            print(f'{new_task} has been added to the to-do list.')

    #method for viewing tasks
    def view_task(self):
        #check if there are any tasks
        if self.tasks:
            #Loop through the list
            for task in self.tasks:
                print(task)
        else:
            print("The to-do list is empty.")        

    #method for editing task completion status
    def edit_task(self, task_id):
        task = self._get_task_from_id(task_id)
        if task:
            new_status = input("Enter new completion status for this task. Complete/Incomplete ")
            task.completion_status = new_status
        print(f'{task.task_id} has successfully been updated.')

    #method for deleting task
    def delete_task(self, task_id):
        task = self._get_task_from_id(task_id)
        if task:
            confirmation = input(f'Are you sure you want to delete this task from the to-do list? This cannot be undone. Enter "yes" to delete: ').lower()
            if confirmation == "yes":
                #remove task from list
                self.tasks.remove(task)
                print(f'{task.task_id} has been deleted.')
            else:
                print('Canceled')
        else:
            print(f'Task with a name of {task_id} does not exist on the To-Do List.')

    #method for retrieving by ID
    def retrieve_task(self, task_id):
        task = self._get_task_from_id(task_id)
        if task:
            print(Task)
        else:
            print("Does not exist.")



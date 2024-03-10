# User Interactions
# Create a simple user interface for the To-Do List Manager using a loop.
# Provide options for users to:
# 1. Add a new task.
# 2. View all tasks.
# 3. Edit the completion status of a task.
# 4. Delete a task.
# 5. Quit the manager.
# Implement appropriate data validation to handle user input and prevent errors.




from to_do_list import Task

def run_app():
    print("Welcome to the To-Do List App by Adonai Romero")
    #create an instance of the to-do list class
    to_do = Task
    # start running the app until user quits
    while True:
        # include methods for adding tasks, viewing tasks, editing task completion status, deleting tasks, and retrieving tasks by ID.
        print(f"What would you like to do?/nPlease enter a number:/n1. Add Task/n2. View Task(s)/n3. Edit Task Completion Status/n4. Delete Task/n5. Retrieve Task ID/n6. Quit")
        # ask the user what they would like to do
        option = input("What would you like to do today? ")
        while option not in ('1', '2', '3', '4', '5', '6'):
            option = print("Not a valid option, please enter 1, 2, 3, 4, 5, or 6. ")
        if option == 6:
            break
        elif to_do == '1':
            # Call the add task method from the app
            to_do.add_task()
        elif to_do == '2':
            # Call the view task function
            to_do.view_task()
            # call the edit task completion function
        elif to_do == '3':
            to_do.edit_completion()
            # call the delete task function
        elif to_do == '4':
            to_do.delete_task()
            # call the retrieve task ID function
        elif to_do == '5':
            to_do.task_ID()
            # If the post is not a digit, re-ask the question
            while not post_id.isdigit():
                post_id = input('Invalid ID. Must be an interger. Please enter ID again: ')
            # Call the view single post method with the integer version of post_id
            to_do.view_post(int(post_id))
        else:
            print(f'Option {to_do} is a work in progress!')
from datetime import datetime

# creating lists to store usernames and passwords read from the user.txt file
user_file = open('user.txt', 'r+')

username_list = []
password_list = []

for line in user_file:
    user, ppd = line.strip('\n').split(', ')
    username_list.append(user)
    password_list.append(ppd)

user_file.close()

# while loop to validate username and password.
username = input("Username: ")
while username not in username_list:
    print("Enter a valid username")
    username = input("Username: ")

ppd_position = username_list.index(username)
password = input("Password: ")
while password != password_list[ppd_position]:
    print("Enter a valid password")
    password = input("Password: ")


while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    menu = input('''\nPlease select one of the following options below:
r - Register a user
a - Add task
va - View all tasks
vm - View my tasks
e - Exit

: ''').lower()

    if menu == 'r':
        pass
        # allow ONLY the admin the right to add a new user to the user.txt file
        # provide admin a new menu option that allows them to display statistics
        if username != 'admin':
            print("Insufficient Privileges")
        elif username == 'admin':
            admin_new_menu = input('''\nPlease select one of the following options below:
        r - Register a user
        d - Display statistics

        : ''').lower()

            if admin_new_menu == 'r':
                new_username = input("Enter a username: ")
                new_password = input("Enter a password: ")
                confirm_new_password = input("Confirm password: ")

                while confirm_new_password != new_password:
                    print("Passwords does not match")
                    confirm_new_password = input("Confirm password: ")
                else:
                    user_file = open('user.txt', 'a')
                    user_file.write(f"\n{new_username}, {new_password}")
                    user_file.close()

            elif admin_new_menu == 'd':

                total_num_tasks = 0
                total_num_users = 0

                tasks_file = open('tasks.txt', 'r')
                for task in tasks_file:
                    total_num_tasks += 1
                print(f"The total number of tasks are: {total_num_tasks}")
                tasks_file.close()

                user_file = open('user.txt', 'r')
                for task in user_file:
                    total_num_users += 1
                print(f"The total number of users are: {total_num_users}")
                user_file.close()

    elif menu == 'a':
        pass
        # allow a user to add a new task to task.txt file
    
        tasks_file = open('tasks.txt', 'a+')

        # request the following input from the user:
        user_assigned_to = input("Enter username of the person the task is to be assigned to: ")

        task_title = input("Task title: ")

        task_descript = input("Task description: ")

        today = datetime.today()
        date_assigned = today.strftime("%d %b %Y")

        task_complete = False
        if not task_complete:
            task_complete = "No"
        else:
            task_complete = "Yes"

        while True:
            try:
                task_due_date = input("Enter date in the format '01 Jan 1999': ")

                # initializing and checking if format matches the date
                due_date = datetime.strptime(task_due_date, "%d %b %Y")
            except ValueError:
                print("Incorrect date format, please enter correct date format.")
            else:
                if due_date.date() >= datetime.now().date():
                    date_task_due = due_date.strftime("%d %b %Y")
                    tasks_file.write(f"\n{user_assigned_to}, {task_title}, {task_descript}, "
                    f"{date_assigned}, {date_task_due}, {task_complete}")
                    break
                else:
                    print("Date must not be in the past.")
                    
                    tasks_file.close()

    elif menu == 'va':
        pass
        # code to allow user to view all tasks
        tasks_file = open('tasks.txt', 'r')
        task_data = tasks_file.readlines()

        for pos, line in enumerate(task_data, 1):
            task_splitdata = line.strip('\n').split(", ")

            all_tasks = f'————————————————[Task {pos}]————————————————————\n'
            all_tasks += '\n'
            all_tasks += f'User assigned to: \t{task_splitdata[0]}\n'
            all_tasks += f'Task title: \t\t{task_splitdata[1]}\n'
            all_tasks += f'Task description: \t{task_splitdata[2]}\n'
            all_tasks += f'Date assigned: \t\t{task_splitdata[3]}\n'
            all_tasks += f'Task due date: \t\t{task_splitdata[4]}\n'
            all_tasks += f'Task complete?: \t{task_splitdata[5]}\n'
            all_tasks += '\n'

            print(all_tasks)

            tasks_file.close()

    elif menu == 'vm':
        pass
        # code to allow user to view tasks assigned to only them
        tasks_file = open('tasks.txt', 'r')

        for line in tasks_file:
            task_splitdata = line.split(', ')
            if task_splitdata[0] == username:

                my_tasks = f'————————————————[{username}]————————————————————\n'
                my_tasks += f'Task title: \t\t{task_splitdata[1]}\n'
                my_tasks += f'Task description: \t{task_splitdata[2]}\n'
                my_tasks += f'Date assigned: \t\t{task_splitdata[3]}\n'
                my_tasks += f'Task due date: \t\t{task_splitdata[4]}\n'
                my_tasks += f'Task complete?: \t{task_splitdata[5]}'

                print(my_tasks)

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please try again")

import menu
import datetime
import tasks

current_time = datetime.datetime.now()
formatted_time = f"{current_time.year}-{current_time.month}-{current_time.day}-{current_time.hour}"
menu = menu.app_menu()

def main():
    # Startup
    menu.working_menu()

    for task in tasks.task_list:
        due_time = datetime.datetime.strptime(task.due, "%Y-%m-%d-%H")
        if ((due_time - current_time) <= datetime.timedelta(hours=48)):
            print(f"Warning {due_time - current_time}")
            menu.warning_menu(task)

    menu.window.mainloop()

if __name__ == "__main__":
    main()
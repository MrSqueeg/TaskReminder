import menu
import datetime
import tasks

current_time = datetime.datetime.now()
formatted_time = f"{current_time.year}-{current_time.month}-{current_time.day}-{current_time.hour}"
menu = menu.app_menu()

def main():
    # Startup
    menu.working_menu()
    tasks.list_tasks()

    curr = tasks.task_list.head
    while curr:
        due_time = datetime.datetime.strptime(curr.due, "%Y-%m-%d-%H")
        if ((due_time - current_time) <= datetime.timedelta(hours=48)):
            print(f"Warning {due_time - current_time}")
            menu.warning_menu(curr)
        else:
            curr = curr.next

    menu.window.mainloop()

if __name__ == "__main__":
    main()
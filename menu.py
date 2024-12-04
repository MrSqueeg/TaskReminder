import tkinter as tk
import ttkbootstrap as ttk
import time
import tasks

tasks.load_tasks()

class app_menu():
    # Menu initial setup
    window = tk.Tk()
    window.title('Window')
    width = window.winfo_screenwidth()               
    height = window.winfo_screenheight()               
    window.geometry("%dx%d" % (width, height))
    popup_time = 5
    
    def reset_window(self):
        for widget in self.window.winfo_children():
            widget.pack_forget()

    def home_menu(self):
        self.reset_window()

        # Title
        title_label = ttk.Label(master = self.window, text = 'Test label', font = 'Calibri 24 bold')
        title_label.pack()

        frame = ttk.Frame(master = self.window)
        button = ttk.Button(master = frame, text = 'swap menu', command = self.working_menu)
        button.pack(side = 'left', padx = 10)
        add_task = ttk.Button(master = frame, text = 'add task', command = self.working_menu)
        add_task.pack(side = 'left', padx = 10)
        name = ttk.Entry(master = frame, text = 'add task', command = self.working_menu)
        name.pack(side = 'left', padx = 10)
        frame.pack(pady = 10)

    def working_menu(self):
        self.reset_window()
        tasks.list_tasks()

        title_label = ttk.Label(master = self.window, text = 'Are you working?', font = 'Calibri 24 bold')
        title_label.pack()

        frame = ttk.Frame(master = self.window)
        yes_button = ttk.Button(master = frame, text = 'Yes', command = self.working)
        no_button = ttk.Button(master = frame, text = 'No', command = self.not_working)
        yes_button.pack(side = 'left', padx = 10)
        no_button.pack(side = 'left', padx = 10)
        frame.pack(pady = 10)

    def not_working(self):
        self.home_menu()

    def working(self):
        self.window.withdraw()
        time.sleep(self.popup_time)
        self.window.deiconify()
    
    def quit(self):
        print('quitting')
        self.window.destroy()
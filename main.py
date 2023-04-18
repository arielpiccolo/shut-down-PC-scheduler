import os
import tkinter as tk
import time

# definy the shutdown function/action
def shutdown():
    os.system("shutdown /s /t 3")
    

# create a pre-set timing option.
def schedule():
    selected_time = time_srt.get()
    if selected_time == "1 hour":
        wait_time = 3600
    elif selected_time == "3 hours":
        wait_time = 10800
    elif selected_time == "5 hours":
        wait_time = 18000
        # after applying one of the above time pre-sets execute the following.
    os.system(f"shutdown /s /t {wait_time}")
    
root = tk.Tk()
root.title("PC Shutdown Scheduler")

# create time selection input
time_str = tk.StringVar()
time_str.set("Select a pre-set time")
time_label = tk.Label(root, text="Shutdown in:")
time_label.pack(side=tk.LEFT)
time_options = ["1 hour", "3 hours", "5 hours"]
time_input = tk.OptionMenu(root, time_str, *time_options)
time_input.pack(side=tk.LEFT)

# create shutdown button
shutdown_button = tk.Button(root, text="Shotdown now", command=shutdown)
shutdown_button.pack(side=tk.LEFT)

# create schedule button
schedule_button = tk.Button(root, text="Schedule shutdown", command=schedule)
schedule_button.pack(side=tk.LEFT)

root.mainloop()

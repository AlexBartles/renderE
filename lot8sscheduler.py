import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import subprocess
import time
import threading as th

root = tk.Tk()
running = False
encodEing = False
reallot8stype = "D" # Fallback in case something decides to break
stop_event = th.Event()
stop_encodE_event = th.Event()

# Set the window properties
root.title("Lot8s Scheduler")

# Manual debugging toggle
DEBUG = False
#DEBUG = True

if DEBUG == True:
    print("Debugging mode enabled.")

preroll = tk.IntVar(root, 8)

# Lot8s run function
def run():
    while running:
        # Here is where the run the actual lot8s commands, FINALLY!!!!!!!!!
        if DEBUG == True:
            print("Running presentation with flavor: {}".format(reallot8stype))
        subprocess.run(["python3", "load.py", "local", reallot8stype])
        time.sleep(preroll.get())
        subprocess.run(["python3", "run.py", "local"])
        if reallot8stype in ["D", "E", "S"]:
            if stop_event.wait(60):
                break
        if reallot8stype in ["K", "O"]:
            if stop_event.wait(90):
                break
        if reallot8stype in ["N", "L", "M"]:
            if stop_event.wait(90):
                break

def submit_settings():
    global target_time
    global interval
    global running
    
    hour = (lot8sstarttimehour_box.get())
    minute = (lot8sstarttimeminute_box.get())
    interval = (interval_box.get())
    
    target_time = f"{hour:02}:{minute:02}"
    running = True

    check_time()

def check_time():
    global running

    if not running:
        return
    
    current_time = time.strftime("%H:%M")
    
    if current_time == target_time:
        running = True
    else:
        root.after(1000, check_time)

def encodE():
    while encodEing:
        if DEBUG == True:
            print("Running encodE!")
        subprocess.run(["python3", "encodE.py"])
        if stop_encodE_event.wait(600):
            break

# Command for start button
def startbuttoncommand():
    if DEBUG == True:
        print("Flavor: {}".format(value_inside.get()[0]))
        print("Preroll time: {}".format(preroll.get()))
    submit_settings()
    global reallot8stype
    global running
    reallot8stype = value_inside.get()[0]
    if value_inside.get() == "Select an Option":
        messagebox.showwarning("Please select an option!", "Please select an option for what presentation to run! Defaulting to D.")
        reallot8stype = "D"
    if value_inside.get()[0] not in ["D", "E", "K", "O", "N", "L", "M", "S"]:
        print("Lot8s selector broken. Real value is: {}".format(value_inside.get()[0]))
        messagebox.showerror("Unknown presentation type", "Welp, it seems something has broken with the presentation type selector!")
    if preroll.get() <= int("-1"):
        messagebox.showerror("Preroll time is less than 0!", "Please set the preroll time to 0 or something higher!")
    else:
        if running == False:
            running = True
            check_th = th.Thread(target=check_time)
            check_th.start()
            run_th = th.Thread(target=run)
            run_th.start()
            stop_event.clear()
        else:
            messagebox.showerror("Already running presentation!", "The presentation is already running, go check renderE!")

# Command for stop button
def stopbuttoncommand():
    global running
    if running == True:
        running = False
        stop_event.set()
    else:
        messagebox.showerror("Presentation isn't running!", "Not running a presentation, start it first!")

def startencodEcommand():
    global encodEing
    if encodEing == False:
        encodEing = True
        encodE_th = th.Thread(target=encodE)
        encodE_th.start()
        stop_event.clear()
    else:
        messagebox.showerror("Already running encodE!", "Already encodEing!")

def stopencodEcommand():
    global encodEing
    if encodEing == True:
        encodEing = False
        stop_encodE_event.set()
    else:
        messagebox.showerror("encodE isnt running!", "Not encodEing, start it first!")

# All lot8s flavors
lot8s_options = ["Select an Option", "D - 60 seconds", "E - 60 seconds", "K - 90 seconds", "O - 90 seconds", "N - 120 seconds", "L - 120 seconds", "M - 120 seconds", "S - Squeezeback"]

# Set blank option string
value_inside = tk.StringVar(root)
value_inside.set("Select an Option")

# you are cordially invited to have a giant slice of my style
style = ttk.Style(root)

style.configure("my.TLabel", font=("Helvetica", 20, "bold"))

# Create a title (this is already annoying)
ttk.Label(root, text="Lot8s Scheduler", style="my.TLabel").pack(pady=(15, 0), padx=10)
ttk.Label(root, text="by AlexBartles").pack(pady=(0, 10))

# Ask to choose a flavor
lot8stype = ttk.Label(root, text="Choose a flavor below")
lot8stype.pack(pady=5)

# Further questioning continues
question_menu = ttk.OptionMenu(root, value_inside, *lot8s_options)
question_menu.pack(pady=5)

# Preroll time
lot8stype = ttk.Label(root, text="Preroll time (seconds)")
lot8stype.pack(pady=5)

preroll_box = ttk.Spinbox(root, from_=1, to=10, textvariable=preroll)
preroll_box.set(8)
preroll_box.pack(pady=5, padx=10)

# Time to start lot8s
lot8sstarttime = ttk.Label(root, text="Lot8s start time:")
lot8sstarttime.pack(pady=5)

lot8sstarttimehour = ttk.Label(root, text="Hour:")
lot8sstarttimehour.pack(pady=5)

lot8sstarttimehour_box = ttk.Spinbox(root, from_=0, to=23, textvariable=lot8sstarttimehour)
lot8sstarttimehour_box.pack(pady=5)

lot8sstarttimeminute = ttk.Label(root, text="Minute:")
lot8sstarttimeminute.pack(pady=5)

lot8sstarttimeminute_box = ttk.Spinbox(root, from_=0, to=59, textvariable=lot8sstarttimeminute)
lot8sstarttimeminute_box.pack(pady=5)

# Interval time
interval = ttk.Label(root, text="Interval time (seconds)")
interval.pack(pady=5)

interval_box = ttk.Spinbox(root, from_=1, to=120, textvariable=interval)

# Create start button
startbutton = ttk.Button(root, text="Start presentation", style="my.TButton", command=startbuttoncommand)
startbutton.pack(pady=5)

# Create stop button
stopbutton = ttk.Button(root, text="Stop presentation", style="my.TButton", command=stopbuttoncommand)
stopbutton.pack(pady=5)

# Create start encodE button
startencodEbutton = ttk.Button(root, text="Start encodEing", style="my.TButton", command=startencodEcommand)
startencodEbutton.pack(pady=5)

# Create stop encodE button
stopencodEbutton = ttk.Button(root, text="Stop encodEing", style="my.TButton", command=stopencodEcommand)
stopencodEbutton.pack(pady=(5, 15))

root.mainloop()
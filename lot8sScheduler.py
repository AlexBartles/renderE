import tkinter as tk
from tkinter import messagebox
import subprocess
import time
import threading as th

root = tk.Tk()
running = False
global encodEing
encodEing = False
global reallot8stype
reallot8stype = "D" # Fallback in case something decides to break
stop_event = th.Event()
stop_encodE_event = th.Event()

# Set the window properties
root.title("Lot8s Scheduler")
root.configure(background="#ADD8E6")
root.minsize(400, 300)
root.maxsize(1000, 800)
root.geometry("700x500")

# Manual debugging toggle
DEBUG = False
#DEBUG = True

if DEBUG == True:
    print("Debugging mode enabled.")

# Lot8s run function
def run():
    while running:
        # Here is where the run the actual lot8s commands, FINALLY!!!!!!!!!
        if DEBUG == True:
            print("Running lot8s with flavour: {}".format(reallot8stype))
        subprocess.run(["python3", "load.py", "local", reallot8stype])
        time.sleep(3)
        subprocess.run(["python3", "run.py", "local"])
        if reallot8stype in ["D", "E", "S"]:
            if stop_event.wait(60):
                break;
        if reallot8stype in ["K", "O"]:
            if stop_event.wait(90):
                break;
        if reallot8stype in ["N", "L", "M"]:
            if stop_event.wait(90):
                break;

def encodE():
    while encodEing:
        if DEBUG == True:
            print("EncodEing starts now!")
        subprocess.run(["python3", "encodE.py"])
        if stop_encodE_event.wait(600):
            break;

# Command for start button
def startbuttoncommand():
    global reallot8stype
    global running
    reallot8stype = value_inside.get()[0]
    if value_inside.get() == "Select an Option":
        tk.messagebox.showwarning("Please select an option!", "Please select an option for what lot8s to run! Defaulting to D.")
        reallot8stype = "D"
    if value_inside.get()[0] not in ["D", "E", "K", "O", "N", "L", "M", "S"]:
        print("Lot8s selector broken. Real value is: {}".format(value_inside.get()[0]))
        tk.messagebox.showerror("Unknown lot8s type", "Welp, it seems something has broken with the lot8s type selector!")
    else:
        if running == False:
            running = True
            run_th = th.Thread(target=run)
            run_th.start()
            stop_event.clear()
        else:
            tk.messagebox.showerror("Already running lot8s!", "The lot8s are already running, go check renderE!")

# Command for stop button
def stopbuttoncommand():
    global running
    if running == True:
        running = False
        stop_event.set()
    else:
        tk.messagebox.showerror("Lot8s aren't running!", "Not running lot8s, start them first!")

def startencodEcommand():
    global encodEing
    if encodEing == False:
        encodEing = True
        encodE_th = th.Thread(target=encodE)
        encodE_th.start()
        stop_event.clear()
    else:
        tk.messagebox.showerror("Already running encodE!", "Already encodEing!")

def stopencodEcommand():
    global encodEing
    if encodEing == True:
        encodEing = False
        stop_encodE_event.set()
    else:
        tk.messagebox.showerror("EncodE isnt running!", "Not encodEing, start it first!")

# All lot8s flavours
lot8s_options = ["D - 60 seconds", "E - 60 seconds", "K - 90 seconds", "O - 90 seconds", "N - 120 seconds", "L - 120 seconds", "M - 120 seconds", "S - squeezeback"]

# Set blank option string
value_inside = tk.StringVar(root)
value_inside.set("Select an Option")

# Create a title (this is already annoying)
tk.Label(root, text="Lot8s Scheduler", background="#ADD8E6", font=("Helvetica", 16, "bold")).pack(pady=20)

# Ask what type of lot8s to run
lot8stype = tk.Label(root, text="What flavour of lot8s do you want to run?", font=("Helvetica", 12), background="#ADD8E6")
lot8stype.pack(pady=20)

# Further questioning continues
question_menu = tk.OptionMenu(root, value_inside, *lot8s_options)
question_menu.config(bg="#ADD8E6")
question_menu["menu"].config(bg="#ADD8E6")
question_menu.pack(pady=20)

# Create start button
startbutton = tk.Button(root, text="Start lot8s with flavour selected above", font=("Helvetica", 12), background="#ADD8E6", command=startbuttoncommand)
startbutton.pack(pady=20)

# Create stop button
stopbutton = tk.Button(root, text="Stop lot8s", font=("Helvetica", 12), background="#ADD8E6", command=stopbuttoncommand)
stopbutton.pack(pady=20)

# Create start encodE button
startencodEbutton = tk.Button(root, text="Start encodEing", font=("Helvetica", 12), background="#ADD8E6", command=startencodEcommand)
startencodEbutton.pack(pady=20)

# Create stop encodE button
stopencodEbutton = tk.Button(root, text="Stop encodEing", font=("Helvetica", 12), background="#ADD8E6", command=stopencodEcommand)
stopencodEbutton.pack(pady=20)

root.mainloop()
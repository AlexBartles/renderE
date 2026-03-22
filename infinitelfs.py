import time
import subprocess

while True:
  subprocess.run(["python3", "load.py", "local", "D"])
  time.sleep(3)
  subprocess.run(["python3", "run.py", "local"])
  time.sleep(60)

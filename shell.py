import subprocess
import os, traceback
import sys

try:
    toolName = "decision_tree"
    
    shellPath =os.path.join(".","decision_tree","main.py")
    filepath = "python " + shellPath + " " + toolName
    
    if sys.platform.startswith("win32"):
        subprocess.call(["python",shellPath,toolName],shell=True)
    else:
        subprocess.call([filepath],shell=True)

except Exception as e:
    print("An error occurred in the system: ")
    print(e)
    traceback.print_exc()
    print("Please use 'python shell.py " + toolName + "' to run the shell again.")
    print
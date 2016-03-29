import subprocess
import os, traceback

try:
    print os.listdir("./decision_tree")
    print "1"
    toolName = "decision_tree"
    shellPath =os.path.join(".","decision_tree","main.py")
    #shellPath = os.path.abspath(shellPath)
    #shellPath = ".\\decision_tree\\main.py"
    print shellPath

    # shellPath = shellPath.replace('\\', '\\\\')
    #shellPath = '"' + shellPath + '"'
    print shellPath
    print "2"
    
    filepath = "python " + shellPath + " " + toolName
    print filepath
    
    subprocess.call(["python",shellPath,toolName],shell=True)
    #subprocess.call(['python E:\\Courses\\CSC_510\\TestRepo\\decision_tree email'],shell = True)
    print "3"
except Exception as e:
    print("An error occurred in the system: ")
    print(e)
    traceback.print_exc()
    print("Please use 'python shell.py " + toolName + "' to run the shell again.")
    print
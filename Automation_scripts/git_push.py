"""
This is a python script tp automate git push. First it makes sure that the direcory is git initialized, then adds all the modified files.
When the script is called it takes in the commit message
"""

import subprocess
import sys

# STEPS
# 1. CHECK THE COMMIT STATUS. IF NO WORK TO COMMIT STOP ELSE GO TO STEP 2
status = subprocess.run(["git", "status"], capture_output=True, text=True)
# print(status)
if "Changes not staged for commit" in status.stdout or "Untracked files" in status.stdout:
    # 2. ADD MODIFIED FILES
    subprocess.run(["git", "add", "-A"])
     # 3. CHECK FOR COMMIT MESSAGE(REQUIRED) PASSED IN WHEN SCRIPT WAS CALLED
    try:
        message = sys.argv[1]
    except:
        print("Commit message not entered")
        message = input("Enter commit message : ")
    commit_result = subprocess.run(["git", "commit", "-m", message], capture_output=True, text=True)
    # chck to make sure that the commit is successfull
    if commit_result.returncode == 0:
        # if commit is successfull push to remote repo
        push_result = subprocess.run(["git", "push"], capture_output=True, text=True)
        if push_result.returncode == 0:
            print("Push completed")
        else:
            print("Push failed...")
            print(push_result.stderr)
    else:
        print("Error committing message...")
        print(commit_result.stderr)
   
else:
    print("Nothing to commit...")